---
description: Orquestra o ciclo completo por setor ou para todos — esqueleto → diagnóstico → geração/atualização de POPs → agentes por processo → curadoria de lições → sincronização e validação — em lotes com checkpoint. Use apenas quando o usuário pedir explicitamente o ciclo completo (/ciclo-pop).
argument-hint: "<setor|sigla|todos> [--sem-llm]"
disable-model-invocation: true
---

Execute o ciclo completo para **$ARGUMENTS**, em lotes, com checkpoint por setor.

1. **Esqueleto (sem IA):** `python3 scripts/scaffold_pops.py --setor <SIGLA>` (ou `--todos`).
2. **Diagnóstico:** para cada sigla do lote (setor e subdivisões), delegue ao subagente **diagnostico-processos** (equivale a `/diagnosticar <SIGLA>`). Com `--sem-llm`, pule esta etapa e as seguintes que exigem modelo: apenas esqueleto, agentes por script, sincronização e validação.
3. **POPs:** para cada processo com `recomendacao: gerar_pop`, delegue ao subagente **construtor-pop** (equivale a `/gerar-pop <CODIGO>`); para POPs já completos, `/atualizar-pop <CODIGO>`.
4. **Agentes:** `python3 scripts/moldar_agente.py <SIGLA>` para todos os POPs do setor com status diferente de `obsoleto`.
5. **Curadoria:** delegue ao subagente **curador-diretrizes** a consolidação das `licoes_propostas` do lote (registrar como propostas; não aprovar).
6. **Sincronizar e validar:** `python3 scripts/sync_data.py --to-data` e `python3 scripts/validate.py` (zero erros antes de prosseguir ao próximo setor).
7. **Checkpoint:** apresente o resumo do lote (POPs criados/atualizados com versões, agentes, lições propostas, lacunas) e prossiga ao próximo setor. Para `todos`, seguir a ordem por riqueza de entradas: ALM, DRH, DFIN, DCOM, DLIC, DPG, COLEG, ATDG (CON/CAP/CTR/MAP), DGRAD, DG, DMC, DCEN, demais.
8. Ao final, sugira o commit por lote (`POP <SIGLA> vX.Y — <resumo>`), sem executá-lo salvo pedido explícito.
