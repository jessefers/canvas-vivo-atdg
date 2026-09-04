#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_index — gera pops/README.md (índice de leitura de POPs, diagnósticos e diretrizes).

Uso: python3 scripts/render_index.py [--branch <nome>]
"""
import glob
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canvas_lib as cl  # noqa: E402


def main():
    org = cl.Org()
    pops = cl.iter_pops()
    grupos = {}
    for p in pops:
        chain = org.chain(p['setor_codigo'])
        raiz = chain[1] if len(chain) > 1 else chain[0]
        grupos.setdefault((raiz['num'], raiz['nome']), []).append(p)
    por_status = {}
    for p in pops:
        por_status[p['status']] = por_status.get(p['status'], 0) + 1
    diags = sorted(glob.glob(os.path.join(cl.DIAG_DIR, '*.json')))
    L = ['# Índice de leitura — POPs (Procedimentos Operacionais Padrão)', '',
         'Formato DDD híbrido (Divisão → Departamento → Descrição + Domain-Driven Design), com organograma e fluxograma BPMN 2.0 padrão Anne Bail. Cada POP tem três arquivos: `.md` (leitura), `.pop.json` (canônico) e `.bpmn.json` (especificação para o Miro). Status: `rascunho` (roteiro de coleta / sem evidência suficiente), `em_validacao` (completo, aguardando revisão do setor), `aprovado`.', '',
         '**Totais:** %d POPs (%s) · %d diagnósticos · %d agentes por processo · %d lições aprovadas.' % (
             len(pops), ', '.join('%d %s' % (v, k) for k, v in sorted(por_status.items())), len(diags), len(cl.load_json(cl.AG_REG, [])), len(cl.licoes_aprovadas())), '',
         '| Setor | Código | Título | Versão | Status | Passos | Agente |', '|---|---|---|---|---|---|---|']
    for (num, nome), ps in sorted(grupos.items()):
        for p in sorted(ps, key=lambda x: x['codigo']):
            L.append('| %s | [%s](%s/%s.md) | %s | %s | %s | %d | %s |' % (nome, p['codigo'], p['sigla'], p['codigo'], p['titulo'].replace('|', '/'), p['versao'], p['status'], len(p['playbook']['passos']), p.get('agente') or '—'))
    L += ['', '## Diagnósticos por setor', '', '| Setor | Arquivo | Processos | Data |', '|---|---|---|---|']
    for f in diags:
        d = cl.load_json(f)
        L.append('| %s (`%s`) | [%s.md](../diagnosticos/%s.md) | %d | %s |' % (d['setor'], d['setor_codigo'], d['sigla'], d['sigla'], len(d.get('processos') or []), str(d.get('data', ''))[:10]))
    L += ['', '## Diretrizes', '',
          '- [00 Índice](../diretrizes/00-indice.md) · [01 Formato DDD](../diretrizes/01-formato-ddd.md) · [02 Template do POP](../diretrizes/02-template-pop-playbook.md) · [03 Organograma](../diretrizes/03-organograma-canonico.md) · [04 BPMN Anne Bail](../diretrizes/04-bpmn-anne-bail.md) · [05 Rubrica de diagnóstico](../diretrizes/05-rubrica-diagnostico.md) · [06 Codificação e versionamento](../diretrizes/06-codificacao-versionamento.md) · [07 Lições aprendidas](../diretrizes/07-licoes-aprendidas.md) · [08 Template de agente](../diretrizes/08-template-agente-processo.md) · [09 Glossário](../diretrizes/09-glossario-institucional.md)', '',
          '_Gerado por `scripts/render_index.py` em %s._' % cl.today()]
    with io.open(os.path.join(cl.POPS_DIR, 'README.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(L) + '\n')
    print('pops/README.md: %d POPs, %d diagnósticos' % (len(pops), len(diags)))


if __name__ == '__main__':
    main()
