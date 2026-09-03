---
id: diretriz-07
titulo: Lições aprendidas (log append-only)
versao: "1.0"
atualizado_em: "2026-09-02"
---

# 07 — Lições aprendidas

Log **append-only**. Somente lições com `status: aprovada` são injetadas nos prompts dos agentes e do app. Ids sequenciais `L-NNN`. Nunca editar linhas anteriores: para reverter, registrar nova lição com `substitui: L-NNN`.

## Regras vigentes (aprovadas)

| id | data | origem | lição | regra | status |
|---|---|---|---|---|---|
| L-001 | 2026-09-02 | curador | POPs anteriores citavam servidores pelo nome, expondo dados pessoais em documentos amplamente distribuídos. | Referir sempre função/cargo; nomes apenas no bloco 13 (Validação), com anuência (LGPD). | aprovada |
| L-002 | 2026-09-02 | curador | Passos compostos ("conferir e lançar") dificultam a atribuição de responsável e a medição. | Um passo = uma ação; ações compostas viram passos distintos. | aprovada |
| L-003 | 2026-09-02 | curador | Interfaces com outros setores apareciam só no texto e sumiam do fluxograma. | Cada linha do mapa de contexto gera um elemento `captura` no BPMN e um passo na raia de destino. | aprovada |
| L-004 | 2026-09-02 | curador | Manuais regenerados do zero perdiam ajustes validados pelo setor. | Nunca regenerar POP existente: aplicar patch com changelog, fontes e versão. | aprovada |
| L-005 | 2026-09-02 | curador | Entradas do Canvas repetiam documentos com versões duplicadas ("(2)", "cópia", "teste"). | No diagnóstico, agrupar versões do mesmo documento e registrar lacuna `versao_documento`. | aprovada |
| L-006 | 2026-09-02 | curador | Códigos legados (CON-01, CTR-01, Almoxarifado 01–08) já circulam no manual institucional. | Preservar códigos legados como códigos de processo; não renumerar. | aprovada |
| L-007 | 2026-09-02 | curador | Referências externas (UFPR, UFABC, UNILA, IFPR) foram tratadas como norma em rascunhos. | Referência Externa é benchmark; normativa do POP só cita atos da Unioeste, do Estado do Paraná ou federais aplicáveis. | aprovada |

## Propostas pendentes

| id | data | origem | lição | regra proposta | status |
|---|---|---|---|---|---|

## Rejeitadas

| id | data | origem | lição | motivo da rejeição | status |
|---|---|---|---|---|---|
