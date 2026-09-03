---
id: diretriz-05
titulo: Rubrica de identificação, diagnóstico e qualificação
versao: "1.1"
atualizado_em: "2026-09-03"
---

# 05 — Rubrica de diagnóstico e qualificação de processos

Aplicada pelo agente `diagnostico-processos` (Claude Code) e por `diagnosticarSetor()` (app) sobre as entradas de um setor (e subdivisões) do Canvas Vivo, com saída no esquema `schemas/diagnostico.schema.json`.

## 1. Identificação (o que é a unidade de trabalho)

| `tipo` | Definição | Exemplo |
|---|---|---|
| `processo` | conjunto recorrente de atividades com gatilho, entrada, saída e responsável definidos | Recebimento de materiais |
| `subprocesso` | recorte de um processo maior, com entrega intermediária | Conferência qualitativa da NF |
| `acao` | atividade pontual/isolada sem recorrência ou sem fluxo próprio | Atualizar lista de contatos |
| `projeto` | esforço temporário com início/fim e produto único | Mapeamento de processos dos colegiados |

Regras: **um POP por processo**; subprocesso vira seção do POP pai ou POP próprio quando tiver raia/responsável distinto; `acao` entra como passo ou checklist; `projeto` gera POP apenas para as rotinas recorrentes que dele decorrem.

## 2. Diagnóstico (escalas)

| Dimensão | Escala | Critério |
|---|---|---|
| `maturidade` | 0–5 | 0 inexistente · 1 informal/tácito · 2 descrito parcialmente (entrada/passos) · 3 documentado com responsável e normativa · 4 medido (KPI) e com contingência · 5 otimizado/auditado e revisado periodicamente |
| `criticidade` | 0–1 | impacto institucional de falha: 1,0 legal/financeiro/TCE-PR; 0,7 continuidade de serviço essencial; 0,4 qualidade/retrabalho; 0,2 conveniência |
| `frequencia` | 0–1 | 1,0 diário · 0,8 semanal · 0,6 mensal · 0,4 semestral · 0,2 anual/esporádico |
| `risco_conformidade` | 0–1 | 1,0 sujeito a auditoria/norma cogente (Lei 14.133, TCE-PR, LGPD) · 0,6 norma interna · 0,2 sem exigência normativa |
| `cobertura` | 0–1 | proporção de campos essenciais evidenciados nas entradas (gatilho, entrada, passos, saída, responsável, normativa, sistema, artefatos) |

## 3. Qualificação (prioridade e recomendação)

`prioridade = 0,30·criticidade + 0,25·frequencia + 0,20·risco_conformidade + 0,15·(5 − maturidade)/5 + 0,10·cobertura`

| Faixa | `recomendacao` | Ação |
|---|---|---|
| ≥ 0,70 | `gerar_pop` | gerar POP completo (mínimo 3 passos) |
| 0,40 – 0,69 | `coletar_mais` | gerar POP em `rascunho` com lacunas explícitas e roteiro de coleta |
| < 0,40 | `descartar` ou `agrupar` | manter como passo/checklist de outro POP, ou backlog |

Evidência mínima para `gerar_pop`: `maturidade ≥ 2` **ou** ≥ 2 entradas convergentes. Processos sem evidência mínima recebem `coletar_mais`.

## 4. Lacunas (vocabulário fechado)

`responsavel`, `normativa`, `gatilho`, `entrada`, `saida`, `passos`, `sistema`, `formulario`, `prazo`, `kpi`, `contingencia`, `interface_setorial`, `versao_documento`, `dados_pessoais_lgpd`.

## 5. Ecossistema (visão de domínio do setor)

Para cada setor diagnosticado: `dominio` (do organograma canônico), `subdominios[]` identificados, `contextos_vizinhos[]` (setores com que troca artefatos), `sistemas[]` e `normas[]` recorrentes. Referências externas (`S00-REF`) entram apenas como `benchmarks[]`.

## 6. Saída do diagnóstico

Objeto único conforme `schemas/diagnostico.schema.json`, com `processos[]` ordenados por `prioridade` decrescente, `codigo_sugerido` respeitando `06-codificacao-versionamento.md` (reutilizar códigos de `processos_conhecidos` quando o processo coincidir), `evidencias[]` (ids das entradas), `lacunas[]` e `licoes_propostas[]`.

## Regras incorporadas na v1.1 (lições aprovadas em 2026-09-03)

- **Piso de prioridade por risco de conformidade (L-009).** Processo com `risco_conformidade ≥ 0,90` e evidência de auditoria externa (TCE-PR, PRAF, fiscalização) recebe `auditoria_externa: true` e piso de prioridade **0,70** (`gerar_pop`), mesmo com frequência baixa (ex.: inventário geral anual).
- **Fluxogramas em imagem (L-013).** Documento cujo fluxo existe só como imagem (sem texto extraível) gera a lacuna `passos` e exige revisão visual manual antes de elevar a maturidade do processo.
- **Referências de outras instituições (L-014).** Documentos de outras instituições entram apenas em `ecossistema.benchmarks`; nunca como evidência de processo próprio nem como normativa.
- **Setor sem evidência operacional (L-017).** Setor cujas fontes se resumem a um único registro genérico de playbook recebe POP-roteiro de coleta (status `rascunho`), nunca POP operacional completo.
