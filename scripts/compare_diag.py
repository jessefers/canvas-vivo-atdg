#!/usr/bin/env python3
"""Compara um diagnóstico gerado pelo app (JSON) com o diagnóstico de referência do repositório.

Uso: python compare_diag.py <referencia.json> <novo.json>
- <novo.json> pode ser o objeto do diagnóstico ou uma exportação do app (lista em "diagnosticos"/"diags").
Saída: divergências por processo (métricas, recomendação, lacunas), ecossistema, lacunas do setor e lições propostas.
"""
import json
import sys

CAMPOS_NUM = ['prioridade', 'maturidade', 'criticidade', 'frequencia', 'risco_conformidade', 'cobertura']
CAMPOS_TXT = ['nome', 'tipo', 'tipo_subdominio', 'recomendacao', 'pop_existente']
CAMPOS_LST = ['lacunas', 'atores', 'sistemas', 'artefatos', 'interfaces', 'evidencias']


def carregar(p):
    with open(p, encoding='utf-8') as f:
        d = json.load(f)
    if isinstance(d, dict) and 'processos' in d:
        return d
    lista = d.get('diagnosticos') or d.get('diags') or (d if isinstance(d, list) else [])
    alvo = [x for x in lista if str(x.get('sigla', '')).upper() == 'ALM' or str(x.get('setor_codigo', '')).endswith('-ALM')]
    if not alvo:
        sys.exit('nenhum diagnóstico ALM em %s' % p)
    return sorted(alvo, key=lambda x: str(x.get('data', '')))[-1]


def conj(x):
    return set(str(v).strip() for v in (x or []))


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    ref, novo = carregar(sys.argv[1]), carregar(sys.argv[2])
    print('REFERÊNCIA: %s · %s · modelo %s · diretrizes v%s · %d processo(s) · hash %s' % (
        ref.get('id'), str(ref.get('data', ''))[:19], ref.get('modelo'), ref.get('versao_diretrizes'), len(ref.get('processos') or []), str(ref.get('hash_fontes', ''))[:12]))
    print('NOVO      : %s · %s · modelo %s · diretrizes v%s · %d processo(s) · hash %s' % (
        novo.get('id'), str(novo.get('data', ''))[:19], novo.get('modelo'), novo.get('versao_diretrizes'), len(novo.get('processos') or []), str(novo.get('hash_fontes', ''))[:12]))
    if ref.get('hash_fontes') != novo.get('hash_fontes'):
        print('!! hash_fontes diferente (fontes mudaram ou fórmula divergente)')
    pr = {p.get('codigo_sugerido'): p for p in ref.get('processos') or []}
    pn = {p.get('codigo_sugerido'): p for p in novo.get('processos') or []}
    print('\n== Processos ==')
    print('só na referência:', sorted(set(pr) - set(pn)) or '—')
    print('só no novo      :', sorted(set(pn) - set(pr)) or '—')
    for cod in sorted(set(pr) & set(pn)):
        a, b = pr[cod], pn[cod]
        difs = []
        for c in CAMPOS_NUM:
            va, vb = a.get(c), b.get(c)
            if va != vb:
                difs.append('%s %s→%s' % (c, va, vb))
        for c in CAMPOS_TXT:
            if str(a.get(c) or '') != str(b.get(c) or ''):
                difs.append('%s %r→%r' % (c, str(a.get(c) or '')[:60], str(b.get(c) or '')[:60]))
        for c in CAMPOS_LST:
            sa, sb = conj(a.get(c)), conj(b.get(c))
            if sa != sb:
                difs.append('%s -%s +%s' % (c, sorted(sa - sb) or '', sorted(sb - sa) or ''))
        if a.get('auditoria_externa') != b.get('auditoria_externa'):
            difs.append('auditoria_externa %s→%s' % (a.get('auditoria_externa'), b.get('auditoria_externa')))
        print('\n%s — %s' % (cod, a.get('nome')))
        for d in difs or ['(sem divergência)']:
            print('   ', d)
    print('\n== Ecossistema ==')
    ea, eb = ref.get('ecossistema') or {}, novo.get('ecossistema') or {}
    for c in ['dominio']:
        if ea.get(c) != eb.get(c):
            print('%s: %r → %r' % (c, ea.get(c), eb.get(c)))
    for c in ['subdominios', 'contextos_vizinhos', 'sistemas', 'normas', 'benchmarks']:
        sa, sb = conj(ea.get(c)), conj(eb.get(c))
        if sa != sb:
            print('%s:\n   -%s\n   +%s' % (c, sorted(sa - sb), sorted(sb - sa)))
    print('\n== Lacunas do setor ==')
    la, lb = conj(ref.get('lacunas_setor')), conj(novo.get('lacunas_setor'))
    print('   -', sorted(la - lb)); print('   +', sorted(lb - la))
    print('\n== Lições propostas pelo novo diagnóstico ==')
    for l in novo.get('licoes_propostas') or []:
        print(' - LIÇÃO:', (l.get('licao') or '')[:220]); print('   REGRA:', (l.get('regra') or '')[:220])
    print('\n== Observações do novo ==\n', (novo.get('observacoes') or '')[:800])


if __name__ == '__main__':
    main()
