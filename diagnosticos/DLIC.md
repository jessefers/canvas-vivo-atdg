---
id: diag-dlic-20260903
setor_codigo: S03.06-DLIC
data: "2026-09-03T01:59:01Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Div. de Licitação (`S03.06-DLIC`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 4 entrada(s) do Canvas (hash `c2cc11cbeb7d…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Contratações Públicas |
| Subdomínios | Planejamento da contratação (TR, cotações, DDF), Processamento licitatório (edital, sessão pública, homologação), Formalização e execução contratual (portarias, empenho, fiscalização) |
| Contextos vizinhos | Direção Geral, Planejamento (Secretaria Administrativa), Sec. Financeira/Contabilidade, Requisitante (unidade demandante), Gestor/Fiscal do contrato |
| Sistemas | GMS, ComprasNet/PNCP, DIOE, e-Protocolo |
| Normas recorrentes | Lei nº 14.133/2021; normas internas Unioeste |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.76 | DLIC-00 | Playbook — Licitação e Contratos (visão geral) | processo | 1 | 0.85 | 0.7 | 0.85 | 0.35 | gerar_pop | DLIC-00 |
| 0.72 | DLIC-01 | Fluxo — Contrato de Aquisição (Licitação) | processo | 2 | 0.9 | 0.55 | 0.9 | 0.4 | gerar_pop | DLIC-01 |
| 0.72 | DLIC-02 | Fluxo — Contrato de Serviços Contínuos (Licitação) | processo | 2 | 0.9 | 0.55 | 0.9 | 0.4 | gerar_pop | DLIC-02 |
| 0.71 | DLIC-03 | Fluxo — Processo de Licitação | processo | 2 | 0.85 | 0.6 | 0.85 | 0.4 | gerar_pop | DLIC-03 |

### DLIC-00 — Playbook — Licitação e Contratos (visão geral)

Guia consolidado do ciclo de aquisições e contratações, do TR à autorização, licitação, contrato, portarias e acompanhamento da execução.

| Campo | Valor |
|---|---|
| Gatilho | Recebimento de demanda de aquisição ou contratação de serviço |
| Saída | Contrato assinado, publicado no DIOE, registrado no GMS e acompanhado até o encerramento da vigência |
| Atores | Chefe da Divisão de Licitação, Requisitante, Direção Geral, Sec. Financeira/Contabilidade, Planejamento, Gestor/Fiscal do contrato |
| Sistemas | GMS, ComprasNet/PNCP, DIOE, e-Protocolo |
| Artefatos | TR, Cotações, DDF, Edital, Contrato, Portaria de Gestor, Portaria de Fiscal |
| Interfaces | Div. de Licitação ↔ Direção Geral, Div. de Licitação ↔ Sec. Financeira/Contabilidade, Div. de Licitação ↔ Planejamento, Div. de Licitação ↔ Gestor/Fiscal do contrato |
| Evidências | pb-licitacao |
| Lacunas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Justificativa | Playbook geral com passos compostos e sem responsável/artefatos/decisões definidos; alta criticidade e risco de conformidade (Lei nº 14.133/2021) justificam completar o POP. |

### DLIC-01 — Fluxo — Contrato de Aquisição (Licitação)

Formalização do contrato de aquisição decorrente de licitação homologada, da geração à conferência de notas fiscais.

| Campo | Valor |
|---|---|
| Gatilho | Homologação da licitação e necessidade de formalizar o contrato de aquisição |
| Saída | Contrato de aquisição publicado, registrado, com portarias emitidas e itens recebidos |
| Atores | Chefe da Divisão de Licitação, Direção Geral, Planejamento, Gestor do contrato, Fiscal do contrato |
| Sistemas | GMS, DIOE, e-Protocolo |
| Artefatos | Contrato de aquisição, Certidões de regularidade fiscal, Portaria de Gestor, Portaria de Fiscal, Nota de empenho, Nota fiscal de aquisição |
| Interfaces | Div. de Licitação ↔ Direção Geral, Div. de Licitação ↔ Planejamento, Div. de Licitação ↔ Gestor/Fiscal do contrato, Div. de Licitação ↔ Sec. Financeira/Contabilidade |
| Evidências | 1780963200054 |
| Lacunas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Justificativa | Fluxo evidenciado com múltiplos atores (Gestor/Fiscal) mas sem verificação de regularidade fiscal explícita nem KPIs; alto valor contratual justifica priorização. |

### DLIC-02 — Fluxo — Contrato de Serviços Contínuos (Licitação)

Formalização e fiscalização mensal do contrato de serviços contínuos, incluindo decisão de prorrogação ao final da vigência.

| Campo | Valor |
|---|---|
| Gatilho | Homologação da licitação e necessidade de formalizar o contrato de serviços contínuos |
| Saída | Contrato de serviços contínuos publicado, registrado e fiscalizado mensalmente até a prorrogação ou o encerramento |
| Atores | Chefe da Divisão de Licitação, Direção Geral, Planejamento, Fiscal do contrato, Sec. Financeira/Contabilidade |
| Sistemas | GMS, DIOE, e-Protocolo |
| Artefatos | Contrato de serviços contínuos, Certidões de regularidade fiscal, Portaria de Gestor, Portaria de Fiscal, Nota de empenho mensal, Relatório de medição mensal, Termo de prorrogação contratual |
| Interfaces | Div. de Licitação ↔ Direção Geral, Div. de Licitação ↔ Planejamento, Div. de Licitação ↔ Sec. Financeira/Contabilidade, Div. de Licitação ↔ Requisitante |
| Evidências | 1780963200055 |
| Lacunas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Justificativa | Continuidade do serviço depende de decisão tempestiva sobre prorrogação, não evidenciada como decisão formal; risco de solução de continuidade justifica gerar POP completo. |

### DLIC-03 — Fluxo — Processo de Licitação

Condução do processo licitatório do TR à homologação, com duas autorizações da Direção Geral, culminando no encaminhamento ao contrato de aquisição ou de serviços contínuos.

| Campo | Valor |
|---|---|
| Gatilho | Recebimento de memorando de solicitação de aquisição ou contratação de serviço |
| Saída | Licitação homologada e encaminhada à formalização do contrato de aquisição ou de serviços contínuos |
| Atores | Requisitante, Planejamento, Direção Geral, Chefe da Divisão de Licitação, Sec. Financeira/Contabilidade |
| Sistemas | GMS, ComprasNet/PNCP, e-Protocolo |
| Artefatos | Memorando de solicitação, TR, Tabela comparativa de cotações, DDF, Edital de licitação |
| Interfaces | Div. de Licitação ↔ Planejamento, Div. de Licitação ↔ Direção Geral, Div. de Licitação ↔ Sec. Financeira/Contabilidade |
| Evidências | 1780963200056 |
| Lacunas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Justificativa | Processo de origem de toda a contratação, com dois pontos de autorização da Direção Geral não formalizados como decisões; base de todo o ciclo, prioridade máxima. |

## 3. Lacunas do setor

- Nenhum POP de DLIC define responsável (função) no nível de identificação até este lote
- Prazos concretos (dias úteis/marcos normativos) não evidenciados em nenhum fluxo — permanecem 'A definir'
- Ausência de KPIs, contingências e checklist formais em todos os fluxos antes deste lote
- Interface entre DLIC-03 (licitação) e DLIC-01/DLIC-02 (gestão do contrato) não estava explicitada no mapa de contexto

## 4. Lições propostas

| Lição | Regra proposta | Exemplo |
|---|---|---|
| Esqueletos automáticos combinam, em um único passo, ações de responsáveis distintos (ex.: 'TR e cotações; autorização da Direção Geral' mistura Requisitante e Direção Geral). | Ao extrair playbooks/fluxos de texto livre para o esqueleto inicial, separar cada oração ligada por ';' ou por mudança de sujeito em um passo distinto, mesmo antes da geração do POP completo. | DLIC-00 e DLIC-01, passo 1 original |

> Setor com evidências ricas (playbook geral + 3 fluxos específicos). Recomenda-se, em lote futuro, considerar unificar a numeração de decisões de autorização da Direção Geral (presentes em DLIC-00 e DLIC-03) em um glossário institucional único para reduzir duplicidade textual entre POPs correlatos.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/DLIC.json` (diretrizes v1.0)._
