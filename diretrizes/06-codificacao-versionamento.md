---
id: diretriz-06
titulo: Codificação, arquivos, status e versionamento
versao: "1.1"
atualizado_em: "2026-09-03"
---

# 06 — Codificação, arquivos, status e versionamento

## Códigos

| Nível | Formato | Exemplos |
|---|---|---|
| Setor nível 1 | `S<num>-<SIGLA>` | `S01-DG`, `S02-ATDG`, `S03-SADM`, `S07-CCSA` |
| Subdivisão / frente / colegiado | `S<num>.<nn>-<SIGLA>` | `S03.04-ALM`, `S02.01-CON`, `S07.01-CCSA-ADM` |
| Processo | `<SIGLA>-<nn>` | `ALM-01`, `CON-03`, `DRH-01`, `CCSA-ADM-01`; `<SIGLA>-00` = visão geral do setor |
| POP (id) | `pop-<codigo minúsculo>` | `pop-alm-01` |
| Diagnóstico (id) | `diag-<sigla minúscula>-<AAAAMMDD>` | `diag-alm-20260902` |
| Agente por processo | `pop-<codigo minúsculo>` (`.claude/agents/pop-alm-01.md`) | `agentes/registry.json → id: agente-pop-alm-01` |
| Lição | `L-NNN` | `L-001` |

Siglas são **únicas no campus** (validadas por `scripts/validate.py`). Códigos legados do manual institucional (`CON-01…05`, `CAP-01/02`, `CTR-01…05`, Almoxarifado `01…08` → `ALM-01…08`) são preservados.

## Arquivos

```
pops/<SIGLA>/<CODIGO>.pop.json      # canônico
pops/<SIGLA>/<CODIGO>.md            # renderizado (render_pop.py) — não editar à mão
pops/<SIGLA>/<CODIGO>.bpmn.json     # especificação para o Miro (mesmo esquema do app)
diagnosticos/<SIGLA>.json | .md     # diagnóstico mais recente do setor (histórico em changelog do próprio arquivo)
agentes/registry.json               # registro dos agentes por processo
```

## Status

`rascunho` → `em_validacao` → `aprovado` → `obsoleto`

- `rascunho`: gerado por scaffold ou com < 3 passos / lacunas essenciais;
- `em_validacao`: POP completo aguardando revisão do responsável do setor;
- `aprovado`: validado (bloco 13 preenchido); **qualquer patch** devolve o POP a `em_validacao`;
- `obsoleto`: substituído (indicar `substituido_por`).

## Versão semântica `MAJOR.MINOR.PATCH`

| Incremento | Quando |
|---|---|
| PATCH | correção textual, glossário, formatação, normativa complementar sem mudar passos |
| MINOR | passo adicionado ou alterado, artefato/formulário novo, decisão nova, KPI novo, interface nova |
| MAJOR | passo removido, raia alterada/renomeada, reestruturação, desmembramento/fusão de processos, mudança de responsável do processo |

Scaffold nasce em `0.1.0`; primeiro POP completo = `1.0.0`. A regra é aplicada por `scripts/apply_patch.py` / `applyPopPatch()`; o campo `tipo_mudanca` devolvido pelo modelo é apenas sugestão.

## Changelog obrigatório (`changelog[]`)

`{versao, data, autor (função ou "agente:<nome>"), tipo (patch|minor|major), mudancas[], fontes[] (ids de entradas), motivo}` — uma entrada por patch, nunca reescrever entradas anteriores.

## Fontes e cache

`fontes_entradas[]` guarda os ids de entradas já incorporados; `hash_fontes` = SHA-256 de `id|ts` ordenados. Atualização incremental só considera entradas com `ts > atualizado_em` ou id ∉ `fontes_entradas`; hash igual ⇒ "sem novidades", sem chamada ao modelo.

## Nome dos commits

`POP <SIGLA> vX.Y — <resumo>` · `DIAG <SIGLA> — <data>` · `DIRETRIZES vX.Y — <resumo>` · `AGENTE pop-<codigo>`.

## Regras incorporadas na v1.1 (lições aprovadas em 2026-09-03)

- **POP inferido permanece rascunho (L-019).** Em setores sem entradas no Canvas, preencher o responsável por função em cada passo (para modelar as raias), mas manter `identificacao.responsavel = "A definir"` até validação formal do setor; isso preserva a distinção entre POP evidenciado (`major` → `em_validacao`) e inferido (`minor` → `rascunho`).
- **Raias novas são mudança maior (L-018).** `bpmn_delta.raias_add` escala o tipo para `major`; em POPs inferidos, usar `regenerar_de_passos`.
