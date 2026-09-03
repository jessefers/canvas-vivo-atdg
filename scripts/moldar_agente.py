#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""moldar_agente — instancia o agente moldado por processo (.claude/agents/pop-<codigo>.md) a partir do template
diretrizes/08-template-agente-processo.md e do POP canônico; registra em agentes/registry.json.

Uso: python3 scripts/moldar_agente.py <codigo|SIGLA|--todos> [--forcar] [--modelo sonnet]
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canvas_lib as cl  # noqa: E402

TEMPLATE = os.path.join(cl.DIR_DIR, '08-template-agente-processo.md')


def template_text():
    txt = io.open(TEMPLATE, encoding='utf-8').read()
    m = re.search(r'<!-- TEMPLATE:INICIO -->\n(.*?)<!-- TEMPLATE:FIM -->', txt, re.S)
    if not m:
        raise SystemExit('Marcadores TEMPLATE:INICIO/FIM não encontrados em %s' % TEMPLATE)
    return m.group(1)


def valores(pop, org):
    node = org.by_codigo.get(pop['setor_codigo']) or {}
    pj, pm, pb = cl.pop_paths(pop)
    rel = lambda p: os.path.relpath(p, cl.ROOT)  # noqa: E731
    spec = pop.get('bpmn_spec') or {}
    ifaces = ['%s → %s (%s)' % (m.get('origem'), m.get('destino'), m.get('relacao')) for m in pop.get('mapa_contexto') or []]
    fontes = pop.get('fontes_entradas') or []
    return {
        'codigo': pop['codigo'], 'codigo_lower': pop['codigo'].lower(), 'nome': pop['titulo'], 'setor': pop['setor'], 'setor_codigo': pop['setor_codigo'],
        'sigla': pop['sigla'], 'dominio': (pop.get('ddd') or {}).get('dominio', node.get('dominio', '')), 'contexto': (pop.get('ddd') or {}).get('contexto', pop['setor_codigo']),
        'arquivo_pop': rel(pj), 'arquivo_md': rel(pm), 'arquivo_bpmn': rel(pb), 'versao': pop.get('versao', ''), 'status': pop.get('status', ''),
        'diretrizes_versao': cl.diretrizes_versao(), 'responsavel': (pop.get('identificacao') or {}).get('responsavel', 'A definir'),
        'raias': ', '.join(spec.get('raias') or []) or 'A definir', 'normativa': '; '.join((pop.get('identificacao') or {}).get('normativa') or []) or 'A definir',
        'interfaces': '; '.join(ifaces) or 'nenhuma registrada', 'fontes': ', '.join(fontes) or 'nenhuma', 'fontes_csv': ','.join(fontes) or '-',
        'hash_fontes': (pop.get('hash_fontes') or '')[:12], 'atualizado_em': pop.get('atualizado_em', ''),
    }


def moldar(pop, org, forcar=False, modelo='sonnet', origem='script'):
    txt = template_text()
    vals = valores(pop, org)
    for k, v in vals.items():
        txt = txt.replace('{{%s}}' % k, str(v))
    txt = re.sub(r'^model: .*$', 'model: %s' % modelo, txt, count=1, flags=re.M)
    resto = re.findall(r'\{\{[a-z_]+\}\}', txt)
    if resto:
        raise SystemExit('Placeholders não resolvidos: %s' % sorted(set(resto)))
    dest = os.path.join(cl.AGENTS_DIR, 'pop-%s.md' % vals['codigo_lower'])
    existia = os.path.exists(dest)
    if existia and not forcar:
        return dest, False
    os.makedirs(cl.AGENTS_DIR, exist_ok=True)
    io.open(dest, 'w', encoding='utf-8', newline='\n').write(txt)
    reg = cl.load_json(cl.AG_REG, [])
    now = cl.now_iso()
    aid = 'agente-pop-%s' % vals['codigo_lower']
    item = {'id': aid, 'codigo': pop['codigo'], 'pop_id': pop['id'], 'nome': 'Agente do processo %s — %s' % (pop['codigo'], pop['titulo']), 'setor_codigo': pop['setor_codigo'],
            'arquivo': os.path.relpath(dest, cl.ROOT), 'versao_diretrizes': vals['diretrizes_versao'], 'versao_pop': pop.get('versao', ''), 'modelo': modelo, 'origem': origem,
            'criado_em': now, 'atualizado_em': now}
    for i, r in enumerate(reg):
        if r.get('id') == aid:
            item['criado_em'] = r.get('criado_em', now)
            reg[i] = item
            break
    else:
        reg.append(item)
    cl.save_json(cl.AG_REG, reg)
    if pop.get('agente') != 'pop-%s' % vals['codigo_lower']:
        pop['agente'] = 'pop-%s' % vals['codigo_lower']
        cl.save_json(cl.pop_paths(pop)[0], pop)
        import render_pop as rp
        rp.render_pop(pop, org)
    return dest, True


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(1)
    forcar = '--forcar' in a
    modelo = a[a.index('--modelo') + 1] if '--modelo' in a else 'sonnet'
    org = cl.Org()
    alvo = [x for x in a if not x.startswith('--') and x != modelo]
    if '--todos' in a:
        pops = cl.iter_pops()
    else:
        pops = []
        for x in alvo:
            if re.match(r'^[A-Z0-9-]+-\d{2}$', x.upper()):
                pops.append(cl.load_pop(x.upper()))
            else:
                node = org.find(x)
                if not node:
                    raise SystemExit('Código ou setor não encontrado: %s' % x)
                pops.extend(p for p in cl.iter_pops() if p['sigla'] == node['sigla'])
    feitos = pulados = 0
    for pop in pops:
        dest, ok = moldar(pop, org, forcar, modelo)
        if ok:
            feitos += 1
            print('  +', os.path.relpath(dest, cl.ROOT))
        else:
            pulados += 1
    print('%d agente(s) moldado(s), %d já existentes (use --forcar para regerar)' % (feitos, pulados))


if __name__ == '__main__':
    main()
