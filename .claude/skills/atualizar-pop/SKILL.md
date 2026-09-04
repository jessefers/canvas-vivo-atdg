---
description: Atualiza incrementalmente um POP existente quando surge novo passo, formulário, decisão, interface, regra ou alteração de processo — protocolo de patch (sem reescrever), com changelog, versão e diagramas regenerados. Use para "atualize o POP X", "adicione o passo/formulário Y ao processo X", "mudou o processo X", ou /atualizar-pop.
argument-hint: "<codigo ex. ALM-01> [--desde AAAA-MM-DD] [insumo em texto livre]"
---

Atualize o POP indicado em **$ARGUMENTS** pelo protocolo incremental (template `diretrizes/08-template-agente-processo.md`, seção "Protocolo de atualização").

Delegação: se existir `.claude/agents/pop-<codigo em minúsculas>.md`, delegue a tarefa ao subagente **pop-<codigo>** (agente moldado do processo) com a ferramenta Agent, passando o código, o insumo em texto livre (se houver) e a instrução de seguir seu protocolo; caso contrário, delegue ao subagente **construtor-pop** em modo atualização.

O subagente deve: (1) ler o `.pop.json`; (2) extrair insumos novos com `python3 scripts/extract_setor.py --setor <SIGLA> --desde <atualizado_em> --exclui <fontes_entradas>` e considerar o texto livre informado; (3) sem insumos ⇒ responder "sem novidades" e não alterar nada; (4) classificar cada insumo (passo novo / passo alterado / formulário / decisão / interface / regra / processo novo ⇒ recomendar `/gerar-pop`, sem impacto); (5) produzir somente `patch.json` (`schemas/patch.schema.json`); (6) aplicar com `python3 scripts/apply_patch.py <CODIGO> <patch.json>`; (7) `python3 scripts/validate.py --quiet` e `python3 scripts/sync_data.py --to-data`; (8) relatar versão anterior → nova, tipo de mudança, itens alterados e lições propostas.
