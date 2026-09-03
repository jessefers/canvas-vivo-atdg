---
description: Governa o aprendizado do ecossistema — lista, propõe, aprova ou rejeita lições em diretrizes/07-licoes-aprendidas.md (log append-only) e sincroniza data.json; lições aprovadas passam a valer nos prompts dos agentes e do app. Use para "isso vira regra", "aprenda que…", "aprovar/rejeitar a lição L-NNN", ou /aprender-diretriz.
argument-hint: "listar [--status proposta] | propor \"<lição>\" \"<regra>\" | aprovar L-NNN | rejeitar L-NNN \"<motivo>\""
allowed-tools: Bash(python3 scripts/*), Read
---

Ação solicitada: **$ARGUMENTS**

- `listar [--status …]` → `python3 scripts/licoes.py listar …`
- `propor "<lição>" "<regra>"` → `python3 scripts/licoes.py propor "<lição>" "<regra>" --origem usuario` (o id `L-NNN` é gerado e a proposta fica pendente).
- `aprovar L-NNN` → `python3 scripts/licoes.py aprovar L-NNN`; em seguida delegue ao subagente **curador-diretrizes** para avaliar se a lição aprovada exige edição em `diretrizes/01–06/09` (incrementar `versao`) e, se a estrutura do POP mudou, `python3 scripts/render_pop.py --todos` + `python3 scripts/validate.py`.
- `rejeitar L-NNN "<motivo>"` → `python3 scripts/licoes.py rejeitar L-NNN "<motivo>"`.
- Sem argumentos ou pedido em linguagem natural ("isso vira regra: …") → formule lição e regra em uma frase cada e registre como proposta; nunca aprove por conta própria.

Sempre terminar com `python3 scripts/sync_data.py --to-data` (os scripts de lições já sincronizam) e mostrar a tabela atual de lições pendentes.
