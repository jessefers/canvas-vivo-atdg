#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync_data — sincroniza pops/, diagnosticos/, diretrizes/ e agentes/registry.json com data.json (e vice-versa a partir de exportações do app).

Uso:
  python3 scripts/sync_data.py --to-data                 # repositório → data.json (merge por id: atualiza+adiciona; entries intactas)
  python3 scripts/sync_data.py --from-export arquivo.json # exportação do app → data.json + arquivos do repositório
  python3 scripts/sync_data.py --check                    # relata divergências sem gravar (sai com 1 se houver)
"""
import glob
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canvas_lib as cl  # noqa: E402
import render_pop as rp  # noqa: E402

VERSAO_DATA = 'Canvas Vivo ATDG v5'


def diretrizes_registros():
    regs = []
    for f in cl.diretrizes_files():
        txt = io.open(f, encoding='utf-8').read()
        fm = cl.read_front_matter(txt)
        nome = os.path.basename(f)
        regs.append({'id': fm.get('id') or 'diretriz-' + nome[:2], 'arquivo': 'diretrizes/' + nome, 'titulo': fm.get('titulo', nome),
                     'versao': fm.get('versao', '1.0'), 'atualizado_em': fm.get('atualizado_em', ''), 'conteudo': txt})
    return regs


def licoes_registros():
    f = os.path.join(cl.DIR_DIR, '07-licoes-aprendidas.md')
    if not os.path.exists(f):
        return []
    out = []
    for l in cl.parse_licoes(io.open(f, encoding='utf-8').read()):
        l = dict(l)
        l['atualizado_em'] = l.get('data', '')
        out.append(l)
    return out


def diagnosticos_arquivos():
    return [cl.load_json(f) for f in sorted(glob.glob(os.path.join(cl.DIAG_DIR, '*.json')))]


def merge_por_id(destino, origem, substituir_mais_novo=True):
    idx = {x.get('id'): i for i, x in enumerate(destino)}
    add = upd = 0
    for x in origem:
        if not x or x.get('id') is None:
            continue
        if x['id'] in idx:
            cur = destino[idx[x['id']]]
            if substituir_mais_novo and mais_novo(cur, x):
                destino[idx[x['id']]] = x
                upd += 1
        else:
            destino.append(x)
            idx[x['id']] = len(destino) - 1
            add += 1
    return add, upd


def mais_novo(cur, inc):
    if cur.get('versao') is not None and inc.get('versao') is not None and str(cur['versao']) != str(inc['versao']):
        return cl.cmp_version(inc['versao'], cur['versao']) > 0
    return str(inc.get('atualizado_em') or inc.get('ts') or '') >= str(cur.get('atualizado_em') or cur.get('ts') or '')


def to_data():
    data = cl.load_data()
    antes = cl.entries_hash(data['entries'])
    res = {}
    res['pops'] = merge_por_id(data.setdefault('pops', []), cl.iter_pops())
    res['diagnosticos'] = merge_por_id(data.setdefault('diagnosticos', []), diagnosticos_arquivos())
    res['agentes'] = merge_por_id(data.setdefault('agentes', []), cl.load_json(cl.AG_REG, []))
    data['diretrizes'] = diretrizes_registros()
    data['licoes'] = licoes_registros()
    data['versao'] = VERSAO_DATA
    data['sincronizado_em'] = cl.now_iso()
    assert cl.entries_hash(data['entries']) == antes, 'entries alteradas — abortado'
    cl.save_data(data)
    for k, (a, u) in res.items():
        print('%s: +%d adicionados, %d atualizados' % (k, a, u))
    print('diretrizes: %d · lições: %d · data.json gravado (%s)' % (len(data['diretrizes']), len(data['licoes']), VERSAO_DATA))


def from_export(arquivo):
    exp = cl.load_json(arquivo)
    data = cl.load_data()
    src = {'entries': exp} if isinstance(exp, list) else exp
    ids = set(e.get('id') for e in data['entries'])
    novas = [e for e in src.get('entries') or [] if e.get('id') not in ids]
    data['entries'].extend(novas)
    print('entries: +%d' % len(novas))
    org = cl.Org()
    a, u = merge_por_id(data.setdefault('pops', []), src.get('pops') or [])
    gravados = 0
    for p in src.get('pops') or []:  # POPs do app viram arquivos canônicos quando mais novos
        pj = cl.pop_paths(p['codigo'])[0]
        atual = cl.load_json(pj) if os.path.exists(pj) else None
        if atual is None or mais_novo(atual, p):
            cl.save_json(pj, p)
            rp.render_pop(p, org)
            gravados += 1
    print('pops: +%d adicionados, %d atualizados, %d arquivos gravados' % (a, u, gravados))
    a, u = merge_por_id(data.setdefault('diagnosticos', []), src.get('diagnosticos') or [])
    for d in src.get('diagnosticos') or []:
        f = os.path.join(cl.DIAG_DIR, '%s.json' % d.get('sigla', d['id']))
        atual = cl.load_json(f) if os.path.exists(f) else None
        if atual is None or mais_novo(atual, d):
            cl.save_json(f, d)
    print('diagnosticos: +%d adicionados, %d atualizados' % (a, u))
    a, u = merge_por_id(data.setdefault('agentes', []), src.get('agentes') or [])
    reg = cl.load_json(cl.AG_REG, [])
    merge_por_id(reg, src.get('agentes') or [])
    cl.save_json(cl.AG_REG, reg)
    print('agentes: +%d adicionados, %d atualizados' % (a, u))
    novas_licoes = [l for l in src.get('licoes') or [] if l.get('id') and l['id'] not in set(x['id'] for x in licoes_registros())]
    if novas_licoes:
        import apply_patch as ap
        ap.registrar_licoes([{'licao': l.get('licao', ''), 'regra': l.get('regra', ''), 'origem': l.get('origem', 'app')} for l in novas_licoes], 'app')
    data['licoes'] = licoes_registros()
    data['diretrizes'] = diretrizes_registros()
    data['versao'] = VERSAO_DATA
    data['sincronizado_em'] = cl.now_iso()
    cl.save_data(data)
    print('lições novas: %d · data.json gravado' % len(novas_licoes))


def check():
    data = cl.load_data()
    div = []
    repo = {p['id']: p for p in cl.iter_pops()}
    dat = {p['id']: p for p in data.get('pops') or []}
    for i, p in repo.items():
        if i not in dat:
            div.append('POP ausente em data.json: %s' % p['codigo'])
        elif str(dat[i].get('versao')) != str(p.get('versao')):
            div.append('POP %s: repo %s ≠ data %s' % (p['codigo'], p.get('versao'), dat[i].get('versao')))
    for i in dat:
        if i not in repo:
            div.append('POP só em data.json (exportação do app não aplicada): %s' % dat[i].get('codigo'))
    if data.get('versao') != VERSAO_DATA:
        div.append('data.json versao = %r (esperado %r)' % (data.get('versao'), VERSAO_DATA))
    dv = {d['id']: d.get('versao') for d in data.get('diretrizes') or []}
    for r in diretrizes_registros():
        if dv.get(r['id']) != r['versao']:
            div.append('diretriz %s: repo %s ≠ data %s' % (r['id'], r['versao'], dv.get(r['id'])))
    if len(data.get('licoes') or []) != len(licoes_registros()):
        div.append('lições: repo %d ≠ data %d' % (len(licoes_registros()), len(data.get('licoes') or [])))
    for d in div:
        print('DIVERGÊNCIA:', d)
    print('%d divergência(s)' % len(div))
    return 1 if div else 0


if __name__ == '__main__':
    if '--to-data' in sys.argv:
        to_data()
    elif '--from-export' in sys.argv:
        from_export(sys.argv[sys.argv.index('--from-export') + 1])
    elif '--check' in sys.argv:
        sys.exit(check())
    else:
        print(__doc__)
        sys.exit(1)
