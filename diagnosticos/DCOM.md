---
id: diag-dcom-20260903
setor_codigo: S03.10-DCOM
data: "2026-09-03T01:19:45Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Div. de Compras (`S03.10-DCOM`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 5 entrada(s) do Canvas (hash `d571066a65f6…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Contratações Públicas |
| Subdomínios | Contratação direta por dispensa de licitação (emergencial), Contratação direta por inexigibilidade de licitação, Formalização por contrato administrativo, Formalização por Ordem de Compra, Pesquisa de preços e verificação de regularidade fiscal |
| Contextos vizinhos | Planejamento, Direção Geral, Assessoria Jurídica, Sec. Financeira/Contabilidade, Div. de Licitação, Fornecedor/Mercado |
| Sistemas | GMS, e-Protocolo, ComprasNet/PNCP, DIOE |
| Normas recorrentes | Lei nº 14.133/2021 (Lei de Licitações e Contratos Administrativos); Lei nº 14.133/2021, art. 74/75 (hipóteses de inexigibilidade e de dispensa); normas internas Unioeste |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.76 | DCOM-02 | Fluxo — Dispensa Emergencial (com Ordem de Compra) | processo | 1 | 0.9 | 0.6 | 0.85 | 0.45 | gerar_pop | pop-dcom-02 |
| 0.74 | DCOM-01 | Fluxo — Dispensa Emergencial (com Contrato) | processo | 1 | 0.95 | 0.45 | 0.9 | 0.45 | gerar_pop | pop-dcom-01 |
| 0.74 | DCOM-03 | Fluxo — Inexigibilidade (com Contrato) | processo | 1 | 0.9 | 0.45 | 0.95 | 0.45 | gerar_pop | pop-dcom-03 |
| 0.74 | DCOM-04 | Fluxo — Inexigibilidade (com Ordem de Compra) | processo | 1 | 0.85 | 0.55 | 0.9 | 0.45 | gerar_pop | pop-dcom-04 |
| 0.72 | DCOM-00 | Visão geral — Div. de Compras (contratações diretas) | processo | 1 | 0.8 | 0.6 | 0.8 | 0.45 | gerar_pop | pop-dcom-00 |

### DCOM-02 — Fluxo — Dispensa Emergencial (com Ordem de Compra)

Contratação direta por dispensa emergencial de licitação, formalizada por Ordem de Compra, da elaboração do memorando pelo interessado até a emissão e publicação da OC e seu encaminhamento à empresa e ao interessado.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade emergencial de contratação identificada pela unidade requisitante, com previsão de emissão de Ordem de Compra |
| Saída | Ordem de Compra emitida, publicada no DIOE e encaminhada à empresa e ao interessado |
| Atores | Requisitante/Interessado, Planejamento, Direção Geral, Div. de Compras, Assessoria Jurídica, Sec. Financeira/Contabilidade, Fornecedor |
| Sistemas | e-Protocolo, ComprasNet/PNCP, GMS, DIOE |
| Artefatos | Memorando, Cotações de preços, Tabela comparativa, Justificativa de urgência, Certidões de regularidade fiscal, Parecer jurídico, Empenho (GMS), Ordem de Compra, Extrato de publicação DIOE |
| Interfaces | Planejamento, Direção Geral, Assessoria Jurídica, Sec. Financeira/Contabilidade, DIOE/Fornecedor |
| Evidências | 1780963200051 |
| Lacunas | responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia |
| Justificativa | Variante de menor formalidade (OC) tende a ser a mais frequente entre as contratações emergenciais; já mapeada em 6 macropassos (fonte 1780963200051), com lacunas de papéis, sistemas e decisões. |

### DCOM-01 — Fluxo — Dispensa Emergencial (com Contrato)

Contratação direta por dispensa emergencial de licitação, formalizada por contrato administrativo, da elaboração do termo de referência pelo interessado até a assinatura do contrato, a emissão das portarias de Gestor/Fiscal e a publicação no DIOE.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade emergencial de contratação identificada pela unidade requisitante, com previsão de formalização por contrato |
| Saída | Contrato assinado e publicado no DIOE, com portarias de Gestor e Fiscal emitidas |
| Atores | Requisitante/Interessado, Planejamento, Direção Geral, Div. de Compras, Assessoria Jurídica, Sec. Financeira/Contabilidade, Div. de Licitação, Fornecedor |
| Sistemas | e-Protocolo, ComprasNet/PNCP, GMS, DIOE |
| Artefatos | Termo de referência, Cotações de preços, Tabela comparativa, Justificativa de urgência, Certidões de regularidade fiscal, Parecer jurídico, Empenho (GMS), Contrato administrativo, Extrato de publicação DIOE, Portarias de Gestor e Fiscal |
| Interfaces | Planejamento, Direção Geral, Assessoria Jurídica, Sec. Financeira/Contabilidade, Div. de Licitação, DIOE/Fornecedor |
| Evidências | 1780963200050 |
| Lacunas | responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia |
| Justificativa | Dispensa emergencial é hipótese de altíssimo risco de conformidade e de maior exposição a controle externo; fluxo já mapeado em 6 macropassos (fonte 1780963200050), mas com papéis, sistemas, decisões e prazos ainda por definir. |

### DCOM-03 — Fluxo — Inexigibilidade (com Contrato)

Contratação direta por inexigibilidade de licitação (fornecedor exclusivo), formalizada por contrato administrativo, incluindo a publicação do aviso de inexigibilidade, o prazo de 3 dias para impugnação e a assinatura do contrato.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de contratação de fornecedor exclusivo identificada pela unidade requisitante, com previsão de formalização por contrato |
| Saída | Contrato assinado e publicado no DIOE, com portarias de Gestor e Fiscal emitidas |
| Atores | Requisitante/Interessado, Planejamento, Direção Geral, Div. de Compras, Assessoria Jurídica, Sec. Financeira/Contabilidade, Div. de Licitação, Fornecedor |
| Sistemas | e-Protocolo, ComprasNet/PNCP, GMS, DIOE |
| Artefatos | Termo de referência, Cotação do fornecedor exclusivo, Carta de exclusividade, Certidões de regularidade fiscal, Parecer jurídico, DDF, Aviso de inexigibilidade, Contrato administrativo, Extrato de publicação DIOE, Portarias de Gestor e Fiscal |
| Interfaces | Planejamento, Direção Geral, Assessoria Jurídica, Sec. Financeira/Contabilidade, Div. de Licitação, DIOE/Fornecedor |
| Evidências | 1780963200052 |
| Lacunas | responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia |
| Justificativa | Inexigibilidade exige comprovação de exclusividade e é hipótese sujeita a forte escrutínio de controle externo (art. 74); fluxo mapeado em 6 macropassos (fonte 1780963200052), com a pausa de 3 dias e demais papéis/sistemas ainda por formalizar. |

### DCOM-04 — Fluxo — Inexigibilidade (com Ordem de Compra)

Contratação direta por inexigibilidade de licitação (fornecedor exclusivo), formalizada por Ordem de Compra, incluindo a publicação do aviso, o prazo de 3 dias para impugnação, a publicação da inexigibilidade e a emissão da OC pela Div. de Compras.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de contratação de fornecedor exclusivo identificada pela unidade requisitante, com previsão de emissão de Ordem de Compra |
| Saída | Ordem de Compra emitida após a publicação da inexigibilidade |
| Atores | Requisitante/Interessado, Planejamento, Direção Geral, Div. de Compras, Assessoria Jurídica, Sec. Financeira/Contabilidade, Div. de Licitação, Fornecedor |
| Sistemas | e-Protocolo, ComprasNet/PNCP, GMS, DIOE |
| Artefatos | Termo de referência, Cotações de preços, Carta de exclusividade, Certidões de regularidade fiscal, Parecer jurídico, DDF, Aviso de inexigibilidade, Extrato de publicação da inexigibilidade, Ordem de Compra |
| Interfaces | Planejamento, Direção Geral, Assessoria Jurídica, Sec. Financeira/Contabilidade, Div. de Licitação, DIOE/Fornecedor |
| Evidências | 1780963200053 |
| Lacunas | responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia |
| Justificativa | Combina o risco de conformidade da inexigibilidade com a formalização simplificada por Ordem de Compra; fluxo mapeado em 6 macropassos (fonte 1780963200053), com papéis, sistemas e decisões ainda por definir. |

### DCOM-00 — Visão geral — Div. de Compras (contratações diretas)

Guia geral das contratações diretas (dispensa emergencial e inexigibilidade de licitação, com contrato ou com Ordem de Compra), cobrindo a tramitação do pedido do interessado até a emissão do instrumento contratual ou da Ordem de Compra e a publicação no DIOE.

| Campo | Valor |
|---|---|
| Gatilho | Identificação, pela unidade requisitante, de necessidade de contratação direta (dispensa emergencial ou inexigibilidade) |
| Saída | Contrato ou Ordem de Compra formalizado(a) e publicado(a), com portarias de Gestor/Fiscal quando aplicável |
| Atores | Requisitante/Interessado, Planejamento, Direção Geral, Div. de Compras, Assessoria Jurídica, Sec. Financeira/Contabilidade, Div. de Licitação, Fornecedor |
| Sistemas | GMS, e-Protocolo, ComprasNet/PNCP, DIOE |
| Artefatos | TR/memorando, Cotações de preços, Tabela comparativa, Justificativa de urgência, Carta de exclusividade, Certidões de regularidade fiscal, Parecer jurídico, DDF/empenho, Contrato ou Ordem de Compra, Extrato de publicação, Portarias de Gestor/Fiscal |
| Interfaces | Planejamento, Direção Geral, Assessoria Jurídica, Sec. Financeira/Contabilidade, Div. de Licitação, DIOE/Fornecedor |
| Evidências | pb-compras |
| Lacunas | responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia |
| Justificativa | Processo core de alto risco de conformidade (Lei nº 14.133/2021) já mapeado em esqueleto (5 macroetapas, v0.1.0, rascunho); faltam responsáveis, sistemas, artefatos, decisões, KPIs e interfaces setoriais. |

## 3. Lacunas do setor

- Responsável (função) não nomeado para nenhum dos 5 processos de contratação direta
- Sistemas de apoio (GMS, e-Protocolo, ComprasNet/PNCP) não confirmados formalmente passo a passo
- Ausência de KPIs de prazo médio de tramitação da dispensa/inexigibilidade e de taxa de publicação tempestiva no DIOE
- Ausência de checklist e de plano de contingência formalizados para falhas comuns (certidão vencida, impugnação, ausência de carta de exclusividade)
- Periodicidade/SLA de cada etapa não normatizados nos fluxos existentes

## 4. Lições propostas

— Nenhuma

> Diagnóstico do lote DCOM (5 processos de contratações diretas) realizado a partir de fluxogramas institucionais (PDF) já convertidos em esqueletos de POP (v0.1.0, status rascunho). Os 5 processos foram qualificados como 'core', de alto risco de conformidade (Lei nº 14.133/2021), e recomendados para geração de POP completo na Tarefa 2 deste lote.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/DCOM.json` (diretrizes v1.0)._
