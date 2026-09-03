---
description: Diagnostica e qualifica os processos de um setor, divisão ou frente do Campus Foz (UNIOESTE) a partir das entradas do Canvas Vivo, gerando diagnosticos/<SIGLA>.json e .md com prioridade, maturidade, lacunas e recomendação (gerar_pop, coletar_mais, agrupar, descartar). Use quando o usuário pedir diagnóstico, levantamento ou priorização de processos de um setor, ou digitar /diagnosticar.
argument-hint: "<setor|sigla|codigo|todos>"
context: fork
agent: diagnostico-processos
---

Diagnostique e qualifique os processos do alvo **$ARGUMENTS** conforme `.claude/agents/diagnostico-processos.md` e `diretrizes/05-rubrica-diagnostico.md`.

- Se o alvo for `todos`: liste os setores que geram POP em `diretrizes/03-organograma-canonico.json` (`gera_pop: true`), priorize os que têm entradas (`python3 scripts/extract_setor.py --setor <sigla> --max 1` mostra `total`) e diagnostique um a um, gravando `diagnosticos/<SIGLA>.json|md` para cada. Setores sem entradas recebem diagnóstico mínimo (processos conhecidos como `coletar_mais`).
- Se o alvo for um setor de nível 1 com subdivisões (ex.: `SADM`), diagnostique o setor e cada subdivisão separadamente (uma sigla por arquivo).
- Ao final, rode `python3 scripts/render_diag.py --todos`, `python3 scripts/validate.py --sem-render --quiet` e `python3 scripts/sync_data.py --to-data`, e apresente a tabela consolidada (setor, processo, prioridade, recomendação, POP existente) com os próximos passos (`/gerar-pop <codigo>`).
