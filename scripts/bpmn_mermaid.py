#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bpmn_mermaid — converte bpmn_spec (padrão Anne Bail) em Mermaid e gera o organograma Mermaid do POP.

Uso: python3 scripts/bpmn_mermaid.py <codigo|arquivo.pop.json> [--org]
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canvas_lib as cl  # noqa: E402

NODE_FMT = {
    'inicio': '{id}(("{label}"))',
    'atividade': '{id}["{label}"]',
    'decisao': '{id}{{"{label}"}}',
    'fim': '{id}((("{label}")))',
    'pausa': '{id}(["⏱ {label}"])',
    'captura': '{id}[["✉ {label}"]]',
}
CLASSDEFS = [
    'classDef inicio fill:#f3f4f6,stroke:#6b7280,stroke-width:1.5px,color:#374151',
    'classDef atividade fill:#E6F7F0,stroke:#0B7A4E,stroke-width:2px,color:#0B7A4E',
    'classDef decisao fill:#FFF4ED,stroke:#C9783A,stroke-width:2px,color:#C9783A',
    'classDef fim fill:#FDEAEE,stroke:#CC1544,stroke-width:4px,color:#CC1544',
    'classDef pausa fill:#FDEAEE,stroke:#CC1544,stroke-width:2px,color:#CC1544',
    'classDef captura fill:#E0F2F8,stroke:#0B4D66,stroke-width:2px,color:#0B4D66',
]


def esc(label, maxlen=70):
    s = re.sub(r'\s+', ' ', str(label or '')).strip().replace('"', "'")
    if len(s) > maxlen:
        s = s[:maxlen - 1].rstrip() + '…'
    return s or '—'


def safe_id(s):
    return re.sub(r'[^A-Za-z0-9_]', '_', str(s))


def spec_to_mermaid(spec, direction='LR'):
    elementos = list((spec or {}).get('elementos') or [])
    conexoes = list((spec or {}).get('conexoes') or [])
    raias = list((spec or {}).get('raias') or [])
    for el in elementos:
        if el.get('raia') and el['raia'] not in raias:
            raias.append(el['raia'])
    raias = [r for r in raias if any(el.get('raia') == r for el in elementos)]
    lines = ['flowchart ' + direction]
    ids_ok = set()
    for i, raia in enumerate(raias, 1):
        lines.append('  subgraph R%d["%s"]' % (i, esc(raia, 50)))
        lines.append('    direction ' + direction)
        for el in elementos:
            if el.get('raia') == raia:
                fmt = NODE_FMT.get(el.get('tipo'), NODE_FMT['atividade'])
                lines.append('    ' + fmt.format(id=safe_id(el['id']), label=esc(el.get('label'))))
                ids_ok.add(el['id'])
        lines.append('  end')
    for el in elementos:  # sem raia
        if el['id'] not in ids_ok:
            fmt = NODE_FMT.get(el.get('tipo'), NODE_FMT['atividade'])
            lines.append('  ' + fmt.format(id=safe_id(el['id']), label=esc(el.get('label'))))
            ids_ok.add(el['id'])
    for c in conexoes:
        if c.get('de') in ids_ok and c.get('para') in ids_ok:
            if c.get('label'):
                lines.append('  %s -- %s --> %s' % (safe_id(c['de']), esc(c['label'], 30), safe_id(c['para'])))
            else:
                lines.append('  %s --> %s' % (safe_id(c['de']), safe_id(c['para'])))
    lines.extend('  ' + c for c in CLASSDEFS)
    by_tipo = {}
    for el in elementos:
        by_tipo.setdefault(el.get('tipo', 'atividade'), []).append(safe_id(el['id']))
    for tipo, ids in by_tipo.items():
        if tipo in NODE_FMT:
            lines.append('  class %s %s' % (','.join(ids), tipo))
    return '\n'.join(lines)


def org_to_mermaid(chain, processo_codigo, processo_titulo, vizinhos=()):
    lines = ['graph TD']
    prev = None
    for node in chain:
        nid = safe_id(node['codigo'])
        lines.append('  %s["%s<br/>%s"]' % (nid, node['codigo'], esc(node['nome'], 60)))
        if prev:
            lines.append('  %s --> %s' % (prev, nid))
        prev = nid
    lines.append('  P["%s<br/>%s"]' % (esc(processo_codigo, 20), esc(processo_titulo, 60)))
    if prev:
        lines.append('  %s --> P' % prev)
    for i, v in enumerate(vizinhos or [], 1):
        vid = 'V%d' % i
        lines.append('  %s["%s"]' % (vid, esc(v, 50)))
        lines.append('  P -. interface .-> %s' % vid)
    lines.append('  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747')
    lines.append('  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747')
    lines.append('  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66')
    if chain:
        lines.append('  class %s setor' % ','.join(safe_id(n['codigo']) for n in chain))
    lines.append('  class P destaque')
    if vizinhos:
        lines.append('  class %s vizinho' % ','.join('V%d' % i for i in range(1, len(vizinhos) + 1)))
    return '\n'.join(lines)


def spec_from_pop(pop, max_atividades=10):
    """Especificação BPMN determinística a partir dos passos e do mapa de contexto (usada por scaffold/patch)."""
    passos = (pop.get('playbook') or {}).get('passos') or []
    raia_principal = (pop.get('identificacao') or {}).get('responsavel') or pop.get('setor') or 'Setor'
    if not raia_principal or raia_principal == 'A definir':
        raia_principal = pop.get('setor') or 'Setor'
    gat = ((pop.get('playbook') or {}).get('gatilho') or {}).get('evento') or 'Início'
    elementos = [{'id': 'e1', 'tipo': 'inicio', 'label': gat, 'raia': raia_principal}]
    conexoes = []
    n = 1
    prev = 'e1'
    for p in passos[:max_atividades]:
        n += 1
        raia = p.get('responsavel') or raia_principal
        if raia == 'A definir':
            raia = raia_principal
        elementos.append({'id': 'e%d' % n, 'tipo': 'atividade', 'label': p.get('acao', ''), 'raia': raia})
        conexoes.append({'de': prev, 'para': 'e%d' % n})
        prev = 'e%d' % n
    contexto = pop.get('setor')
    for mc in pop.get('mapa_contexto') or []:
        dest = mc.get('destino')
        if dest and dest != contexto and mc.get('relacao') in ('fornece', 'informa', 'valida', 'aprova'):
            n += 1
            elementos.append({'id': 'e%d' % n, 'tipo': 'captura', 'label': '%s %s' % ({'fornece': 'Encaminhar a', 'informa': 'Informar', 'valida': 'Validação por', 'aprova': 'Aprovação por'}[mc['relacao']], dest), 'raia': dest})
            conexoes.append({'de': prev, 'para': 'e%d' % n})
            prev = 'e%d' % n
    saida = (pop.get('playbook') or {}).get('saida') or []
    n += 1
    elementos.append({'id': 'e%d' % n, 'tipo': 'fim', 'label': (saida[0] if saida else 'Concluído'), 'raia': raia_principal})
    conexoes.append({'de': prev, 'para': 'e%d' % n})
    raias = []
    for el in elementos:
        if el['raia'] not in raias:
            raias.append(el['raia'])
    return {'raias': raias, 'elementos': elementos, 'conexoes': conexoes,
            'observacoes_construcao_miro': 'Especificação gerada a partir dos passos do POP; %d raia(s). Revisar decisões e pausas antes de construir no Miro.' % len(raias)}


def refresh_mermaid(pop, org=None):
    """Regenera organograma_mermaid e fluxograma_mermaid do POP (in place)."""
    org = org or cl.Org()
    chain = org.chain(pop['setor_codigo'])
    vizinhos = []
    for mc in pop.get('mapa_contexto') or []:
        for lado in ('origem', 'destino'):
            v = mc.get(lado)
            if v and v != pop.get('setor') and v not in vizinhos:
                vizinhos.append(v)
    pop['organograma_mermaid'] = org_to_mermaid(chain, pop['codigo'], pop['titulo'], vizinhos[:6])
    if not (pop.get('bpmn_spec') or {}).get('elementos'):
        pop['bpmn_spec'] = spec_from_pop(pop)
    pop['fluxograma_mermaid'] = spec_to_mermaid(pop['bpmn_spec'])
    return pop


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__)
        sys.exit(1)
    src = args[0]
    pop = cl.load_json(src) if src.endswith('.json') else cl.load_pop(src)
    if '--org' in sys.argv:
        print(org_to_mermaid(cl.Org().chain(pop['setor_codigo']), pop['codigo'], pop['titulo']))
    else:
        print(spec_to_mermaid(pop.get('bpmn_spec') or spec_from_pop(pop)))
