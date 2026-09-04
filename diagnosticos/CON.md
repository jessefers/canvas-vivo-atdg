---
id: diag-con-20260903
setor_codigo: S02.01-CON
data: "2026-09-03T02:02:00Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — ATDG — Assessoria Técnica da Direção Geral (`S02.01-CON`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 0 entrada(s) do Canvas (hash `e3b0c44298fc…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Convênios, Parcerias e Captação |
| Subdomínios | Instrução de Convênio, Celebração de Convênio, Execução de Convênio, Prestação de Contas de Convênio, Encerramento de Convênio |
| Contextos vizinhos | Direção Geral do Campus, Setor demandante, SETI, TCE-PR |
| Sistemas | e-Protocolo, OneDrive ATDG |
| Normas recorrentes | Lei nº 14.133/2021 (Lei de Licitações e Contratos Administrativos), no que for pertinente à formalização de convênios |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.72 | CON-04 | Prestação de Contas de Convênio | processo | 0 | 0.9 | 0.4 | 0.9 | 0.15 | gerar_pop | pop-con-04 |
| 0.67 | CON-01 | Instrução de Convênio | processo | 0 | 0.8 | 0.5 | 0.7 | 0.18 | coletar_mais | pop-con-01 |
| 0.67 | CON-03 | Execução de Convênio | processo | 0 | 0.75 | 0.55 | 0.7 | 0.18 | coletar_mais | pop-con-03 |
| 0.66 | CON-02 | Celebração de Convênio | processo | 0 | 0.8 | 0.45 | 0.7 | 0.15 | coletar_mais | pop-con-02 |
| 0.54 | CON-05 | Encerramento de Convênio | processo | 0 | 0.6 | 0.3 | 0.6 | 0.15 | coletar_mais | pop-con-05 |

### CON-04 — Prestação de Contas de Convênio

Prestação de Contas de Convênio — financeira e técnica, TCE-PR.

| Campo | Valor |
|---|---|
| Gatilho | Encerramento da vigência ou do objeto do convênio, exigindo prestação de contas |
| Saída | Prestação de contas aprovada e disponível ao TCE-PR |
| Atores | Setor demandante, Assessoria Técnica da Direção Geral (ATDG), Direção Geral do Campus, TCE-PR |
| Sistemas | e-Protocolo |
| Artefatos | Prestação de contas financeira e técnica, Planilha de conferência financeira |
| Interfaces | Direção Geral do Campus, TCE-PR |
| Evidências | — |
| Lacunas | responsavel, kpi, formulario, prazo, normativa |
| Justificativa | Processo de maior risco de conformidade do subdomínio (TCE-PR); sem entradas do Canvas, playbook construído por inferência (minor, rascunho), prioridade alta para validação com a ATDG. |

### CON-01 — Instrução de Convênio

Instrução de Convênio — pré-aprovação, documentação e encaminhamento à SETI.

| Campo | Valor |
|---|---|
| Gatilho | Manifestação de interesse do setor demandante em celebrar convênio, ou publicação de edital/chamamento que enseje convênio |
| Saída | Processo de convênio instruído, pré-aprovado e encaminhado à SETI |
| Atores | Setor demandante, Assessoria Técnica da Direção Geral (ATDG), Direção Geral do Campus, SETI |
| Sistemas | e-Protocolo |
| Artefatos | Plano de trabalho, Minuta de convênio |
| Interfaces | Direção Geral do Campus, SETI |
| Evidências | — |
| Lacunas | responsavel, kpi, formulario, prazo, normativa |
| Justificativa | Escopo evidenciado apenas pelo manual institucional da ATDG (jun/2026), sem entradas do Canvas; playbook construído por inferência (minor, rascunho), pendente de validação da ATDG. |

### CON-03 — Execução de Convênio

Execução de Convênio — acompanhamento e relatórios parciais.

| Campo | Valor |
|---|---|
| Gatilho | Convênio celebrado e vigente, com execução do objeto em curso |
| Saída | Relatório parcial de execução aprovado e acompanhamento atualizado |
| Atores | Setor demandante, Assessoria Técnica da Direção Geral (ATDG), SETI |
| Sistemas | e-Protocolo, OneDrive ATDG |
| Artefatos | Relatório parcial de execução, Registro de acompanhamento do convênio |
| Interfaces | SETI |
| Evidências | — |
| Lacunas | responsavel, kpi, formulario, prazo, normativa |
| Justificativa | Sem entradas do Canvas; playbook construído por inferência a partir do escopo do manual institucional (minor, rascunho). |

### CON-02 — Celebração de Convênio

Celebração de Convênio — assinaturas, publicação e registro.

| Campo | Valor |
|---|---|
| Gatilho | Aprovação da minuta de convênio pela SETI recebida |
| Saída | Convênio assinado, publicado e registrado |
| Atores | Assessoria Técnica da Direção Geral (ATDG), Direção Geral do Campus, SETI, Setor demandante |
| Sistemas | e-Protocolo, OneDrive ATDG |
| Artefatos | Convênio (instrumento assinado), Registro de convênios |
| Interfaces | Direção Geral do Campus, SETI, Setor demandante |
| Evidências | — |
| Lacunas | responsavel, kpi, formulario, prazo, normativa |
| Justificativa | Sem entradas do Canvas; playbook construído por inferência a partir do escopo do manual institucional (minor, rascunho). |

### CON-05 — Encerramento de Convênio

Encerramento de Convênio — baixa, arquivo e lições aprendidas.

| Campo | Valor |
|---|---|
| Gatilho | Prestação de contas aprovada e convênio pronto para baixa e arquivamento |
| Saída | Convênio baixado e arquivado, com lições aprendidas registradas |
| Atores | Assessoria Técnica da Direção Geral (ATDG), Setor demandante, Direção Geral do Campus |
| Sistemas | e-Protocolo, OneDrive ATDG |
| Artefatos | Registro de lições aprendidas do convênio, Processo de convênio arquivado |
| Interfaces | Setor demandante, Direção Geral do Campus |
| Evidências | — |
| Lacunas | responsavel, kpi, formulario, prazo, normativa |
| Justificativa | Sem entradas do Canvas; playbook construído por inferência a partir do escopo do manual institucional (minor, rascunho). |

## 3. Lacunas do setor

- sem entradas no Canvas

## 4. Lições propostas

— Nenhuma

> Diagnóstico do lote CON (5 processos), sem entradas do Canvas Vivo para este subdomínio. Escopos derivados do manual institucional da ATDG (jun/2026) e da prática administrativa geral de convênios em universidades estaduais do Paraná. Playbooks elaborados por inferência (tipo_mudanca minor, status permanece rascunho), com responsável do processo, prazos, formulários, KPIs e normativa específica marcados como lacunas pendentes de validação com a ATDG.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/CON.json` (diretrizes v1.0)._
