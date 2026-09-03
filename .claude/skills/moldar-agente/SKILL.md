---
description: Instancia ou atualiza o agente moldado por processo (.claude/agents/pop-<codigo>.md) a partir do template diretrizes/08 e do POP canônico, registrando em agentes/registry.json. Use para "crie um agente para o processo X", "molde o agente do POP", ou /moldar-agente.
argument-hint: "<codigo ex. ALM-01 | sigla ex. ALM | --todos> [--forcar]"
allowed-tools: Bash(python3 scripts/*), Read, Glob
---

Molde o(s) agente(s) para **$ARGUMENTS**:

1. Execute `python3 scripts/moldar_agente.py $ARGUMENTS` (aceita código, sigla ou `--todos`; `--forcar` regera agentes existentes após mudança de diretrizes ou do POP).
2. Execute `python3 scripts/validate.py --sem-render --quiet` e `python3 scripts/sync_data.py --to-data`.
3. Se o processo exigir orientação específica que o template não cobre (sistema exclusivo, prazo legal, raia obrigatória), delegue ao subagente **moldador-agentes** para ajustar o corpo do agente gerado, mantendo o front matter válido.
4. Informe ao usuário os agentes criados/atualizados (`pop-<codigo>`), a versão de diretrizes embutida e como acioná-los (`/atualizar-pop <CODIGO>` ou delegação automática pela descrição).
