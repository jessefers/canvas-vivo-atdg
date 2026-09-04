---
id: diag-ctr-20260903
setor_codigo: S02.03-CTR
data: "2026-09-03T02:02:00Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — ATDG — Assessoria Técnica da Direção Geral (`S02.03-CTR`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 0 entrada(s) do Canvas (hash `e3b0c44298fc…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Controladoria, Compliance e Riscos |
| Subdomínios | Auditoria TCE-PR, Compliance Institucional, Relacionamento com a PRAF, Fiscalização Externa, Gestão de Riscos |
| Contextos vizinhos | TCE-PR, PRAF, Setor demandante/respondente, Direção Geral do Campus |
| Sistemas | e-Protocolo, OneDrive ATDG |
| Normas recorrentes | — |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.71 | CTR-01 | Auditoria TCE-PR | processo | 0 | 0.9 | 0.35 | 0.9 | 0.18 | gerar_pop | pop-ctr-01 |
| 0.67 | CTR-04 | Fiscalização Externa | processo | 0 | 0.85 | 0.3 | 0.85 | 0.15 | coletar_mais | pop-ctr-04 |
| 0.66 | CTR-02 | Compliance Institucional | processo | 0 | 0.75 | 0.5 | 0.7 | 0.15 | coletar_mais | pop-ctr-02 |
| 0.60 | CTR-03 | Relacionamento com a PRAF | processo | 0 | 0.65 | 0.45 | 0.65 | 0.15 | coletar_mais | pop-ctr-03 |
| 0.57 | CTR-05 | Gestão de Riscos | processo | 0 | 0.7 | 0.3 | 0.6 | 0.15 | coletar_mais | pop-ctr-05 |

### CTR-01 — Auditoria TCE-PR

Auditoria TCE-PR — demandas, prazos, respostas formais.

| Campo | Valor |
|---|---|
| Gatilho | Recebimento de demanda, notificação ou diligência do TCE-PR dirigida ao Campus |
| Saída | Resposta formal encaminhada ao TCE-PR dentro do prazo |
| Atores | TCE-PR, Assessoria Técnica da Direção Geral (ATDG), Setor respondente, Direção Geral do Campus |
| Sistemas | e-Protocolo |
| Artefatos | Registro de demandas do TCE-PR, Resposta formal ao TCE-PR |
| Interfaces | Setor respondente, Direção Geral do Campus |
| Evidências | — |
| Lacunas | responsavel, kpi, formulario, prazo, normativa |
| Justificativa | Processo de maior risco de conformidade do subdomínio (auditoria de órgão de controle externo); sem entradas do Canvas, playbook construído por inferência (minor, rascunho). |

### CTR-04 — Fiscalização Externa

Fiscalização Externa — visitas, diligências, relatórios.

| Campo | Valor |
|---|---|
| Gatilho | Comunicação de visita, inspeção ou diligência de fiscalização externa ao Campus |
| Saída | Fiscalização atendida e recomendações monitoradas |
| Atores | TCE-PR, Assessoria Técnica da Direção Geral (ATDG), Setor respondente |
| Sistemas | e-Protocolo |
| Artefatos | Plano de atendimento às recomendações de fiscalização, Registro de fiscalizações externas |
| Interfaces | Setor respondente |
| Evidências | — |
| Lacunas | responsavel, kpi, formulario, prazo, normativa |
| Justificativa | Sem entradas do Canvas; playbook construído por inferência a partir do escopo do manual institucional (minor, rascunho); interage com CTR-01 (recomendações podem repetir achados de auditoria). |

### CTR-02 — Compliance Institucional

Compliance Institucional — riscos, planos de mitigação, monitoramento.

| Campo | Valor |
|---|---|
| Gatilho | Identificação de risco de conformidade ou de não conformidade institucional |
| Saída | Plano de mitigação aprovado e matriz de riscos atualizada |
| Atores | Setor demandante, Assessoria Técnica da Direção Geral (ATDG), Direção Geral do Campus |
| Sistemas | OneDrive ATDG, e-Protocolo |
| Artefatos | Matriz de riscos institucionais, Plano de mitigação de risco |
| Interfaces | Direção Geral do Campus |
| Evidências | — |
| Lacunas | responsavel, kpi, formulario, prazo, normativa |
| Justificativa | Sem entradas do Canvas; playbook construído por inferência a partir do escopo do manual institucional (minor, rascunho); interage com CTR-01, CTR-04 e CTR-05. |

### CTR-03 — Relacionamento com a PRAF

Relacionamento com a PRAF — fluxos financeiros, conferências.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de conferência ou alinhamento de fluxo financeiro entre o Campus e a PRAF |
| Saída | Conferência financeira concluída e pendências regularizadas |
| Atores | PRAF, Assessoria Técnica da Direção Geral (ATDG) |
| Sistemas | A definir, OneDrive ATDG |
| Artefatos | Planilha de conciliação financeira, Registro de conferências financeiras com a PRAF |
| Interfaces | PRAF |
| Evidências | — |
| Lacunas | responsavel, kpi, formulario, prazo, normativa |
| Justificativa | Sem entradas do Canvas; playbook construído por inferência a partir do escopo do manual institucional (minor, rascunho); sistema financeiro da PRAF ainda não identificado. |

### CTR-05 — Gestão de Riscos

Gestão de Riscos — mapeamento, probabilidade, impacto.

| Campo | Valor |
|---|---|
| Gatilho | Definição do ciclo periódico de gestão de riscos institucionais |
| Saída | Matriz de riscos atualizada e relatório do ciclo consolidado |
| Atores | Setor demandante, Assessoria Técnica da Direção Geral (ATDG), Direção Geral do Campus |
| Sistemas | OneDrive ATDG |
| Artefatos | Matriz de riscos institucionais (ciclo de mapeamento), Relatório de gestão de riscos do ciclo |
| Interfaces | Direção Geral do Campus |
| Evidências | — |
| Lacunas | responsavel, kpi, formulario, prazo, normativa |
| Justificativa | Sem entradas do Canvas; playbook construído por inferência a partir do escopo do manual institucional (minor, rascunho); alimenta os planos de mitigação de CTR-02. |

## 3. Lacunas do setor

- sem entradas no Canvas

## 4. Lições propostas

— Nenhuma

> Diagnóstico do lote CTR (5 processos), sem entradas do Canvas Vivo para este subdomínio. Escopos derivados do manual institucional da ATDG (jun/2026) e da prática administrativa geral de controladoria, compliance e gestão de riscos. Playbooks elaborados por inferência (tipo_mudanca minor, status permanece rascunho), com responsável do processo, prazos, formulários, KPIs e normativa específica marcados como lacunas pendentes de validação com a ATDG.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/CTR.json` (diretrizes v1.0)._
