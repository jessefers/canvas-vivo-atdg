---
description: Gera (ou completa) o POP em modo playbook de um processo — formato DDD híbrido, organograma e fluxograma BPMN 2.0 Anne Bail — a partir do diagnóstico e das entradas do Canvas Vivo, sempre por patch sobre pops/<SIGLA>/<CODIGO>.pop.json. Use para "gerar POP", "montar o POP do processo X", "completar o esqueleto do POP", ou /gerar-pop.
argument-hint: "<codigo ex. ALM-01 | sigla ex. ALM>"
context: fork
agent: construtor-pop
---

Gere ou complete o(s) POP(s) de **$ARGUMENTS** conforme `.claude/agents/construtor-pop.md`.

1. Se o argumento for uma sigla de setor, trate todos os POPs de `pops/<SIGLA>/` cujo status seja `rascunho` e que tenham evidência suficiente no diagnóstico (`recomendacao: gerar_pop`) ou nas entradas; os demais recebem apenas lacunas e roteiro de coleta (`coletar_mais`).
2. Se não houver diagnóstico do setor, rode antes `python3 scripts/extract_setor.py --setor <SIGLA> --saida /tmp/<sigla>.json` e trabalhe com as entradas; recomende `/diagnosticar <SIGLA>` no relatório.
3. Se o POP não existir, crie o esqueleto (`python3 scripts/scaffold_pops.py --setor <SIGLA>` ou estrutura equivalente com `versao 0.1.0`) e então construa por patch.
4. Aplique cada patch com `python3 scripts/apply_patch.py <CODIGO> <patch.json>`; ao completar (≥ 3 passos, responsável, gatilho, entrada, saída) use `tipo_mudanca: "major"` para promover a `1.0.0`.
5. Finalize com `python3 scripts/validate.py --quiet` e `python3 scripts/sync_data.py --to-data`, e informe: versão anterior → nova, passos, artefatos, interfaces, lacunas remanescentes e lições propostas.
