#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_diag — renderiza diagnosticos/<SIGLA>.json em Markdown (diagnosticos/<SIGLA>.md) e recalcula prioridades.

Uso: python3 scripts/render_diag.py <SIGLA|arquivo.json> [--todos]
"""
import glob
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canvas_lib as cl  # noqa: E402
from render_pop import cell, tabela, lista  # noqa: E402


def prioridade(p):
    return round(0.30 * float(p.get('criticidade', 0)) + 0.25 * float(p.get('frequencia', 0)) + 0.20 * float(p.get('risco_conformidade', 0))
                 + 0.15 * (5 - int(p.get('maturidade', 0))) / 5.0 + 0.10 * float(p.get('cobertura', 0)), 2)


def recalcular(diag):
    for p in diag.get('processos') or []:
        p['prioridade'] = prioridade(p)
        if not p.get('recomendacao'):
            p['recomendacao'] = 'gerar_pop' if p['prioridade'] >= 0.7 else ('coletar_mais' if p['prioridade'] >= 0.4 else 'descartar')
    diag['processos'] = sorted(diag.get('processos') or [], key=lambda p: -p['prioridade'])
    return diag


def render_md(diag):
    eco = diag.get('ecossistema') or {}
    L = ['---', 'id: %s' % diag['id'], 'setor_codigo: %s' % diag['setor_codigo'], 'data: "%s"' % diag.get('data', ''), 'modelo: %s' % diag.get('modelo', ''),
         'versao_diretrizes: "%s"' % diag.get('versao_diretrizes', ''), '---', '',
         '# Diagnóstico de processos — %s (`%s`)' % (diag['setor'], diag['setor_codigo']), '',
         '> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: %d entrada(s) do Canvas (hash `%s…`) · Data %s' % (len(diag.get('fontes_entradas') or []), (diag.get('hash_fontes') or '')[:12], diag.get('data', '')[:10]), '',
         '## 1. Ecossistema do setor', '',
         tabela(['Campo', 'Valor'], [['Domínio', eco.get('dominio')], ['Subdomínios', ', '.join(eco.get('subdominios') or [])], ['Contextos vizinhos', ', '.join(eco.get('contextos_vizinhos') or [])],
                                     ['Sistemas', ', '.join(eco.get('sistemas') or [])], ['Normas recorrentes', '; '.join(eco.get('normas') or [])], ['Benchmarks (referência externa)', ', '.join(eco.get('benchmarks') or [])]]), '',
         '## 2. Processos identificados e qualificados', '',
         tabela(['Prior.', 'Código', 'Processo', 'Tipo', 'Mat.', 'Crit.', 'Freq.', 'Risco', 'Cob.', 'Recomendação', 'POP'],
                [[('%.2f' % p['prioridade']), p.get('codigo_sugerido'), p.get('nome'), p.get('tipo'), p.get('maturidade'), p.get('criticidade'), p.get('frequencia'), p.get('risco_conformidade'), p.get('cobertura'), p.get('recomendacao'), p.get('pop_existente') or '—'] for p in diag.get('processos') or []]), '']
    for p in diag.get('processos') or []:
        L += ['### %s — %s' % (p.get('codigo_sugerido'), p.get('nome')), '', cell(p.get('descricao')) if p.get('descricao') else '', '',
              tabela(['Campo', 'Valor'], [['Gatilho', p.get('gatilho')], ['Saída', p.get('saida')], ['Atores', ', '.join(p.get('atores') or [])], ['Sistemas', ', '.join(p.get('sistemas') or [])],
                                          ['Artefatos', ', '.join(p.get('artefatos') or [])], ['Interfaces', ', '.join(p.get('interfaces') or [])], ['Evidências', ', '.join(p.get('evidencias') or []) or '—'],
                                          ['Lacunas', ', '.join(p.get('lacunas') or []) or 'nenhuma'], ['Justificativa', p.get('justificativa') or '—']]), '']
    L += ['## 3. Lacunas do setor', '', lista(diag.get('lacunas_setor'), '— Nenhuma registrada'), '',
          '## 4. Lições propostas', '', tabela(['Lição', 'Regra proposta', 'Exemplo'], [[l.get('licao'), l.get('regra'), l.get('exemplo') or '—'] for l in diag.get('licoes_propostas') or []], '— Nenhuma'), '']
    if diag.get('observacoes'):
        L += ['> %s' % cell(diag['observacoes']), '']
    L += ['---', '_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/%s.json` (diretrizes v%s)._' % (diag.get('sigla'), diag.get('versao_diretrizes', ''))]
    return '\n'.join(L) + '\n'


def render(diag, write=True):
    diag = recalcular(diag)
    if write:
        f = os.path.join(cl.DIAG_DIR, '%s.json' % diag['sigla'])
        cl.save_json(f, diag)
        with io.open(f[:-5] + '.md', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(render_md(diag))
    return diag


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    files = sorted(glob.glob(os.path.join(cl.DIAG_DIR, '*.json'))) if '--todos' in sys.argv else [a if a.endswith('.json') else os.path.join(cl.DIAG_DIR, a.upper() + '.json') for a in args]
    if not files:
        print(__doc__)
        sys.exit(1)
    for f in files:
        d = render(cl.load_json(f))
        print('%s: %d processo(s) · md gerado' % (d['sigla'], len(d.get('processos') or [])))
