#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""apply_patch — aplica um patch incremental (schemas/patch.schema.json) a um POP canônico, com bump de versão,
changelog, fontes/hash, renumeração de passos, regeneração dos diagramas e re-render (.md/.bpmn.json).

Uso: python3 scripts/apply_patch.py <codigo> <patch.json> [--dry-run]
Regra de versão (diretriz 06): major = passo removido, raia alterada, responsável do processo alterado, reestruturação;
minor = passo adicionado/alterado, artefato, decisão, KPI, interface, elemento BPMN; patch = texto, glossário, normativa,
contingência, checklist, pontos de atenção. `tipo_mudanca` do patch só pode escalar o tipo calculado.
"""
import copy
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canvas_lib as cl  # noqa: E402
import bpmn_mermaid as bm  # noqa: E402
import render_pop as rp  # noqa: E402

LISTAS = [  # (chave do patch, caminho no POP, tipo de mudança)
    ('entrada_nova', ('playbook', 'entrada'), 'minor'), ('saida_nova', ('playbook', 'saida'), 'minor'),
    ('artefatos_novos', ('artefatos',), 'minor'), ('decisoes_novas', ('decisoes',), 'minor'),
    ('kpis_novos', ('kpis',), 'minor'), ('mapa_contexto_novo', ('mapa_contexto',), 'minor'),
    ('pontos_atencao_novos', ('pontos_atencao',), 'patch'), ('contingencia_nova', ('contingencia',), 'patch'),
    ('checklist_novo', ('checklist',), 'patch'), ('glossario_novo', ('ddd', 'glossario'), 'patch'),
    ('normativa_nova', ('identificacao', 'normativa'), 'patch'),
]


def _get(d, path):
    for k in path:
        d = d.setdefault(k, {} if k != path[-1] else [])
    return d


def _set_dotted(pop, key, value):
    parts = key.split('.')
    d = pop
    for k in parts[:-1]:
        d = d.setdefault(k, {})
    d[parts[-1]] = value


def aplicar(pop, patch, org=None, data=None):
    org = org or cl.Org()
    pop = copy.deepcopy(pop)
    errs = cl.validate_schema(patch, cl.load_schema('patch.schema.json'))
    if errs:
        raise SystemExit('Patch inválido:\n  ' + '\n  '.join(errs))
    if patch.get('codigo') and patch['codigo'] != pop['codigo']:
        raise SystemExit('Patch para %s aplicado em %s' % (patch['codigo'], pop['codigo']))
    tipo = 'patch'
    mudancas = []
    pb = pop.setdefault('playbook', {})
    passos = pb.setdefault('passos', [])

    # remoções
    rem = set(patch.get('passos_removidos') or [])
    if rem:
        antes = len(passos)
        passos[:] = [p for p in passos if p.get('n') not in rem]
        mudancas.append('Passos removidos: %s' % ', '.join(str(n) for n in sorted(rem)))
        if len(passos) < antes:
            tipo = cl.max_tipo(tipo, 'major')
    # alterações
    for alt in patch.get('passos_alterados') or []:
        for p in passos:
            if p.get('n') == alt['n']:
                p.update({k: v for k, v in (alt.get('campos') or {}).items()})
                mudancas.append('Passo %d alterado (%s)' % (alt['n'], ', '.join(alt.get('campos') or {})))
                tipo = cl.max_tipo(tipo, 'minor')
    # adições — semântica: "após o passo n da numeração ORIGINAL"; várias adições com o mesmo apos_n
    # (ou em playbook vazio) preservam a ordem em que foram listadas no patch
    adds = patch.get('passos_adicionados') or []
    if adds:
        def novo_passo(a):
            novo = dict(a['passo'])
            novo.setdefault('sistema', '')
            novo.setdefault('artefato', '')
            novo.setdefault('prazo', 'A definir')
            novo.setdefault('evento', '')
            novo.setdefault('fontes', list(patch.get('fontes') or []))
            return novo
        por_pos = {}
        for a in adds:
            pos = a.get('apos_n')
            pos = float('inf') if pos is None else int(pos)
            por_pos.setdefault(pos, []).append(a)
        orig = list(passos)
        ns_orig = set(p.get('n') for p in orig)
        novos = [novo_passo(a) for a in por_pos.get(0, [])]
        for p in orig:
            novos.append(p)
            novos.extend(novo_passo(a) for a in por_pos.get(p.get('n'), []))
        for pos in sorted(k for k in por_pos if k != 0 and k not in ns_orig):
            novos.extend(novo_passo(a) for a in por_pos[pos])
        passos[:] = novos
        for a in adds:
            mudancas.append('Passo adicionado após %s: %s' % ('fim' if a.get('apos_n') is None else a.get('apos_n'), str(a['passo'].get('acao', ''))[:80]))
        tipo = cl.max_tipo(tipo, 'minor')
    for i, p in enumerate(passos, 1):
        p['n'] = i
    # listas
    for chave, caminho, t in LISTAS:
        itens = patch.get(chave) or []
        if not itens:
            continue
        alvo = _get(pop, caminho)
        for it in itens:
            if it not in alvo:
                alvo.append(it)
        mudancas.append('%s: +%d' % (chave, len(itens)))
        tipo = cl.max_tipo(tipo, t)
    # campos escalares
    for k, v in (patch.get('campos') or {}).items():
        antigo = pop
        for part in k.split('.'):
            antigo = antigo.get(part) if isinstance(antigo, dict) else None
        if k == 'identificacao.responsavel' and antigo and antigo != 'A definir' and antigo != v:
            tipo = cl.max_tipo(tipo, 'major')
        elif k in ('titulo', 'setor_codigo'):
            tipo = cl.max_tipo(tipo, 'major')
        elif k == 'status':
            pass
        else:
            tipo = cl.max_tipo(tipo, 'patch')
        _set_dotted(pop, k, v)
        mudancas.append('Campo %s atualizado' % k)
    # BPMN
    delta = patch.get('bpmn_delta') or {}
    spec = pop.setdefault('bpmn_spec', {'raias': [], 'elementos': [], 'conexoes': [], 'observacoes_construcao_miro': ''})
    if delta.get('regenerar_de_passos') or not spec.get('elementos'):
        pop['bpmn_spec'] = bm.spec_from_pop(pop)
        spec = pop['bpmn_spec']
        if delta.get('regenerar_de_passos'):
            mudancas.append('Fluxograma regenerado a partir dos passos')
    if delta.get('raias_add'):
        for r in delta['raias_add']:
            if r not in spec['raias']:
                spec['raias'].append(r)
        tipo = cl.max_tipo(tipo, 'major')
        mudancas.append('Raias adicionadas: %s' % ', '.join(delta['raias_add']))
    if delta.get('elementos_rm'):
        rm = set(delta['elementos_rm'])
        spec['elementos'] = [e for e in spec['elementos'] if e['id'] not in rm]
        spec['conexoes'] = [c for c in spec['conexoes'] if c['de'] not in rm and c['para'] not in rm]
        tipo = cl.max_tipo(tipo, 'minor')
        mudancas.append('Elementos BPMN removidos: %s' % ', '.join(sorted(rm)))
    if delta.get('elementos_add'):
        ids = set(e['id'] for e in spec['elementos'])
        for e in delta['elementos_add']:
            if e['id'] not in ids:
                spec['elementos'].append(e)
                ids.add(e['id'])
                if e.get('raia') and e['raia'] not in spec['raias']:
                    spec['raias'].append(e['raia'])
        tipo = cl.max_tipo(tipo, 'minor')
        mudancas.append('Elementos BPMN adicionados: %d' % len(delta['elementos_add']))
    if delta.get('conexoes_rm'):
        rmc = set((c['de'], c['para']) for c in delta['conexoes_rm'])
        spec['conexoes'] = [c for c in spec['conexoes'] if (c['de'], c['para']) not in rmc]
    if delta.get('conexoes_add'):
        for c in delta['conexoes_add']:
            if c not in spec['conexoes']:
                spec['conexoes'].append(c)
        tipo = cl.max_tipo(tipo, 'minor')
    # lacunas e lições
    if patch.get('lacunas_resolvidas'):
        pop['lacunas'] = [l for l in pop.get('lacunas') or [] if l not in set(patch['lacunas_resolvidas'])]
    for l in patch.get('lacunas_novas') or []:
        if l not in pop.setdefault('lacunas', []):
            pop['lacunas'].append(l)
    for l in patch.get('licoes_aplicadas') or []:
        if l not in pop.setdefault('licoes_aplicadas', []):
            pop['licoes_aplicadas'].append(l)
    # tipo final, versão, status
    tipo = cl.max_tipo(tipo, patch.get('tipo_mudanca', 'patch'))
    pop['versao'] = cl.bump_version(pop['versao'], tipo)
    resp = (pop.get('identificacao') or {}).get('responsavel', 'A definir')
    if pop['status'] == 'aprovado':
        pop['status'] = 'em_validacao'
        mudancas.append('Status devolvido a em_validacao (POP aprovado alterado)')
    elif pop['status'] == 'rascunho' and len(passos) >= 3 and resp and resp != 'A definir':
        pop['status'] = 'em_validacao'
        mudancas.append('Status promovido a em_validacao (≥ 3 passos e responsável definido)')
    if 'passos' in (pop.get('lacunas') or []) and len(passos) >= 3:
        pop['lacunas'].remove('passos')
    if 'responsavel' in (pop.get('lacunas') or []) and resp and resp != 'A definir':
        pop['lacunas'].remove('responsavel')
    # fontes
    fontes = list(pop.get('fontes_entradas') or [])
    for f in patch.get('fontes') or []:
        if f not in fontes:
            fontes.append(f)
    pop['fontes_entradas'] = fontes
    data = data or cl.load_data()
    ents = [e for e in data['entries'] if e.get('id') in set(fontes)]
    pop['hash_fontes'] = cl.hash_fontes(ents) if ents else cl.hash_fontes(fontes)
    now = cl.now_iso()
    pop['atualizado_em'] = now
    pop['versao_diretrizes'] = cl.diretrizes_versao()
    pop.setdefault('changelog', []).append({'versao': pop['versao'], 'data': now[:10], 'autor': patch.get('autor', 'agente'), 'tipo': tipo,
                                            'mudancas': mudancas or ['Sem alterações estruturais'], 'fontes': list(patch.get('fontes') or []), 'motivo': patch.get('motivo', '')})
    bm.refresh_mermaid(pop, org)
    return pop, tipo, mudancas


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    codigo, patch_file = args[0], args[1]
    dry = '--dry-run' in sys.argv
    pop = cl.load_pop(codigo)
    patch = cl.load_json(patch_file)
    novo, tipo, mudancas = aplicar(pop, patch)
    licoes = patch.get('licoes_propostas') or []
    if not dry:
        cl.save_json(cl.pop_paths(novo)[0], novo)
        rp.render_pop(novo)
        if licoes:
            registrar_licoes(licoes, 'pop:' + codigo)
    print('%s%s: %s → %s (%s)' % ('[dry-run] ' if dry else '', codigo, pop['versao'], novo['versao'], tipo))
    for m in mudancas:
        print('  -', m)
    if licoes:
        print('  lições propostas: %d%s' % (len(licoes), ' (não registradas em dry-run)' if dry else ' registradas em diretrizes/07-licoes-aprendidas.md'))


def registrar_licoes(licoes, origem):
    """Acrescenta lições propostas à tabela 'Propostas pendentes' de 07-licoes-aprendidas.md."""
    import io
    f = os.path.join(cl.DIR_DIR, '07-licoes-aprendidas.md')
    txt = io.open(f, encoding='utf-8').read()
    marcador = '## Propostas pendentes\n\n| id | data | origem | lição | regra proposta | status |\n|---|---|---|---|---|---|\n'
    if marcador not in txt:
        raise SystemExit('Tabela de propostas pendentes não encontrada em 07-licoes-aprendidas.md')
    linhas = ''
    for l in licoes:
        lid = cl.next_licao_id()
        linhas += '| %s | %s | %s | %s | %s | proposta |\n' % (lid, cl.today(), (l.get('origem') or origem).replace('|', '/'), (l.get('licao') or '').replace('|', '/').replace('\n', ' '), (l.get('regra') or '').replace('|', '/').replace('\n', ' '))
        txt = txt.replace(marcador, marcador + linhas)
        linhas = ''
        io.open(f, 'w', encoding='utf-8', newline='\n').write(txt)
        txt = io.open(f, encoding='utf-8').read()
    return True


if __name__ == '__main__':
    main()
