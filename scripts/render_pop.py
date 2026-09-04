#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_pop — renderiza POP canônico (.pop.json) em Markdown (.md) e especificação BPMN para o Miro (.bpmn.json).

Uso:
  python3 scripts/render_pop.py ALM-01 [CON-02 ...]   # renderiza códigos
  python3 scripts/render_pop.py --todos               # todos os POPs de pops/
  python3 scripts/render_pop.py --organograma         # regenera diretrizes/03-organograma-canonico.md
  python3 scripts/render_pop.py --check [--todos]     # compara sem gravar (sai com 1 se divergente)
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canvas_lib as cl  # noqa: E402
import bpmn_mermaid as bm  # noqa: E402


def cell(s):
    return str(s if s is not None else '').replace('|', '\\|').replace('\r', ' ').replace('\n', ' ').strip() or '—'


def lista(items, vazio='— A definir'):
    items = [i for i in (items or []) if str(i).strip()]
    return '\n'.join('- %s' % cell(i) for i in items) if items else vazio


def tabela(cabecalho, linhas, vazio='— A definir'):
    if not linhas:
        return vazio
    out = ['| ' + ' | '.join(cabecalho) + ' |', '|' + '---|' * len(cabecalho)]
    for l in linhas:
        out.append('| ' + ' | '.join(cell(c) for c in l) + ' |')
    return '\n'.join(out)


def render_md(pop, org=None, licoes=None):
    org = org or cl.Org()
    ddd = pop.get('ddd') or {}
    idn = pop.get('identificacao') or {}
    pb = pop.get('playbook') or {}
    spec = pop.get('bpmn_spec') or {}
    lic = {l['id']: l for l in (licoes if licoes is not None else cl.licoes_aprovadas())}
    L = []
    L += ['---', 'codigo: %s' % pop['codigo'], 'titulo: "%s"' % pop['titulo'].replace('"', "'"), 'versao: "%s"' % pop['versao'],
          'status: %s' % pop['status'], 'setor_codigo: %s' % pop['setor_codigo'], 'setor: "%s"' % pop['setor'].replace('"', "'"),
          'atualizado_em: "%s"' % pop.get('atualizado_em', ''), 'agente: %s' % (pop.get('agente') or '—'),
          'versao_diretrizes: "%s"' % pop.get('versao_diretrizes', ''), '---', '']
    L.append('# POP %s — %s' % (pop['codigo'], pop['titulo']))
    L.append('')
    L.append('> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **%s** · Status **%s** · Atualizado em %s' % (pop['versao'], pop['status'], pop.get('atualizado_em', '')[:10]))
    L.append('')
    L.append('## 0. Cabeçalho DDD')
    L.append('')
    L.append(tabela(['Divisão', 'Departamento', 'Descrição'], [[ddd.get('divisao'), ddd.get('departamento'), ddd.get('descricao')]]))
    L.append('')
    L.append(tabela(['Domínio', 'Subdomínio', 'Tipo', 'Contexto delimitado'], [[ddd.get('dominio'), ddd.get('subdominio'), ddd.get('tipo_subdominio'), ddd.get('contexto')]]))
    L.append('')
    L.append('### 0.3 Linguagem ubíqua (glossário do processo)')
    L.append('')
    L.append(tabela(['Termo', 'Definição', 'Sistema'], [[g.get('termo'), g.get('definicao'), g.get('sistema')] for g in ddd.get('glossario') or []],
                    'Herda integralmente o glossário institucional (`diretrizes/09-glossario-institucional.md`); sem termos locais adicionais.'))
    L.append('')
    L.append('## 1. Identificação')
    L.append('')
    rows = [['Código', pop['codigo']], ['Setor', '%s (`%s`)' % (pop['setor'], pop['setor_codigo'])], ['Responsável (função)', idn.get('responsavel')],
            ['Periodicidade', idn.get('periodicidade')], ['Subordinação', idn.get('subordinacao')],
            ['Normativa', '; '.join(idn.get('normativa') or []) or 'A definir'], ['Produto ATDG', idn.get('produto_atdg')],
            ['Pasta OneDrive', idn.get('pasta_onedrive')], ['Fontes (entradas do Canvas)', ', '.join(pop.get('fontes_entradas') or []) or '—'],
            ['Lacunas abertas', ', '.join(pop.get('lacunas') or []) or 'nenhuma'], ['Agente responsável', pop.get('agente') or '— (não moldado)']]
    L.append(tabela(['Campo', 'Valor'], rows))
    L.append('')
    L.append('## 2. Organograma')
    L.append('')
    L.append('```mermaid\n%s\n```' % pop.get('organograma_mermaid', ''))
    L.append('')
    L.append('## 3. Playbook')
    L.append('')
    L.append('### 3.1 Gatilho (evento de domínio)')
    L.append('')
    g = pb.get('gatilho') or {}
    L.append('**%s**%s' % (g.get('evento') or 'A definir', (' — origem: %s' % g['origem']) if g.get('origem') else ''))
    L.append('')
    L.append('### 3.2 Entrada')
    L.append('')
    L.append(lista(pb.get('entrada')))
    L.append('')
    L.append('### 3.3 Passo a passo')
    L.append('')
    L.append(tabela(['Nº', 'Ação', 'Responsável', 'Sistema', 'Artefato', 'Prazo', 'Evento'],
                    [[p.get('n'), p.get('acao'), p.get('responsavel'), p.get('sistema') or '—', p.get('artefato') or '—', p.get('prazo') or 'A definir', p.get('evento') or '—'] for p in pb.get('passos') or []],
                    '— A documentar (nenhum passo registrado)'))
    L.append('')
    L.append('### 3.4 Saída (entregáveis)')
    L.append('')
    L.append(lista(pb.get('saida')))
    L.append('')
    L.append('## 4. Formulários e artefatos (agregados)')
    L.append('')
    L.append(tabela(['Nome', 'Tipo', 'Sistema', 'Campos-chave', 'Preenchimento'],
                    [[a.get('nome'), a.get('tipo'), a.get('sistema') or '—', ', '.join(a.get('campos_chave') or []) or '—', a.get('responsavel_preenchimento') or '—'] for a in pop.get('artefatos') or []]))
    L.append('')
    L.append('## 5. Decisões, exceções e pontos de atenção')
    L.append('')
    L.append(tabela(['Decisão', 'Condição', 'Sim →', 'Não →'], [[d.get('decisao'), d.get('condicao'), d.get('sim'), d.get('nao')] for d in pop.get('decisoes') or []], '— Sem decisões registradas'))
    L.append('')
    L.append('**Pontos de atenção**')
    L.append('')
    L.append(lista(pop.get('pontos_atencao'), '— Nenhum registrado'))
    L.append('')
    L.append('## 6. Contingência')
    L.append('')
    L.append(lista(pop.get('contingencia')))
    L.append('')
    L.append('## 7. Checklist')
    L.append('')
    ck = [i for i in (pop.get('checklist') or []) if str(i).strip()]
    L.append('\n'.join('- ( ) %s' % cell(i) for i in ck) if ck else '— A definir')
    L.append('')
    L.append('## 8. KPI / Indicadores')
    L.append('')
    L.append(tabela(['Indicador', 'Fórmula', 'Meta', 'Fonte'], [[k.get('indicador'), k.get('formula') or 'A definir', k.get('meta') or 'A definir', k.get('fonte') or 'A definir'] for k in pop.get('kpis') or []]))
    L.append('')
    L.append('## 9. Mapa de contexto (interfaces inter-setoriais)')
    L.append('')
    L.append(tabela(['Origem', 'Relação', 'Destino', 'Artefato', 'Canal'], [[m.get('origem'), m.get('relacao'), m.get('destino'), m.get('artefato') or '—', m.get('canal') or '—'] for m in pop.get('mapa_contexto') or []], '— Sem interfaces registradas'))
    L.append('')
    L.append('## 10. Fluxograma (BPMN 2.0 — padrão Anne Bail)')
    L.append('')
    L.append('```mermaid\n%s\n```' % pop.get('fluxograma_mermaid', ''))
    L.append('')
    L.append('## 11. Especificação BPMN para o Miro')
    L.append('')
    L.append('**Raias:** %s' % (' · '.join(spec.get('raias') or []) or '—'))
    L.append('')
    L.append(tabela(['Id', 'Tipo', 'Elemento', 'Raia'], [[e.get('id'), e.get('tipo'), e.get('label'), e.get('raia')] for e in spec.get('elementos') or []]))
    L.append('')
    L.append(tabela(['De', 'Para', 'Rótulo'], [[c.get('de'), c.get('para'), c.get('label') or '—'] for c in spec.get('conexoes') or []]))
    L.append('')
    if spec.get('observacoes_construcao_miro'):
        L.append('_%s_' % cell(spec['observacoes_construcao_miro']))
        L.append('')
    L.append('## 12. Histórico de versões')
    L.append('')
    L.append(tabela(['Versão', 'Data', 'Autor', 'Tipo', 'Mudanças', 'Fontes'],
                    [[c.get('versao'), c.get('data'), c.get('autor'), c.get('tipo'), '; '.join(c.get('mudancas') or []), ', '.join(c.get('fontes') or []) or '—'] for c in pop.get('changelog') or []]))
    L.append('')
    L.append('## 13. Validação e aprovação')
    L.append('')
    v = pop.get('validacao') or {}
    L.append(tabela(['Papel', 'Função / unidade', 'Data'], [['Elaboração', v.get('elaboracao'), pop.get('criado_em', '')[:10]], ['Revisão', v.get('revisao'), '___/___/______'], ['Aprovação', v.get('aprovacao'), v.get('data_aprovacao') or '___/___/______']]))
    L.append('')
    L.append('## 14. Lições incorporadas')
    L.append('')
    ids = pop.get('licoes_aplicadas') or []
    L.append('\n'.join('- **%s** — %s' % (i, lic[i]['regra'] if i in lic else 'ver `diretrizes/07-licoes-aprendidas.md`') for i in ids) if ids else '— Nenhuma lição específica além das diretrizes vigentes.')
    L.append('')
    if pop.get('observacoes'):
        L.append('> **Observações:** %s' % cell(pop['observacoes']))
        L.append('')
    L.append('---')
    L.append('_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `%s` (diretrizes v%s)._' % (os.path.relpath(cl.pop_paths(pop)[0], cl.ROOT), pop.get('versao_diretrizes', '')))
    return '\n'.join(L) + '\n'


def bpmn_export(pop):
    spec = pop.get('bpmn_spec') or {}
    return {'setor': pop['setor'], 'codigo': pop['codigo'], 'gerado_em': cl.now_iso(), 'padrao': 'BPMN 2.0 — Anne Bail (UNIOESTE Foz)',
            'processos': [{'nome': '%s — %s' % (pop['codigo'], pop['titulo']), 'descricao': (pop.get('ddd') or {}).get('descricao', ''),
                           'raias': spec.get('raias') or [], 'elementos': spec.get('elementos') or [], 'conexoes': spec.get('conexoes') or [],
                           'observacoes_construcao_miro': spec.get('observacoes_construcao_miro', '')}]}


def render_pop(pop, org=None, write=True, licoes=None):
    md = render_md(pop, org, licoes)
    if write:
        pj, pm, pbp = cl.pop_paths(pop)
        os.makedirs(os.path.dirname(pm), exist_ok=True)
        with io.open(pm, 'w', encoding='utf-8', newline='\n') as f:
            f.write(md)
        cl.save_json(pbp, bpmn_export(pop))
    return md


def check_pop(pop, org=None, licoes=None):
    pm = cl.pop_paths(pop)[1]
    if not os.path.exists(pm):
        return False
    atual = io.open(pm, encoding='utf-8').read()
    return atual == render_md(pop, org, licoes)


def render_organograma_md(org=None):
    org = org or cl.Org()
    L = ['---', 'id: diretriz-03', 'titulo: Organograma canônico codificado', 'versao: "%s"' % org.data.get('versao', '1.0'), 'atualizado_em: "%s"' % org.data.get('atualizado_em', ''), '---', '',
         '# 03 — Organograma canônico do Campus Foz do Iguaçu (codificado)', '',
         'Fonte: `03-organograma-canonico.json` (este `.md` é gerado por `python3 scripts/render_pop.py --organograma`; não editar à mão). Convenções: setor nível 1 `S<num>-<SIGLA>`, subdivisão `S<num>.<nn>-<SIGLA>`, processo `<SIGLA>-<nn>`.', '',
         '| Código | Sigla | Setor | Rótulo no app (`id_app`) | Pai | Status | Domínio | Tipo | Gera POP | Processos conhecidos |', '|---|---|---|---|---|---|---|---|---|---|']
    for s in org.setores:
        pk = ', '.join(p['codigo'] for p in s.get('processos_conhecidos') or []) or '—'
        L.append('| `%s` | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (s['codigo'], s['sigla'], cell(s['nome']), cell(s['id_app']), s.get('pai') or '—', s['status'], s['dominio'], s['tipo_subdominio'], 'sim' if s.get('gera_pop', True) else 'não', pk))
    L += ['', '## Árvore (Mermaid)', '', '```mermaid', 'graph TD']
    for s in org.setores:
        nid = bm.safe_id(s['codigo'])
        L.append('  %s["%s<br/>%s"]' % (nid, s['codigo'], bm.esc(s['nome'], 60)))
        if s.get('pai'):
            L.append('  %s --> %s' % (bm.safe_id(s['pai']), nid))
    L += ['```', '', '## Processos conhecidos (códigos legados preservados)', '', '| Código | Processo | Escopo | Setor |', '|---|---|---|---|']
    for s in org.setores:
        for p in s.get('processos_conhecidos') or []:
            L.append('| `%s` | %s | %s | `%s` |' % (p['codigo'], cell(p['nome']), cell(p.get('escopo', '')), s['codigo']))
    text = '\n'.join(L) + '\n'
    with io.open(os.path.join(cl.DIR_DIR, '03-organograma-canonico.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    return text


def main(argv):
    org = cl.Org()
    if '--organograma' in argv:
        render_organograma_md(org)
        print('03-organograma-canonico.md regenerado (%d setores)' % len(org.setores))
        return 0
    check = '--check' in argv
    codes = [a for a in argv if not a.startswith('--')]
    pops = cl.iter_pops() if ('--todos' in argv or not codes) else [cl.load_pop(c) for c in codes]
    licoes = cl.licoes_aprovadas()
    bad = 0
    for pop in pops:
        if check:
            if not check_pop(pop, org, licoes):
                bad += 1
                print('DIVERGENTE:', pop['codigo'])
        else:
            render_pop(pop, org, True, licoes)
    if check:
        print('%d POP(s) verificados, %d divergente(s)' % (len(pops), bad))
        return 1 if bad else 0
    print('%d POP(s) renderizados' % len(pops))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
