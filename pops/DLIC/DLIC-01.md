---
codigo: DLIC-01
titulo: "Fluxo — Contrato de Aquisição (Licitação)"
versao: "1.1.0"
status: em_validacao
setor_codigo: S03.06-DLIC
setor: "Div. de Licitação"
atualizado_em: "2026-09-03T01:44:33Z"
agente: pop-dlic-01
versao_diretrizes: "1.0"
---

# POP DLIC-01 — Fluxo — Contrato de Aquisição (Licitação)

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **1.1.0** · Status **em_validacao** · Atualizado em 2026-09-03

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Secretaria Administrativa | Div. de Licitação | Formaliza o contrato de aquisição decorrente de licitação homologada: geração do contrato, verificação da regularidade fiscal, publicação no DIOE, emissão de portarias de Gestor e Fiscal, registro no Planejamento, solicitação de empenho e acompanhamento da entrega e das notas fiscais até o recebimento definitivo. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Contratações Públicas | Formalização e execução de contrato de aquisição | core | S03.06-DLIC |

### 0.3 Linguagem ubíqua (glossário do processo)

| Termo | Definição | Sistema |
|---|---|---|
| Empenho | Ato administrativo que reserva o crédito orçamentário para a despesa contratada. | GMS |
| Recebimento definitivo | Confirmação de que os itens adquiridos atendem às especificações do contrato. | — |

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | DLIC-01 |
| Setor | Div. de Licitação (`S03.06-DLIC`) |
| Responsável (função) | Chefe da Divisão de Licitação |
| Periodicidade | Por contrato de aquisição formalizado |
| Subordinação | Secretaria Administrativa |
| Normativa | Lei nº 14.133/2021; normas internas Unioeste |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | 1780963200054 |
| Lacunas abertas | prazo |
| Agente responsável | pop-dlic-01 |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S03_SADM["S03-SADM<br/>Secretaria Administrativa"]
  S01_DG --> S03_SADM
  S03_06_DLIC["S03.06-DLIC<br/>Div. de Licitação"]
  S03_SADM --> S03_06_DLIC
  P["DLIC-01<br/>Fluxo — Contrato de Aquisição (Licitação)"]
  S03_06_DLIC --> P
  V1["Direção Geral"]
  P -. interface .-> V1
  V2["Planejamento"]
  P -. interface .-> V2
  V3["Gestor/Fiscal do contrato"]
  P -. interface .-> V3
  V4["Sec. Financeira/Contabilidade"]
  P -. interface .-> V4
  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747
  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747
  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66
  class S01_DG,S03_SADM,S03_06_DLIC setor
  class P destaque
  class V1,V2,V3,V4 vizinho
```

## 3. Playbook

### 3.1 Gatilho (evento de domínio)

**Homologação da licitação e necessidade de formalizar o contrato de aquisição** — origem: Div. de Licitação (processo licitatório homologado)

### 3.2 Entrada

- Processo licitatório homologado
- Minuta do contrato de aquisição

### 3.3 Passo a passo

| Nº | Ação | Responsável | Sistema | Artefato | Prazo | Evento |
|---|---|---|---|---|---|---|
| 1 | Gerar o contrato de aquisição no GMS | Chefe da Divisão de Licitação | GMS | Contrato de aquisição | A definir | Contrato gerado |
| 2 | Verificar a regularidade fiscal do contratado antes da assinatura | Chefe da Divisão de Licitação | — | Certidões de regularidade fiscal | A definir | Regularidade fiscal verificada |
| 3 | Publicar o contrato assinado no Diário Oficial do Estado (DIOE) | Chefe da Divisão de Licitação | DIOE | Extrato de publicação no DIOE | A definir | Contrato publicado |
| 4 | Emitir e publicar as portarias de Gestor e Fiscal do contrato | Direção Geral | e-Protocolo | Portaria de Gestor; Portaria de Fiscal | A definir | Portarias publicadas |
| 5 | Registrar o contrato e as portarias no Planejamento (GMS) | Planejamento | GMS | Registro do contrato no GMS | A definir | Contrato registrado |
| 6 | Solicitar o empenho à Sec. Financeira/Contabilidade | Gestor do contrato | GMS | Nota de empenho | A definir | Empenho solicitado |
| 7 | Solicitar a aquisição e a entrega dos itens contratados | Gestor do contrato | GMS | Solicitação de entrega | A definir | Entrega solicitada |
| 8 | Acompanhar a entrega e conferir as notas fiscais até o recebimento definitivo | Fiscal do contrato | GMS | Nota fiscal de aquisição | Até o recebimento definitivo dos itens | Recebimento definitivo confirmado |

### 3.4 Saída (entregáveis)

- Contrato de aquisição publicado, registrado e com portarias emitidas
- Itens adquiridos recebidos e notas fiscais conferidas

## 4. Formulários e artefatos (agregados)

| Nome | Tipo | Sistema | Campos-chave | Preenchimento |
|---|---|---|---|---|
| Contrato de aquisição | documento | GMS | nº do contrato, objeto, fornecedor, valor, prazo de entrega | Chefe da Divisão de Licitação |
| Certidões de regularidade fiscal | documento | — | CNPJ, validade, situação | Chefe da Divisão de Licitação |
| Portaria de Gestor do contrato | documento | e-Protocolo | nº da portaria, servidor designado | Direção Geral |
| Portaria de Fiscal do contrato | documento | e-Protocolo | nº da portaria, servidor designado | Direção Geral |
| Nota de empenho | documento | GMS | nº do empenho, valor, elemento de despesa | Gestor do contrato |
| Nota fiscal de aquisição | documento | GMS | nº da NF, itens, quantidade, valor | Fiscal do contrato |

## 5. Decisões, exceções e pontos de atenção

| Decisão | Condição | Sim → | Não → |
|---|---|---|---|
| Contratado está com a regularidade fiscal em dia? | Conferência das certidões de regularidade fiscal do contratado | Prossegue para publicação do contrato no DIOE | Assinatura/execução suspensa até a regularização |

**Pontos de atenção**

- Portarias de Gestor e Fiscal são obrigatórias
- Verificar regularidade fiscal em cada etapa de pagamento
- Registro no GMS e publicação no DIOE
- Aquisição de bens exige recebimento provisório e definitivo conforme o objeto contratado
- Divergência entre a nota de empenho e a nota fiscal deve ser resolvida antes do pagamento

## 6. Contingência

- Se o contratado não apresentar regularidade fiscal, suspender a assinatura até a regularização ou aplicar as sanções cabíveis
- Se a Direção Geral não emitir as portarias em tempo hábil, reiterar o pedido antes do início da execução
- Se a nota fiscal apresentar divergência com o empenho, o Fiscal deve notificar o fornecedor e suspender o pagamento
- Se os itens não forem entregues no prazo contratual, o Fiscal deve notificar o fornecedor e registrar a ocorrência

## 7. Checklist

- ( ) Regularidade fiscal do contratado verificada antes da assinatura
- ( ) Contrato publicado no DIOE
- ( ) Portarias de Gestor e Fiscal emitidas
- ( ) Contrato registrado no Planejamento (GMS)
- ( ) Empenho solicitado e nota de empenho emitida
- ( ) Notas fiscais conferidas pelo Fiscal do contrato

## 8. KPI / Indicadores

| Indicador | Fórmula | Meta | Fonte |
|---|---|---|---|
| Prazo médio entre homologação e assinatura do contrato de aquisição | Data de assinatura − Data de homologação | A definir | GMS |
| Percentual de notas fiscais conferidas sem divergência | (NF sem divergência ÷ total de NF) × 100 | 100% | GMS |

## 9. Mapa de contexto (interfaces inter-setoriais)

| Origem | Relação | Destino | Artefato | Canal |
|---|---|---|---|---|
| Div. de Licitação | informa | Direção Geral | Contrato de aquisição assinado | e-Protocolo |
| Div. de Licitação | fornece | Planejamento | Registro do contrato e portarias | GMS |
| Div. de Licitação | informa | Gestor/Fiscal do contrato | Contrato de aquisição para gestão | e-Protocolo |
| Div. de Licitação | recebe | Sec. Financeira/Contabilidade | Empenho da despesa | GMS |

## 10. Fluxograma (BPMN 2.0 — padrão Anne Bail)

```mermaid
flowchart LR
  subgraph R1["Div. de Licitação"]
    direction LR
    e1(("Homologação da licitação e necessidade de formalizar o contrato"))
    e2["Gerar o contrato de aquisição no GMS"]
    e3["Verificar a regularidade fiscal do contratado"]
    e4{"Contratado está com a regularidade fiscal em dia?"}
    e5(["⏱ Aguardar regularização fiscal do contratado"])
    e6["Publicar o contrato assinado no DIOE"]
  end
  subgraph R2["Direção Geral"]
    direction LR
    e7[["✉ Encaminhar contrato à Direção Geral para portarias"]]
    e8["Emitir e publicar as portarias de Gestor e Fiscal"]
  end
  subgraph R3["Planejamento"]
    direction LR
    e9[["✉ Encaminhar contrato e portarias ao Planejamento"]]
    e10["Registrar o contrato e as portarias no Planejamento (GMS)"]
  end
  subgraph R4["Gestor do contrato"]
    direction LR
    e11[["✉ Informar Gestor do contrato assinado"]]
    e12["Solicitar o empenho à Sec. Financeira/Contabilidade"]
    e13["Solicitar a aquisição e a entrega dos itens"]
  end
  subgraph R5["Fiscal do contrato"]
    direction LR
    e14[["✉ Informar Fiscal do contrato assinado"]]
    e15["Acompanhar a entrega e conferir as notas fiscais"]
    e16((("Recebimento definitivo confirmado")))
  end
  e1 --> e2
  e2 --> e3
  e3 --> e4
  e4 -- Sim --> e6
  e4 -- Não --> e5
  e5 --> e3
  e6 --> e7
  e7 --> e8
  e8 --> e9
  e9 --> e10
  e10 --> e11
  e11 --> e12
  e12 --> e13
  e13 --> e14
  e14 --> e15
  e15 --> e16
  classDef inicio fill:#f3f4f6,stroke:#6b7280,stroke-width:1.5px,color:#374151
  classDef atividade fill:#E6F7F0,stroke:#0B7A4E,stroke-width:2px,color:#0B7A4E
  classDef decisao fill:#FFF4ED,stroke:#C9783A,stroke-width:2px,color:#C9783A
  classDef fim fill:#FDEAEE,stroke:#CC1544,stroke-width:4px,color:#CC1544
  classDef pausa fill:#FDEAEE,stroke:#CC1544,stroke-width:2px,color:#CC1544
  classDef captura fill:#E0F2F8,stroke:#0B4D66,stroke-width:2px,color:#0B4D66
  class e1 inicio
  class e2,e3,e6,e8,e10,e12,e13,e15 atividade
  class e4 decisao
  class e5 pausa
  class e7,e9,e11,e14 captura
  class e16 fim
```

## 11. Especificação BPMN para o Miro

**Raias:** Div. de Licitação · Direção Geral · Planejamento · Gestor do contrato · Fiscal do contrato

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | Homologação da licitação e necessidade de formalizar o contrato | Div. de Licitação |
| e2 | atividade | Gerar o contrato de aquisição no GMS | Div. de Licitação |
| e3 | atividade | Verificar a regularidade fiscal do contratado | Div. de Licitação |
| e4 | decisao | Contratado está com a regularidade fiscal em dia? | Div. de Licitação |
| e5 | pausa | Aguardar regularização fiscal do contratado | Div. de Licitação |
| e6 | atividade | Publicar o contrato assinado no DIOE | Div. de Licitação |
| e7 | captura | Encaminhar contrato à Direção Geral para portarias | Direção Geral |
| e8 | atividade | Emitir e publicar as portarias de Gestor e Fiscal | Direção Geral |
| e9 | captura | Encaminhar contrato e portarias ao Planejamento | Planejamento |
| e10 | atividade | Registrar o contrato e as portarias no Planejamento (GMS) | Planejamento |
| e11 | captura | Informar Gestor do contrato assinado | Gestor do contrato |
| e12 | atividade | Solicitar o empenho à Sec. Financeira/Contabilidade | Gestor do contrato |
| e13 | atividade | Solicitar a aquisição e a entrega dos itens | Gestor do contrato |
| e14 | captura | Informar Fiscal do contrato assinado | Fiscal do contrato |
| e15 | atividade | Acompanhar a entrega e conferir as notas fiscais | Fiscal do contrato |
| e16 | fim | Recebimento definitivo confirmado | Fiscal do contrato |

| De | Para | Rótulo |
|---|---|---|
| e1 | e2 | — |
| e2 | e3 | — |
| e3 | e4 | — |
| e4 | e6 | Sim |
| e4 | e5 | Não |
| e5 | e3 | — |
| e6 | e7 | — |
| e7 | e8 | — |
| e8 | e9 | — |
| e9 | e10 | — |
| e10 | e11 | — |
| e11 | e12 | — |
| e12 | e13 | — |
| e13 | e14 | — |
| e14 | e15 | — |
| e15 | e16 | — |

_Especificação gerada a partir dos passos do POP; 1 raia(s). Revisar decisões e pausas antes de construir no Miro._

## 12. Histórico de versões

| Versão | Data | Autor | Tipo | Mudanças | Fontes |
|---|---|---|---|---|---|
| 0.1.0 | 2026-09-02 | scripts/scaffold_pops.py | patch | Esqueleto inicial gerado deterministicamente a partir das entradas 1780963200054 | 1780963200054 |
| 1.0.0 | 2026-09-03 | agente:construtor-pop (lote C) | major | Passo 1 alterado (acao, responsavel, sistema, artefato, prazo, evento, fontes); Passo 2 alterado (acao, responsavel, sistema, artefato, prazo, evento, fontes); Passo 3 alterado (acao, responsavel, sistema, artefato, prazo, evento, fontes); Passo 4 alterado (acao, responsavel, sistema, artefato, prazo, evento, fontes); Passo 5 alterado (acao, responsavel, sistema, artefato, prazo, evento, fontes); Passo adicionado após 5: Solicitar a aquisição e a entrega dos itens contratados; Passo adicionado após 5: Acompanhar a entrega e conferir as notas fiscais até o recebimento definitivo; Passo adicionado após 1: Verificar a regularidade fiscal do contratado antes da assinatura; entrada_nova: +2; saida_nova: +2; artefatos_novos: +6; decisoes_novas: +1; kpis_novos: +2; mapa_contexto_novo: +4; pontos_atencao_novos: +2; contingencia_nova: +4; checklist_novo: +6; glossario_novo: +2; Campo identificacao.responsavel atualizado; Campo identificacao.periodicidade atualizado; Campo ddd.descricao atualizado; Campo ddd.subdominio atualizado; Campo playbook.gatilho atualizado; Raias adicionadas: Direção Geral, Planejamento, Gestor do contrato, Fiscal do contrato; Elementos BPMN removidos: e1, e2, e3, e4, e5, e6, e7; Elementos BPMN adicionados: 16; Status promovido a em_validacao (≥ 3 passos e responsável definido) | 1780963200054 |
| 1.1.0 | 2026-09-03 | agente:construtor-pop (lote C) | minor | Passo 7 alterado (acao, responsavel, sistema, artefato, prazo, evento, fontes); Passo 8 alterado (acao, responsavel, sistema, artefato, prazo, evento, fontes) | 1780963200054 |

## 13. Validação e aprovação

| Papel | Função / unidade | Data |
|---|---|---|
| Elaboração | ATDG — Assessoria Técnica da Direção Geral | 2026-09-02 |
| Revisão | A definir (responsável do setor) | ___/___/______ |
| Aprovação | Direção Geral do Campus | ___/___/______ |

## 14. Lições incorporadas

- **L-001** — Referir sempre função/cargo; nomes apenas no bloco 13 (Validação), com anuência (LGPD).
- **L-004** — Nunca regenerar POP existente: aplicar patch com changelog, fontes e versão.
- **L-006** — Preservar códigos legados como códigos de processo; não renumerar.
- **L-007** — Referência Externa é benchmark; normativa do POP só cita atos da Unioeste, do Estado do Paraná ou federais aplicáveis.
- **L-002** — Um passo = uma ação; ações compostas viram passos distintos.
- **L-003** — Cada linha do mapa de contexto gera um elemento `captura` no BPMN e um passo na raia de destino.
- **L-005** — No diagnóstico, agrupar versões do mesmo documento e registrar lacuna `versao_documento`.

---
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/DLIC/DLIC-01.pop.json` (diretrizes v1.0)._
