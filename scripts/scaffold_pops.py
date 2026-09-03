#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scaffold_pops — cria POPs-esqueleto determinísticos (sem IA) para setores do organograma canônico (e, com --de-diagnosticos, para processos identificados nos diagnósticos sem POP).

Para cada setor que gera POP:
  • <SIGLA>-00  visão geral do setor, a partir do playbook (entrada pb-*) quando existir;
  • processos conhecidos (códigos legados do manual institucional) em status rascunho;
  • candidatos: entradas tipo=processo com ≥ 3 passos no procedimento (exclui documentos de referência).
Nunca sobrescreve um POP existente.

Uso: python3 scripts/scaffold_pops.py [--setor X ...] [--todos] [--dry-run]
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canvas_lib as cl  # noqa: E402
import bpmn_mermaid as bm  # noqa: E402
import render_pop as rp  # noqa: E402

EXCLUIR_CLASSES = {'Fluxogramas', 'Referência Metodológica', 'Mapeamento de Processos', 'Contatos', 'OVERVIEW', 'PLAYBOOK'}
EXCLUIR_TITULO = re.compile(r'^(manual|question|checklist|fluxograma|contatos|refer[êe]ncia|projeto|consolida|exemplo|planilha|subprocesso .*\(exemplo\))', re.I)
DUPLICATA = re.compile(r'\[c[óo]pia\]|\bc[óo]pia\b|\(vazio\)|\bteste\b|\(2\)', re.I)
VERSAO_RX = re.compile(r'\s*v\d+(\.\d+)*\s*', re.I)
AUTOR = 'scripts/scaffold_pops.py'
LICOES_ESTRUTURAIS = ['L-001', 'L-004', 'L-006', 'L-007']


def normas_de(texto):
    """Divide a normativa por ';' fora de parênteses (ex.: 'A definir (normas; TCE-PR)' permanece um item)."""
    partes, atual, nivel = [], '', 0
    for ch in texto or '':
        if ch == '(':
            nivel += 1
        elif ch == ')':
            nivel = max(0, nivel - 1)
        if ch == ';' and nivel == 0:
            partes.append(atual)
            atual = ''
        else:
            atual += ch
    partes.append(atual)
    out = []
    for n in partes:
        n = n.strip()
        if n and cl.norm(n) not in ('nao especificada', 'a definir', 'nao especificado'):
            out.append(n)
    return out


def make_pop(org, node, codigo, titulo, descricao, fontes, passos_txt=(), normativa='', atencoes=(), subdominio='', escopo='', heranca=None):
    chain = org.chain(node['codigo'])
    divisao = node['nome'] if node['codigo'] == 'S01-DG' or len(chain) < 2 else chain[1]['nome']
    pai = org.by_codigo.get(node.get('pai')) if node.get('pai') else None
    subordinacao = pai['nome'] if pai else ('Reitoria da Unioeste' if node['codigo'] == 'S01-DG' else 'Direção Geral de Campus')
    ids = [e['id'] for e in fontes]
    passos = [{'n': i + 1, 'acao': t.strip(), 'responsavel': 'A definir', 'sistema': '', 'artefato': '', 'prazo': 'A definir', 'evento': '', 'fontes': list(ids)}
              for i, t in enumerate([t for t in passos_txt if str(t).strip()])]
    normas = normas_de(normativa)
    lacunas = ['responsavel', 'gatilho', 'entrada', 'saida', 'kpi', 'contingencia', 'formulario', 'prazo']
    if len(passos) < 3:
        lacunas.insert(0, 'passos')
    if not normas:
        lacunas.append('normativa')
    now = cl.now_iso()
    pop = {
        'id': cl.pop_id(codigo), 'codigo': codigo, 'titulo': titulo, 'setor': node['id_app'], 'setor_codigo': node['codigo'], 'sigla': node['sigla'],
        'versao': '0.1.0', 'status': 'rascunho',
        'ddd': {'divisao': divisao, 'departamento': node['nome'], 'descricao': descricao, 'dominio': node['dominio'],
                'subdominio': subdominio or titulo, 'tipo_subdominio': node.get('tipo_subdominio', 'suporte'), 'contexto': node['codigo'], 'glossario': []},
        'identificacao': {'responsavel': 'A definir', 'periodicidade': 'A definir', 'normativa': normas, 'subordinacao': subordinacao,
                          'produto_atdg': 'POP', 'pasta_onedrive': node.get('pasta_onedrive', '03_MAPEAMENTO DE PROCESSOS')},
        'organograma_mermaid': '',
        'playbook': {'gatilho': {'evento': (heranca or {}).get('gatilho') or 'A definir', 'origem': (heranca or {}).get('origem', '')},
                     'entrada': list((heranca or {}).get('entrada') or []), 'passos': passos, 'saida': list((heranca or {}).get('saida') or [])},
        'artefatos': [], 'decisoes': [], 'pontos_atencao': [a for a in atencoes if str(a).strip()], 'contingencia': [], 'checklist': [], 'kpis': [], 'mapa_contexto': [],
        'fluxograma_mermaid': '', 'bpmn_spec': {'raias': [], 'elementos': [], 'conexoes': [], 'observacoes_construcao_miro': ''},
        'changelog': [{'versao': '0.1.0', 'data': now[:10], 'autor': AUTOR, 'tipo': 'patch',
                       'mudancas': ['Esqueleto inicial gerado deterministicamente' + ((' a partir do escopo "%s"' % escopo) if escopo else (' a partir das entradas %s' % ', '.join(ids) if ids else ''))],
                       'fontes': list(ids), 'motivo': 'Scaffold do piloto (todos os setores do organograma)'}],
        'validacao': {'elaboracao': 'ATDG — Assessoria Técnica da Direção Geral', 'revisao': 'A definir (responsável do setor)', 'aprovacao': 'Direção Geral do Campus', 'data_aprovacao': ''},
        'licoes_aplicadas': list(LICOES_ESTRUTURAIS), 'lacunas': lacunas, 'observacoes': '',
        'fontes_entradas': list(ids), 'hash_fontes': cl.hash_fontes(fontes), 'agente': '',
        'versao_diretrizes': cl.diretrizes_versao(), 'criado_em': now, 'atualizado_em': now,
    }
    if heranca:
        h = heranca
        if h.get('gatilho'):
            pop['lacunas'] = [l for l in pop['lacunas'] if l != 'gatilho']
        if h.get('saida'):
            pop['lacunas'] = [l for l in pop['lacunas'] if l != 'saida']
        if h.get('entrada'):
            pop['lacunas'] = [l for l in pop['lacunas'] if l != 'entrada']
        if h.get('artefatos'):
            pop['artefatos'] = [{'nome': a, 'tipo': 'documento', 'sistema': '', 'campos_chave': [], 'responsavel_preenchimento': ''} for a in h['artefatos']]
        if h.get('interfaces'):
            pop['mapa_contexto'] = [{'origem': node['id_app'], 'destino': i, 'relacao': 'informa', 'artefato': '', 'canal': 'A definir'} for i in h['interfaces'] if i and i != node['id_app']]
        if h.get('lacunas'):
            for l in h['lacunas']:
                if l not in pop['lacunas']:
                    pop['lacunas'].append(l)
        pop['observacoes'] = 'Esqueleto herdado do diagnóstico %s (processo identificado sem POP); gatilho, saída, artefatos e interfaces provisórios — inferência a validar (lição L-008).' % h.get('diag_id', '')
        pop['changelog'][0]['mudancas'] = ['Esqueleto gerado a partir do diagnóstico %s (recomendação: %s)' % (h.get('diag_id', ''), h.get('recomendacao', ''))]
        pop['changelog'][0]['motivo'] = 'Processo identificado no diagnóstico do setor sem POP correspondente'
    bm.refresh_mermaid(pop, org)
    return pop


def de_diagnosticos(org, data, dry_run=False):
    """Cria esqueletos para processos dos diagnósticos sem POP (pop_existente vazio e código sem arquivo)."""
    import glob as _glob
    existentes = {p['codigo']: p for p in cl.iter_pops()}
    criados = []
    for f in sorted(_glob.glob(os.path.join(cl.DIAG_DIR, '*.json'))):
        diag = cl.load_json(f)
        node = org.by_codigo.get(diag.get('setor_codigo'))
        if not node or not node.get('gera_pop', True):
            continue
        for proc in diag.get('processos') or []:
            codigo = (proc.get('codigo_sugerido') or '').strip().upper()
            if not codigo or proc.get('pop_existente') or codigo in existentes or proc.get('recomendacao') == 'descartar':
                continue
            if cl.sigla_of_code(codigo) != node['sigla'] or not re.match(r'^[A-Z0-9-]+-\d{2}$', codigo):
                continue
            fontes = [e for e in data['entries'] if e.get('id') in set(proc.get('evidencias') or [])]
            heranca = {'gatilho': proc.get('gatilho', ''), 'origem': '', 'saida': [proc['saida']] if proc.get('saida') else [], 'entrada': [],
                       'artefatos': proc.get('artefatos') or [], 'interfaces': proc.get('interfaces') or [], 'lacunas': proc.get('lacunas') or [],
                       'diag_id': diag.get('id', ''), 'recomendacao': proc.get('recomendacao', '')}
            pop = make_pop(org, node, codigo, proc.get('nome') or codigo, proc.get('descricao') or '', fontes, [], '', [], proc.get('nome') or '', '', heranca)
            if proc.get('tipo_subdominio') in ('core', 'suporte', 'generico'):
                pop['ddd']['tipo_subdominio'] = proc['tipo_subdominio']
            existentes[codigo] = pop
            criados.append(codigo)
            if not dry_run:
                cl.save_json(cl.pop_paths(codigo)[0], pop)
                rp.render_pop(pop, org)
    return criados


def candidatos(org, node, entries, existentes):
    """Lista (codigo, titulo, descricao, fontes, passos, normativa, atencoes, subdominio, escopo)."""
    out = []
    own = org.entries_for(entries, node, include_children=False)
    filhos_rx = [c['filtro_regex'] for c in org.children(node['codigo']) if c.get('filtro_regex')]
    if filhos_rx:  # pai de frentes: não reivindica o que uma frente já filtra
        own = [e for e in own if not any(re.search(rx, cl.text_of_entry(e), re.I) for rx in filhos_rx)]
    usados = set()
    for p in existentes.values():
        usados.update(p.get('fontes_entradas') or [])
    pb = [e for e in own if str(e.get('id', '')).startswith('pb-')]
    if pb:
        e = pb[0]
        p = e.get('p') or {}
        out.append((node['sigla'] + '-00', 'Visão geral — %s' % node['nome'], p.get('resumo') or e.get('desc', ''), [e], p.get('procedimento') or [],
                    p.get('normativa', ''), p.get('atencoes') or [], 'Visão geral do setor (playbook)', ''))
    conhecidos = node.get('processos_conhecidos') or []
    for k in conhecidos:
        fontes = [e for e in own if cl.norm(k['nome']) in cl.norm((e.get('p') or {}).get('titulo', '')) and not str(e['id']).startswith('pb-')]
        desc = '%s%s. Processo codificado no manual institucional da ATDG (jun/2026); conteúdo operacional a documentar.' % (k['nome'], (' — %s' % k['escopo']) if k.get('escopo') else '')
        out.append((k['codigo'], k['nome'], desc, fontes, [], '', [], k['nome'], k.get('escopo', '')))
    codigos = set(existentes.keys()) | set(c[0] for c in out)
    # candidatos: entradas de processo com ≥ 3 passos; versões/cópias do mesmo documento são agrupadas (lição L-005)
    grupos = {}
    for e in own:
        p = e.get('p') or {}
        titulo = p.get('titulo', '')
        if e.get('tipo') != 'processo' or str(e.get('id', '')).startswith('pb-') or e['id'] in usados:
            continue
        if p.get('class') in EXCLUIR_CLASSES or EXCLUIR_TITULO.search(titulo) or DUPLICATA.search(titulo):
            continue
        if len(p.get('procedimento') or []) < 3:
            continue
        if any(cl.norm(k['nome']) in cl.norm(titulo) for k in conhecidos):
            continue
        chave = cl.norm(VERSAO_RX.sub(' ', titulo))
        grupos.setdefault(chave, []).append(e)
    for chave, es in grupos.items():
        def versao_de(e):
            m = re.search(r'v(\d+(?:\.\d+)*)', (e.get('p') or {}).get('titulo', ''), re.I)
            return cl.version_tuple(m.group(1)) if m else (0, 0, 0)
        es = sorted(es, key=lambda e: (versao_de(e), e.get('ts', '')))
        e = es[-1]
        p = e.get('p') or {}
        n = cl.next_process_number(node['sigla'], codigos)
        codigo = '%s-%02d' % (node['sigla'], n)
        codigos.add(codigo)
        out.append((codigo, VERSAO_RX.sub(' ', p.get('titulo') or e.get('desc', '')[:60]).strip(), p.get('resumo') or e.get('desc', ''), es, p.get('procedimento') or [],
                    p.get('normativa', ''), p.get('atencoes') or [], p.get('titulo', ''), ''))
    return out


def scaffold(org, data, setores=None, dry_run=False):
    entries = data['entries']
    nodes = [n for n in org.setores if n.get('gera_pop', True)]
    if setores:
        sel = []
        for s in setores:
            n = org.find(s)
            if not n:
                raise SystemExit('Setor não encontrado: %s' % s)
            sel.append(n)
            sel.extend(org.descendants(n['codigo']))
        nodes = [n for n in nodes if n['codigo'] in set(x['codigo'] for x in sel)]
    existentes = {p['codigo']: p for p in cl.iter_pops()}
    criados, pulados = [], []
    for node in nodes:
        for (codigo, titulo, desc, fontes, passos, normativa, atencoes, subd, escopo) in candidatos(org, node, entries, existentes):
            pj = cl.pop_paths(codigo)[0]
            if codigo in existentes or os.path.exists(pj):
                pulados.append(codigo)
                continue
            pop = make_pop(org, node, codigo, titulo, desc, fontes, passos, normativa, atencoes, subd, escopo)
            existentes[codigo] = pop
            criados.append(codigo)
            if not dry_run:
                cl.save_json(pj, pop)
                rp.render_pop(pop, org)
    return criados, pulados


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--setor', action='append', default=[])
    ap.add_argument('--todos', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--de-diagnosticos', action='store_true', help='cria esqueletos para processos identificados nos diagnósticos sem POP')
    a = ap.parse_args()
    if not a.setor and not a.todos and not a.de_diagnosticos:
        ap.error('informe --setor X, --todos ou --de-diagnosticos')
    org = cl.Org()
    data = cl.load_data()
    if a.de_diagnosticos:
        criados = de_diagnosticos(org, data, a.dry_run)
        print('%s%d esqueleto(s) criados a partir dos diagnósticos: %s' % ('[dry-run] ' if a.dry_run else '', len(criados), ', '.join(criados) or '—'))
        if not a.setor and not a.todos:
            return
    criados, pulados = scaffold(org, data, a.setor or None, a.dry_run)
    print('%s%d POP(s) criados, %d já existentes' % ('[dry-run] ' if a.dry_run else '', len(criados), len(pulados)))
    for c in criados:
        print('  +', c)


if __name__ == '__main__':
    main()
