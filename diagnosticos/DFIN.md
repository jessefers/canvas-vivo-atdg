---
id: diag-dfin-20260903
setor_codigo: S04.01-DFIN
data: "2026-09-03T01:41:28Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Div. de Finanças (`S04.01-DFIN`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 7 entrada(s) do Canvas (hash `8bfecfc6f37d…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Finanças e Orçamento |
| Subdomínios | Execução de despesas do campus (diárias, passagens, hospedagem), Tramitação de despesas no e-Protocolo até o empenho |
| Contextos vizinhos | Div. de Contabilidade, Secretaria Financeira, Direção Geral de Campus, PRAF (Pró-Reitoria de Administração e Finanças) |
| Sistemas | e-Protocolo, Cadin |
| Normas recorrentes | Procedimentos PRAF/Secretaria Financeira; Fluxos de despesas do Campus Foz (e-Protocolo) |
| Benchmarks (referência externa) | Descrição de subprocesso financeiro — Contas a Pagar (Hospital Padre Germano Lauck, 2018) — referência metodológica externa, não norma da Unioeste, Fluxograma financeiro genérico (documento de referência externa) — adaptado apenas como modelo de representação visual |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.74 | DFIN-04 | Procedimento — Diárias Nacionais | processo | 2 | 0.8 | 0.7 | 0.85 | 0.65 | gerar_pop | DFIN-04 |
| 0.71 | DFIN-01 | Fluxo Despesas Campus Foz — Diárias Nacionais | processo | 2 | 0.8 | 0.7 | 0.8 | 0.5 | gerar_pop | DFIN-01 |
| 0.70 | DFIN-00 | Visão geral — execução de despesas | processo | 2 | 0.8 | 0.6 | 0.8 | 0.6 | gerar_pop | DFIN-00 |
| 0.67 | DFIN-02 | Fluxo Despesas Campus Foz — Passagem e Hospedagem | processo | 2 | 0.75 | 0.6 | 0.75 | 0.5 | coletar_mais | DFIN-02 |
| 0.59 | DFIN-03 | Fluxo Despesas Campus Foz — Geral | processo | 1 | 0.6 | 0.5 | 0.6 | 0.45 | coletar_mais | DFIN-03 |

### DFIN-04 — Procedimento — Diárias Nacionais

Procedimento textual detalhado de solicitação de diárias nacionais, da abertura à indicação de fonte/conta pela Secretaria Financeira e ao empenho pela Contabilidade.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de viagem a serviço no território nacional |
| Saída | Processo de diárias nacionais encaminhado à Contabilidade com fonte/conta indicada |
| Atores | Servidor/Requisitante, Chefia imediata, Secretaria Financeira, Div. de Contabilidade |
| Sistemas | e-Protocolo, Cadin |
| Artefatos | Formulário de despesa, Folder/justificativa, Consulta Cadin, Declaração de Disponibilidade Orçamentária e Financeira |
| Interfaces | Div. de Contabilidade, Secretaria Financeira |
| Evidências | 1780963200049 |
| Lacunas | sistema, dados_pessoais_lgpd |
| Justificativa | Procedimento mais detalhado e acionável do conjunto (inclui consulta obrigatória ao Cadin e verificação orçamentária); maior cobertura textual. |

### DFIN-01 — Fluxo Despesas Campus Foz — Diárias Nacionais

Fluxograma específico do Campus Foz para diárias nacionais no e-Protocolo (documento-fonte em imagem).

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de viagem a serviço no território nacional |
| Saída | Processo de diárias nacionais empenhado |
| Atores | Servidor/Requisitante, Chefia imediata, Secretaria Financeira, Div. de Contabilidade |
| Sistemas | e-Protocolo, Cadin |
| Artefatos | Formulário de despesa, Folder/justificativa, Consulta Cadin, Declaração de Disponibilidade Orçamentária e Financeira |
| Interfaces | Div. de Contabilidade, Secretaria Financeira |
| Evidências | 1780963200040 |
| Lacunas | sistema, versao_documento |
| Justificativa | Fluxo específico de alta frequência (viagens a serviço); documento-fonte é imagem, sem texto extraível — cobertura parcial. |

### DFIN-00 — Visão geral — execução de despesas

Guia consolidado da execução de despesas do campus (diárias, passagens, hospedagem e pagamentos), com tramitação no e-Protocolo até o empenho.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de despesa do servidor (diária, passagem, hospedagem ou pagamento) |
| Saída | Despesa empenhada pela Div. de Contabilidade |
| Atores | Servidor/Requisitante, Chefia imediata, Secretaria Financeira, Div. de Contabilidade |
| Sistemas | e-Protocolo, Cadin |
| Artefatos | Formulário de despesa, Folder/justificativa, Consulta Cadin, Declaração de Disponibilidade Orçamentária e Financeira |
| Interfaces | Div. de Contabilidade, Secretaria Financeira |
| Evidências | pb-financas |
| Lacunas | sistema, interface_setorial |
| Justificativa | Consolida os fluxos específicos (diárias, passagem/hospedagem) já evidenciados; alta criticidade orçamentária e risco de conformidade (Cadin, disponibilidade). |

### DFIN-02 — Fluxo Despesas Campus Foz — Passagem e Hospedagem

Fluxograma específico do Campus Foz para passagem e hospedagem no e-Protocolo (documento-fonte em imagem).

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de passagem e/ou hospedagem para viagem a serviço |
| Saída | Processo de passagem/hospedagem empenhado |
| Atores | Servidor/Requisitante, Chefia imediata, Secretaria Financeira, Div. de Contabilidade |
| Sistemas | e-Protocolo, Cadin |
| Artefatos | Formulário de despesa, Folder/justificativa, Consulta Cadin, Declaração de Disponibilidade Orçamentária e Financeira |
| Interfaces | Div. de Contabilidade, Secretaria Financeira |
| Evidências | 1780963200041 |
| Lacunas | sistema, versao_documento |
| Justificativa | Fluxo específico correlato às diárias; mesma limitação de cobertura por ser documento-imagem. |

### DFIN-03 — Fluxo Despesas Campus Foz — Geral

Fluxograma geral consolidado das despesas do Campus Foz tramitadas via e-Protocolo (documento-fonte em imagem).

| Campo | Valor |
|---|---|
| Gatilho | Abertura de qualquer pedido de despesa do Campus Foz no e-Protocolo |
| Saída | Pedido de despesa direcionado ao fluxo específico aplicável |
| Atores | Servidor/Requisitante, Chefia imediata, Secretaria Financeira, Div. de Contabilidade |
| Sistemas | e-Protocolo, Cadin |
| Artefatos | Formulário de despesa, Folder/justificativa, Consulta Cadin, Declaração de Disponibilidade Orçamentária e Financeira |
| Interfaces | Div. de Contabilidade, Secretaria Financeira |
| Evidências | 1780963200042 |
| Lacunas | sistema, versao_documento |
| Justificativa | Visão consolidada de baixo detalhamento próprio (aponta para os fluxos específicos); recomenda-se manter como POP roteador. |

## 3. Lacunas do setor

- Responsável nominal (função) da Div. de Finanças ainda não formalizado no POP
- Prazos (SLA) de análise da Secretaria Financeira e de empenho pela Contabilidade não evidenciados em dias

## 4. Lições propostas

| Lição | Regra proposta | Exemplo |
|---|---|---|
| Documentos de referência de outras instituições (ex.: Hospital Padre Germano Lauck) foram anexados ao acervo do setor como exemplo metodológico, sem detalhar o processo real da Unioeste. | Registrar documentos de outras instituições apenas em ecossistema.benchmarks do diagnóstico, nunca como evidência de processo próprio nem como normativa institucional. | DFIN — entradas 1780963200036 e 1780963200037 |

> Os fluxogramas do Campus Foz (DFIN-01/02/03) são arquivos em PDF no formato de imagem, sem texto extraível; a cobertura textual desses processos permanece parcial até nova leitura visual/transcrição. DFIN-02 e DFIN-03 pontuam 'coletar_mais' pela fórmula (prioridade < 0,70), mas, por integrarem o esqueleto já existente do Lote D1, seus POPs são completados nesta leva conforme escopo definido; a recomendação numérica orienta o aprofundamento futuro (nova leitura visual dos fluxogramas).

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/DFIN.json` (diretrizes v1.0)._
