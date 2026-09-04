#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate — valida esquemas, códigos, organograma, BPMN/Mermaid, renderizações e integridade de data.json.

Uso: python3 scripts/validate.py [--permitir-entries] [--sem-render] [--quiet]
Sai com 1 quando há erros. Avisos não bloqueiam.
"""
import copy
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canvas_lib as cl  # noqa: E402
import render_pop as rp  # noqa: E402

ERROS, AVISOS = [], []


def err(m):
    ERROS.append(m)


def warn(m):
    AVISOS.append(m)


def check_org(org):
    codes, siglas = set(), set()
    labels = set()
    for s in org.setores:
        if s['codigo'] in codes:
            err('organograma: código duplicado %s' % s['codigo'])
        codes.add(s['codigo'])
        if s['sigla'] in siglas:
            err('organograma: sigla duplicada %s' % s['sigla'])
        siglas.add(s['sigla'])
        if s.get('pai') and s['pai'] not in org.by_codigo:
            err('organograma: pai inexistente %s → %s' % (s['codigo'], s['pai']))
        if not re.match(r'^S\d{2}(\.\d{2})?-[A-Z0-9-]+$', s['codigo']):
            err('organograma: código fora do padrão %s' % s['codigo'])
        labels.add(s.get('id_app'))
        labels.update(s.get('aliases') or [])
    for sid in cl.sectors_from_index():
        if sid not in labels:
            err('SECTORS do index.html sem correspondência no organograma canônico: %r' % sid)
    for opt in cl.select_options_from_index():
        if opt not in labels:
            warn('opção do seletor #inSetor sem correspondência no organograma: %r' % opt)
    check_org_embutido(org)
    return siglas


def check_org_embutido(org):
    """O ORGANOGRAMA embutido no index.html deve espelhar o JSON canônico (código, sigla, id_app, pai, nivel, gera_pop, processos)."""
    src = io.open(cl.path('index.html'), encoding='utf-8').read()
    m = re.search(r'const ORGANOGRAMA=(\[.*?\]);\n', src, re.S)
    if not m:
        warn('index.html sem ORGANOGRAMA embutido (aba Agentes)')
        return
    try:
        emb = json.loads(m.group(1).replace('<\\/', '</'))
    except Exception as e:  # noqa: BLE001
        err('ORGANOGRAMA embutido no index.html não é JSON válido: %s' % e)
        return
    e_by = {s['codigo']: s for s in emb}
    for s in org.setores:
        x = e_by.get(s['codigo'])
        if not x:
            err('ORGANOGRAMA embutido: falta %s (rode o patch da aba Agentes / scripts/sync_org.py)' % s['codigo'])
            continue
        for k in ('sigla', 'id_app', 'pai', 'nivel', 'dominio', 'tipo_subdominio'):
            if (x.get(k) or None) != (s.get(k) or None):
                err('ORGANOGRAMA embutido: %s.%s = %r ≠ %r' % (s['codigo'], k, x.get(k), s.get(k)))
        if bool(x.get('gera_pop', True)) != bool(s.get('gera_pop', True)):
            err('ORGANOGRAMA embutido: %s.gera_pop divergente' % s['codigo'])
        pk = [p['codigo'] for p in (x.get('processos_conhecidos') or [])]
        if pk != [p['codigo'] for p in (s.get('processos_conhecidos') or [])]:
            err('ORGANOGRAMA embutido: %s.processos_conhecidos divergente' % s['codigo'])
    for c in e_by:
        if c not in org.by_codigo:
            err('ORGANOGRAMA embutido tem setor inexistente no canônico: %s' % c)


def check_mermaid(txt, onde):
    if not txt or not txt.strip():
        err('%s: Mermaid vazio' % onde)
        return
    abre = len(re.findall(r'^\s*subgraph\b', txt, re.M))
    fecha = len(re.findall(r'^\s*end\s*$', txt, re.M))
    if abre != fecha:
        err('%s: subgraph/end desbalanceados (%d/%d)' % (onde, abre, fecha))
    if not re.match(r'^(flowchart|graph)\s+(TD|LR|TB|RL|BT)', txt.strip()):
        err('%s: cabeçalho Mermaid inválido' % onde)


def check_pop(pop, org, schema, siglas, licoes, render=True):
    c = pop.get('codigo', '?')
    for e in cl.validate_schema(pop, schema):
        err('POP %s: %s' % (c, e))
    if pop.get('id') != cl.pop_id(c):
        err('POP %s: id %r ≠ %r' % (c, pop.get('id'), cl.pop_id(c)))
    sig = cl.sigla_of_code(c)
    if sig not in siglas:
        err('POP %s: prefixo %s não é sigla do organograma' % (c, sig))
    if pop.get('sigla') != sig:
        err('POP %s: campo sigla %r ≠ prefixo %r' % (c, pop.get('sigla'), sig))
    node = org.by_codigo.get(pop.get('setor_codigo'))
    if not node:
        err('POP %s: setor_codigo inexistente %r' % (c, pop.get('setor_codigo')))
    elif node['sigla'] != sig:
        err('POP %s: sigla do setor %s ≠ prefixo do código' % (c, node['sigla']))
    elif node.get('id_app') != pop.get('setor'):
        err('POP %s: setor %r ≠ id_app do organograma %r' % (c, pop.get('setor'), node.get('id_app')))
    pj = cl.pop_paths(pop)[0]
    if not os.path.exists(pj):
        err('POP %s: arquivo canônico ausente em %s' % (c, os.path.relpath(pj, cl.ROOT)))
    passos = (pop.get('playbook') or {}).get('passos') or []
    ns = [p.get('n') for p in passos]
    if ns != list(range(1, len(ns) + 1)):
        err('POP %s: numeração de passos inválida %s' % (c, ns))
    if pop.get('status') in ('em_validacao', 'aprovado') and len(passos) < 3:
        err('POP %s: status %s exige ≥ 3 passos' % (c, pop['status']))
    vers = [ch.get('versao') for ch in pop.get('changelog') or []]
    for a, b in zip(vers, vers[1:]):
        if cl.cmp_version(b, a) < 0:
            err('POP %s: changelog não monotônico (%s → %s)' % (c, a, b))
    if vers and vers[-1] != pop.get('versao'):
        err('POP %s: última versão do changelog %s ≠ versao %s' % (c, vers[-1], pop.get('versao')))
    spec = pop.get('bpmn_spec') or {}
    ids = [e.get('id') for e in spec.get('elementos') or []]
    if len(ids) != len(set(ids)):
        err('POP %s: ids BPMN duplicados' % c)
    for cx in spec.get('conexoes') or []:
        if cx.get('de') not in ids or cx.get('para') not in ids:
            err('POP %s: conexão BPMN com id inexistente %s→%s' % (c, cx.get('de'), cx.get('para')))
    tipos = [e.get('tipo') for e in spec.get('elementos') or []]
    if spec.get('elementos') and ('inicio' not in tipos or 'fim' not in tipos):
        warn('POP %s: fluxograma sem início ou fim' % c)
    for e in spec.get('elementos') or []:
        if e.get('raia') and e['raia'] not in (spec.get('raias') or []):
            err('POP %s: raia %r não declarada' % (c, e['raia']))
    check_mermaid(pop.get('fluxograma_mermaid'), 'POP %s fluxograma' % c)
    check_mermaid(pop.get('organograma_mermaid'), 'POP %s organograma' % c)
    for l in pop.get('licoes_aplicadas') or []:
        if l not in licoes:
            warn('POP %s: lição %s não está aprovada' % (c, l))
    if render and not rp.check_pop(pop, org):
        err('POP %s: %s desatualizado (rode scripts/render_pop.py %s)' % (c, os.path.relpath(cl.pop_paths(pop)[1], cl.ROOT), c))
    for n in re.findall(r'\b(?:Sr\.|Sra\.|Prof\.|Profa\.)\s+[A-ZÁ-Ú]\w+', json.dumps(pop, ensure_ascii=False)):
        warn('POP %s: possível nome de pessoa (LGPD): %s' % (c, n))


def check_entries_hash(data, permitir):
    try:
        base = subprocess.run(['git', 'show', 'HEAD:data.json'], cwd=cl.ROOT, capture_output=True, text=True, check=True).stdout
        base_entries = json.loads(base)['entries']
    except Exception as e:  # noqa: BLE001
        warn('não foi possível ler data.json de HEAD (%s)' % e)
        return
    if cl.entries_hash(base_entries) != cl.entries_hash(data['entries']):
        (warn if permitir else err)('data.json: entries divergem de HEAD (%d → %d entradas)' % (len(base_entries), len(data['entries'])))


def self_test_patch(pops, org):
    if not pops:
        return
    import apply_patch as ap
    pop = copy.deepcopy(pops[0])
    v0 = pop['versao']
    n0 = len(pop['playbook']['passos'])
    patch = {'codigo': pop['codigo'], 'motivo': 'auto-teste', 'autor': 'validate.py', 'fontes': [],
             'passos_adicionados': [{'apos_n': 0, 'passo': {'acao': 'Passo de teste', 'responsavel': 'Teste'}}]}
    novo, tipo, _ = ap.aplicar(pop, patch, org, {'entries': []})
    if tipo != 'minor' or cl.bump_version(v0, 'minor') != novo['versao'] or len(novo['playbook']['passos']) != n0 + 1 or novo['playbook']['passos'][0]['n'] != 1:
        err('auto-teste do patch falhou (%s → %s, %s, %d passos)' % (v0, novo['versao'], tipo, len(novo['playbook']['passos'])))
    vazio = copy.deepcopy(pops[0])
    vazio['playbook']['passos'] = []
    patch3 = {'codigo': vazio['codigo'], 'motivo': 'auto-teste', 'autor': 'validate.py', 'fontes': [],
              'passos_adicionados': [{'apos_n': i, 'passo': {'acao': 'Passo %s' % l, 'responsavel': 'Teste'}} for i, l in enumerate('ABC')]}
    novo3, _, _ = ap.aplicar(vazio, patch3, org, {'entries': []})
    if [p['acao'] for p in novo3['playbook']['passos']] != ['Passo A', 'Passo B', 'Passo C']:
        err('auto-teste do patch: ordem de inserção múltipla incorreta: %s' % [p['acao'] for p in novo3['playbook']['passos']])
    dois = copy.deepcopy(pops[0])
    dois['playbook']['passos'] = [{'n': 1, 'acao': 'Um', 'responsavel': 'T'}, {'n': 2, 'acao': 'Dois', 'responsavel': 'T'}]
    patch4 = {'codigo': dois['codigo'], 'motivo': 'auto-teste', 'autor': 'validate.py', 'fontes': [],
              'passos_adicionados': [{'apos_n': 1, 'passo': {'acao': 'Meio', 'responsavel': 'T'}}, {'apos_n': 9, 'passo': {'acao': 'Fim', 'responsavel': 'T'}}, {'apos_n': 0, 'passo': {'acao': 'Inicio', 'responsavel': 'T'}}]}
    novo4, _, _ = ap.aplicar(dois, patch4, org, {'entries': []})
    if [p['acao'] for p in novo4['playbook']['passos']] != ['Inicio', 'Um', 'Meio', 'Dois', 'Fim']:
        err('auto-teste do patch: inserção intercalada incorreta: %s' % [p['acao'] for p in novo4['playbook']['passos']])
    patch2 = {'codigo': pop['codigo'], 'motivo': 'auto-teste', 'autor': 'validate.py', 'fontes': [], 'passos_removidos': [1]}
    if n0:
        novo2, tipo2, _ = ap.aplicar(pop, patch2, org, {'entries': []})
        if tipo2 != 'major':
            err('auto-teste do patch: remoção deveria ser major (obtido %s)' % tipo2)


def main(argv):
    permitir = '--permitir-entries' in argv
    render = '--sem-render' not in argv
    quiet = '--quiet' in argv
    try:
        data = cl.load_data()
    except Exception as e:  # noqa: BLE001
        err('data.json inválido: %s' % e)
        data = None
    org = cl.Org()
    siglas = check_org(org)
    licoes = set(l['id'] for l in cl.licoes_aprovadas())
    schema = cl.load_schema('pop.schema.json')
    pops = cl.iter_pops()
    codes = [p.get('codigo') for p in pops]
    for c in set(codes):
        if codes.count(c) > 1:
            err('código de POP duplicado: %s' % c)
    for p in pops:
        check_pop(p, org, schema, siglas, licoes, render)
    dschema = cl.load_schema('diagnostico.schema.json')
    import glob
    for f in sorted(glob.glob(os.path.join(cl.DIAG_DIR, '*.json'))):
        d = cl.load_json(f)
        for e in cl.validate_schema(d, dschema):
            err('diagnóstico %s: %s' % (os.path.basename(f), e))
        if d.get('setor_codigo') not in org.by_codigo:
            err('diagnóstico %s: setor_codigo inexistente' % os.path.basename(f))
    aschema = cl.load_schema('agente.schema.json')
    for a in cl.load_json(cl.AG_REG, []):
        for e in cl.validate_schema(a, aschema):
            err('agente %s: %s' % (a.get('id'), e))
        if not os.path.exists(cl.path(a.get('arquivo', ''))):
            err('agente %s: arquivo ausente %s' % (a.get('id'), a.get('arquivo')))
    if data is not None:
        check_entries_hash(data, permitir)
        for k in ('pops', 'diagnosticos', 'agentes', 'diretrizes', 'licoes'):
            ids = [x.get('id') for x in data.get(k) or []]
            if len(ids) != len(set(ids)):
                err('data.json: ids duplicados em %s' % k)
        for p in data.get('pops') or []:
            for e in cl.validate_schema(p, schema):
                err('data.json pops[%s]: %s' % (p.get('codigo'), e))
    self_test_patch(pops, org)
    if not quiet:
        for a in AVISOS:
            print('AVISO:', a)
    for e in ERROS:
        print('ERRO:', e)
    print('validate: %d POP(s), %d erro(s), %d aviso(s)' % (len(pops), len(ERROS), len(AVISOS)))
    return 1 if ERROS else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
