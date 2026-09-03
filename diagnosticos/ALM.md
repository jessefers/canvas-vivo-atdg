---
id: diag-alm-20260903
setor_codigo: S03.04-ALM
data: "2026-09-03T01:29:30Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Div. de Almoxarifado (`S03.04-ALM`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 3 entrada(s) do Canvas (hash `a802d9d68df3…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Suprimentos e Materiais |
| Subdomínios | Recebimento e conferência de materiais, Armazenagem e guarda, Distribuição para departamentos, Inventário rotativo, Inventário geral, Conciliação físico-contábil, Desfazimento de materiais inservíveis, Relatórios e prestação de contas |
| Contextos vizinhos | PRAF, Fornecedor, Div. de Patrimônio e Equipamentos (S03.05-DPAT), Div. de Contabilidade (S04.02-DCONT), Div. de Licitação (S03.06-DLIC), Requisitante/Departamento |
| Sistemas | GMS/ERP, e-Protocolo, planilha de controle |
| Normas recorrentes | Manual de Gestão do Almoxarifado — Materiais de Consumo (Unioeste Foz, obrigatório); Manual de Mapeamento de Processos do Almoxarifado (Unioeste Foz); Legislação federal de materiais (referência genérica nas entradas do Canvas, sem número específico evidenciado); Normativas do TCE-PR (referência genérica nas entradas do Canvas, sem número específico evidenciado); Lei nº 14.133/2021 (Lei de Licitações e Contratos Administrativos), no que for pertinente ao recebimento de materiais decorrentes de contratações públicas e ao desfazimento/alienação de bens |
| Benchmarks (referência externa) | Boas práticas de outras universidades estaduais do Paraná, citadas de forma genérica no Manual de Gestão do Almoxarifado, sem identificação nominal das instituições |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.82 | ALM-01 | Recebimento de Materiais | processo | 1 | 0.95 | 0.9 | 0.85 | 0.15 | gerar_pop | pop-alm-01 |
| 0.73 | ALM-08 | Relatórios e Prestação de Contas | processo | 1 | 0.85 | 0.6 | 0.9 | 0.2 | gerar_pop | pop-alm-08 |
| 0.72 | ALM-02 | Armazenagem | processo | 1 | 0.8 | 0.85 | 0.65 | 0.15 | gerar_pop | pop-alm-02 |
| 0.71 | ALM-00 | Visão geral — Div. de Almoxarifado | processo | 1 | 0.85 | 0.65 | 0.75 | 0.25 | gerar_pop | pop-alm-00 |
| 0.71 | ALM-03 | Distribuição para Departamentos | processo | 1 | 0.8 | 0.85 | 0.6 | 0.15 | gerar_pop | pop-alm-03 |
| 0.71 | ALM-05 | Inventário Geral | processo | 1 | 0.95 | 0.35 | 0.95 | 0.25 | gerar_pop | pop-alm-05 |
| 0.71 | ALM-06 | Conciliação Físico-Contábil | processo | 1 | 0.85 | 0.55 | 0.9 | 0.15 | gerar_pop | pop-alm-06 |
| 0.71 | ALM-07 | Desfazimento de Materiais Inservíveis | processo | 1 | 0.95 | 0.35 | 0.95 | 0.25 | gerar_pop | pop-alm-07 |
| 0.70 | ALM-04 | Inventário Rotativo | processo | 1 | 0.8 | 0.65 | 0.8 | 0.15 | gerar_pop | pop-alm-04 |

### ALM-01 — Recebimento de Materiais

Recebe e confere materiais de consumo (quantitativa e qualitativamente) contra a nota fiscal, lança no GMS/ERP e obtém confirmação da PRAF antes do armazenamento definitivo.

| Campo | Valor |
|---|---|
| Gatilho | Chegada de material acompanhado de nota fiscal, entregue pelo Fornecedor no Almoxarifado |
| Saída | Material conferido e lançado no GMS/ERP, apto ao encaminhamento para armazenagem (ALM-02) |
| Atores | Agente Universitário do Almoxarifado, Chefe da Divisão de Almoxarifado, Fornecedor, PRAF |
| Sistemas | GMS/ERP |
| Artefatos | Nota Fiscal, Termo de recebimento, Formulário de conferência |
| Interfaces | Fornecedor, PRAF, Div. de Licitação (origem contratual da NF) |
| Evidências | pb-almoxarifado, 1780963200000, 1780963200001 |
| Lacunas | passos, responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia, interface_setorial, versao_documento, normativa |
| Justificativa | Processo de maior frequência e criticidade do setor — porta de entrada de todo material de consumo. O manual determina lançamento no GMS/ERP e confirmação da PRAF antes do armazenamento, mas o POP não tem nenhum passo, responsável ou artefato documentado. |

### ALM-08 — Relatórios e Prestação de Contas

Consolida indicadores e resultados dos demais processos do Almoxarifado (recebimento, armazenagem, distribuição, inventários, desfazimento) em relatórios gerenciais e de prestação de contas periódicos.

| Campo | Valor |
|---|---|
| Gatilho | Cronograma de emissão de relatórios (mensal/anual) ou solicitação da PRAF |
| Saída | Relatório de prestação de contas emitido e encaminhado à PRAF |
| Atores | Chefe da Divisão de Almoxarifado, PRAF |
| Sistemas | GMS/ERP, planilha de controle |
| Artefatos | Relatório de prestação de contas |
| Interfaces | PRAF, Div. de Contabilidade (S04.02-DCONT) |
| Evidências | pb-almoxarifado, 1780963200000, 1780963200001 |
| Lacunas | passos, responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia, interface_setorial, versao_documento, normativa |
| Justificativa | Processo de encerramento do ciclo de gestão do Almoxarifado, com alto risco de conformidade perante PRAF/TCE-PR; sem estrutura de indicadores nem passos documentados. |

### ALM-02 — Armazenagem

Organiza, localiza e conserva no espaço físico do Almoxarifado os materiais já conferidos e lançados no GMS/ERP, mantendo correspondência entre estoque físico e registro sistêmico.

| Campo | Valor |
|---|---|
| Gatilho | Material conferido e lançado no GMS/ERP (saída de ALM-01) |
| Saída | Material armazenado, conservado e localizado no mapa de estoque, disponível para distribuição (ALM-03) |
| Atores | Agente Universitário do Almoxarifado, Chefe da Divisão de Almoxarifado |
| Sistemas | GMS/ERP, planilha de controle |
| Artefatos | Mapa de estoque |
| Interfaces | ALM-01 Recebimento de Materiais (entrada), ALM-03 Distribuição para Departamentos (saída) |
| Evidências | pb-almoxarifado, 1780963200000, 1780963200001 |
| Lacunas | passos, responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia, interface_setorial, versao_documento, normativa |
| Justificativa | Responsável pela conservação e localização dos materiais após o recebimento; manual não detalha critérios de organização por classe de material, e o POP está sem qualquer passo documentado. |

### ALM-00 — Visão geral — Div. de Almoxarifado

Guia operacional consolidado do Almoxarifado, do recebimento ao desfazimento de materiais de consumo; organiza os oito processos do setor (ALM-01 a ALM-08) segundo o Manual de Gestão e o Manual de Mapeamento de Processos.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de orientação consolidada sobre o funcionamento do Almoxarifado (integração de servidor, auditoria, revisão de processo) |
| Saída | Visão consolidada dos 8 processos do Almoxarifado, com remissão aos POPs específicos (ALM-01 a ALM-08) |
| Atores | Chefe da Divisão de Almoxarifado, Agente Universitário do Almoxarifado |
| Sistemas | GMS/ERP |
| Artefatos | Manual de Gestão do Almoxarifado, Manual de Mapeamento de Processos do Almoxarifado |
| Interfaces | Requisitante/Departamento, PRAF, Fornecedor, Sec. Financeira/Contabilidade, Div. de Patrimônio |
| Evidências | pb-almoxarifado, 1780963200000, 1780963200001 |
| Lacunas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo, interface_setorial, versao_documento |
| Justificativa | Documento obrigatório (Manual de Gestão) que organiza os demais 8 processos do setor; esqueleto já lista os 8 macroprocessos, mas ainda sem responsável, gatilho, entradas/saídas nem indicadores definidos. |

### ALM-03 — Distribuição para Departamentos

Atende requisições de materiais de consumo dos departamentos do Campus, entrega o material e registra a saída (baixa) no GMS/ERP.

| Campo | Valor |
|---|---|
| Gatilho | Requisição de material de consumo apresentada por um Departamento |
| Saída | Material entregue ao requisitante e baixa registrada no GMS/ERP |
| Atores | Requisitante/Departamento, Agente Universitário do Almoxarifado, Chefe da Divisão de Almoxarifado |
| Sistemas | GMS/ERP |
| Artefatos | Requisição de material, Termo/comprovante de entrega |
| Interfaces | Requisitante/Departamento |
| Evidências | pb-almoxarifado, 1780963200000, 1780963200001 |
| Lacunas | passos, responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia, interface_setorial, versao_documento, normativa |
| Justificativa | Processo de saída de materiais, de alta frequência e visibilidade para os demais setores do Campus; sem critérios documentados de aprovação de requisição nem de limites por departamento. |

### ALM-05 — Inventário Geral

Realiza a contagem física total anual de todo o estoque do Almoxarifado, base da conciliação físico-contábil, da prestação de contas e da auditoria do TCE-PR.

| Campo | Valor |
|---|---|
| Gatilho | Cronograma anual de inventário geral (encerramento do exercício) |
| Saída | Relatório de inventário geral anual consolidado |
| Atores | Chefe da Divisão de Almoxarifado, Agente Universitário do Almoxarifado, PRAF |
| Sistemas | GMS/ERP, planilha de controle |
| Artefatos | Relatório de inventário geral |
| Interfaces | PRAF, Div. de Contabilidade (S04.02-DCONT), TCE-PR (auditoria externa) |
| Evidências | pb-almoxarifado, 1780963200000, 1780963200001 |
| Lacunas | passos, responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia, interface_setorial, versao_documento, normativa |
| Justificativa | Processo anual obrigatório e o mais exposto à auditoria externa (TCE-PR); frequência baixa, mas criticidade e risco de conformidade máximos, sem nenhum passo documentado. |

### ALM-06 — Conciliação Físico-Contábil

Confronta os saldos físicos do Almoxarifado (apurados em ALM-04/ALM-05) com os registros contábeis, apurando e regularizando divergências junto à Contabilidade.

| Campo | Valor |
|---|---|
| Gatilho | Fechamento de inventário rotativo ou geral, ou cronograma de conciliação contábil |
| Saída | Relatório de conciliação físico-contábil sem divergências pendentes |
| Atores | Chefe da Divisão de Almoxarifado, Sec. Financeira/Contabilidade |
| Sistemas | GMS/ERP |
| Artefatos | Relatório de conciliação |
| Interfaces | Sec. Financeira/Contabilidade (Div. de Contabilidade, S04.02-DCONT) |
| Evidências | pb-almoxarifado, 1780963200000, 1780963200001 |
| Lacunas | passos, responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia, interface_setorial, versao_documento, normativa |
| Justificativa | Interliga o controle físico do Almoxarifado ao registro contábil institucional; risco de conformidade elevado (TCE-PR) e nenhuma etapa documentada. |

### ALM-07 — Desfazimento de Materiais Inservíveis

Identifica, classifica e regulariza a baixa de materiais inservíveis, obsoletos ou danificados, por meio de desfazimento regulamentado (doação, alienação ou descarte).

| Campo | Valor |
|---|---|
| Gatilho | Identificação de material inservível (por inventário, avaria ou obsolescência) |
| Saída | Termo de desfazimento emitido e baixa formalizada no GMS/ERP |
| Atores | Chefe da Divisão de Almoxarifado, Div. de Patrimônio, PRAF |
| Sistemas | GMS/ERP, e-Protocolo |
| Artefatos | Termo de desfazimento |
| Interfaces | Div. de Patrimônio (S03.05-DPAT), PRAF |
| Evidências | pb-almoxarifado, 1780963200000, 1780963200001 |
| Lacunas | passos, responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia, interface_setorial, versao_documento, normativa |
| Justificativa | Processo regulamentado com a maior exposição legal e patrimonial do lote; frequência baixa, mas risco de conformidade muito alto, sem qualquer passo documentado. |

### ALM-04 — Inventário Rotativo

Realiza contagens periódicas por amostragem dos itens em estoque para identificar e corrigir divergências entre o físico e o sistema, dentro do checklist de supervisão mensal previsto no Manual de Gestão.

| Campo | Valor |
|---|---|
| Gatilho | Cronograma periódico de contagem (checklist de supervisão mensal) |
| Saída | Relatório de inventário rotativo com divergências apontadas e regularizadas |
| Atores | Agente Universitário do Almoxarifado, Chefe da Divisão de Almoxarifado |
| Sistemas | GMS/ERP, planilha de controle |
| Artefatos | Relatório de inventário |
| Interfaces | Div. de Contabilidade (S04.02-DCONT), quando há divergência relevante |
| Evidências | pb-almoxarifado, 1780963200000, 1780963200001 |
| Lacunas | passos, responsavel, gatilho, entrada, saida, sistema, formulario, prazo, kpi, contingencia, interface_setorial, versao_documento, normativa |
| Justificativa | O Manual de Gestão prevê checklist de supervisão mensal e inventário rotativo, mas o POP não detalha amostragem, critérios de divergência nem responsável pela execução. |

## 3. Lacunas do setor

- Nenhum POP específico (ALM-01 a ALM-08) tem passo a passo documentado; apenas a visão geral (ALM-00) lista os 8 macroprocessos
- Responsável funcional de cada processo não formalizado em identificacao.responsavel (todos em "A definir")
- Mapa de contexto (interfaces com PRAF, Div. de Patrimônio, Div. de Contabilidade, Div. de Licitação e Fornecedores) ausente em todos os POPs
- Indicadores (KPIs) por processo não definidos em nenhum POP do setor
- Planos de contingência e checklists operacionais ausentes em todos os POPs
- Normativa específica (identificacao.normativa) não preenchida nos POPs ALM-01 a ALM-08, apenas em ALM-00
- Nenhum POP passou de status "rascunho"/versão 0.1.0

## 4. Lições propostas

| Lição | Regra proposta | Exemplo |
|---|---|---|
| Playbooks multiprocesso (um POP-00 de visão geral mais N POPs específicos) nascem do scaffold com o macroprocesso já listado em ALM-00, mas os POPs específicos (ALM-01 a ALM-08) não herdam automaticamente gatilho, entrada ou saída aproximados do mesmo manual institucional. | Ao gerar esqueletos de setores com Manual de Mapeamento próprio, herdar de ALM-00 (ou do manual-fonte) ao menos um gatilho e uma saída provisórios por processo específico, reduzindo lacunas de "gatilho"/"saida" já na criação do esqueleto. | ALM-01 a ALM-08 nasceram com playbook.gatilho = "A definir" mesmo com o Manual de Mapeamento descrevendo o fluxo de cada um |
| Processos de baixa frequência mas altíssimo risco de conformidade (inventário geral anual, desfazimento regulamentado) ficam próximos do limiar de priorização porque a frequência pesa tanto quanto o risco na fórmula padrão. | Quando risco_conformidade ≥ 0,90 e há evidência de auditoria externa (TCE-PR/PRAF) nas fontes, considerar piso de prioridade de 0,70 independentemente da frequência, evitando subpriorização de processos anuais/obrigatórios. | ALM-05 (Inventário Geral) e ALM-07 (Desfazimento) — frequência 0,35, mas risco_conformidade 0,95 |

> Diagnóstico elaborado a partir de 3 entradas do Canvas Vivo (playbook do Almoxarifado e os dois Manuais — Mapeamento e Gestão), que descrevem os 8 processos em nível macro (passo a passo geral, responsáveis por função, indicadores e riscos por processo), mas sem o detalhamento operacional linha a linha necessário para o POP. Todos os 9 itens (ALM-00 a ALM-08) atingiram prioridade ≥ 0,70 e recomendação "gerar_pop", coerente com o lote de patches gerado na sequência (Tarefa 2). Maturidade 1 e cobertura baixa (0,15–0,25) refletem o estágio de esqueleto (rascunho v0.1.0) de todos os POPs antes da aplicação dos patches.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/ALM.json` (diretrizes v1.0)._
