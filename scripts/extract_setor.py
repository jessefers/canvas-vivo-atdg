#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extract_setor — extrai, em JSON compacto, as entradas do Canvas de um setor (e subdivisões) para alimentar diagnósticos e patches.

Uso: python3 scripts/extract_setor.py --setor <codigo|sigla|rótulo> [--desde ISO] [--exclui id1,id2] [--max 40] [--chars 400] [--sem-filhos] [--saida arquivo.json]
Saída: {"setor","setor_codigo","sigla","total","hash_fontes","entradas":[...]}
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canvas_lib as cl  # noqa: E402


def extrair(setor, desde='', exclui=(), maximo=40, chars=400, filhos=True, org=None, data=None):
    org = org or cl.Org()
    data = data or cl.load_data()
    node = org.find(setor)
    if not node:
        raise SystemExit('Setor não encontrado: %s' % setor)
    ents = org.entries_for(data['entries'], node, include_children=filhos)
    excl = set(x for x in exclui if x)
    sel = [e for e in ents if e.get('id') not in excl and (not desde or str(e.get('ts', '')) > desde)]
    sel = sel[-maximo:] if maximo and len(sel) > maximo else sel
    return {'setor': node['id_app'], 'setor_codigo': node['codigo'], 'sigla': node['sigla'], 'dominio': node['dominio'],
            'total': len(ents), 'selecionadas': len(sel), 'hash_fontes': cl.hash_fontes(ents), 'desde': desde or None,
            'entradas': [cl.summarize_entry(e, chars) for e in sel]}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--setor', required=True)
    ap.add_argument('--desde', default='')
    ap.add_argument('--exclui', default='')
    ap.add_argument('--max', type=int, default=40)
    ap.add_argument('--chars', type=int, default=400)
    ap.add_argument('--sem-filhos', action='store_true')
    ap.add_argument('--saida', default='')
    a = ap.parse_args()
    out = extrair(a.setor, a.desde, [x.strip() for x in a.exclui.split(',')], a.max, a.chars, not a.sem_filhos)
    if a.saida:
        cl.save_json(a.saida, out)
        print('gravado em %s (%d entradas)' % (a.saida, out['selecionadas']))
    else:
        print(cl.dumps(out))


if __name__ == '__main__':
    main()
