---
codigo: DFIN-03
titulo: "Fluxo Despesas Campus Foz — Geral"
versao: "1.0.0"
status: em_validacao
setor_codigo: S04.01-DFIN
setor: "Div. de Finanças"
atualizado_em: "2026-09-03T01:52:53Z"
agente: —
versao_diretrizes: "1.2"
---

# POP DFIN-03 — Fluxo Despesas Campus Foz — Geral

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **1.0.0** · Status **em_validacao** · Atualizado em 2026-09-03

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Secretaria Financeira | Div. de Finanças | Fluxograma geral das despesas do Campus Foz tramitadas via e-Protocolo, abrangendo o conjunto dos pedidos financeiros locais. Arquivo em PDF no formato de imagem/diagrama, sem texto extraível automaticamente. Consolida visualmente a tramitação das despesas; requer leitura visual. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Finanças e Orçamento | Fluxo Despesas Campus Foz — Geral | core | S04.01-DFIN |

### 0.3 Linguagem ubíqua (glossário do processo)

| Termo | Definição | Sistema |
|---|---|---|
| Cadin | Cadastro Informativo de créditos não quitados do setor público federal; consulta obrigatória para verificar pendências do beneficiário antes da concessão de diárias ou despesas de viagem. | Cadin |
| e-Protocolo | Sistema institucional de tramitação eletrônica de processos e documentos da Unioeste, usado para abrir, assinar e encaminhar solicitações de despesa. | e-Protocolo |
| Empenho | Ato administrativo que reserva o crédito orçamentário para a despesa, formalizado pela Div. de Contabilidade após a indicação de fonte e conta pela Secretaria Financeira. | Sistema orçamentário/contábil |
| PRAF | Pró-Reitoria de Administração e Finanças da Unioeste, responsável pelos formulários e procedimentos oficiais de despesas, diárias e viagens. | — |
| Folder/justificativa | Documento que detalha objetivo, roteiro e justificativa institucional da viagem ou despesa solicitada, anexado ao processo no e-Protocolo. | e-Protocolo |

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | DFIN-03 |
| Setor | Div. de Finanças (`S04.01-DFIN`) |
| Responsável (função) | Chefe da Divisão de Finanças |
| Periodicidade | A definir |
| Subordinação | Secretaria Financeira |
| Normativa | Procedimentos de despesas — PRAF/Unioeste; Fluxograma: Fluxos e-Protocolo — Despesas, Campus Foz do Iguaçu (visão geral, documento-fonte em formato imagem) |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | 1780963200042 |
| Lacunas abertas | versao_documento, dados_pessoais_lgpd |
| Agente responsável | — (não moldado) |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S04_SFIN["S04-SFIN<br/>Secretaria Financeira"]
  S01_DG --> S04_SFIN
  S04_01_DFIN["S04.01-DFIN<br/>Div. de Finanças"]
  S04_SFIN --> S04_01_DFIN
  P["DFIN-03<br/>Fluxo Despesas Campus Foz — Geral"]
  S04_01_DFIN --> P
  V1["Servidor/Requisitante"]
  P -. interface .-> V1
  V2["Div. de Contabilidade"]
  P -. interface .-> V2
  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747
  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747
  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66
  class S01_DG,S04_SFIN,S04_01_DFIN setor
  class P destaque
  class V1,V2 vizinho
```

## 3. Playbook

### 3.1 Gatilho (evento de domínio)

**Abertura de qualquer pedido de despesa do Campus Foz no e-Protocolo** — origem: Servidor/Requisitante

### 3.2 Entrada

- Pedido de despesa do Campus Foz (diárias, passagem, hospedagem ou outra) aberto no e-Protocolo

### 3.3 Passo a passo

| Nº | Ação | Responsável | Sistema | Artefato | Prazo | Evento |
|---|---|---|---|---|---|---|
| 1 | Abrir o arquivo do fluxograma geral para leitura visual | Servidor/Requisitante | e-Protocolo | Fluxograma — Despesas, Campus Foz (visão geral) | A definir | Fluxo consultado |
| 2 | Identificar a etapa/tipo de despesa aplicável (diárias, passagem/hospedagem ou outra) | Servidor/Requisitante | e-Protocolo | Formulário de Despesa (Campus Foz) | A definir | Tipo de despesa identificado |
| 3 | Consultar a Secretaria Financeira em caso de dúvida sobre o tipo de despesa | Secretaria Financeira | e-Protocolo | Processo de despesa | A definir | Tipo de despesa reclassificado |
| 4 | Direcionar o processo ao fluxo específico aplicável (Diárias Nacionais, Passagem e Hospedagem ou Procedimento correspondente) | Secretaria Financeira | e-Protocolo | Processo de despesa | A definir | Processo direcionado |
| 5 | Seguir a tramitação local até empenho/pagamento pelo fluxo específico aplicável | Secretaria Financeira | e-Protocolo | Processo de despesa | A definir | Tramitação concluída |
| 6 | Verificar a disponibilidade orçamentária da despesa | Secretaria Financeira | e-Protocolo | Declaração de Disponibilidade Orçamentária e Financeira (DDF) | A definir | Disponibilidade confirmada |
| 7 | Indicar a fonte e a conta orçamentária e encaminhar à Div. de Contabilidade | Secretaria Financeira | e-Protocolo | Processo de despesa | A definir | Processo encaminhado à Contabilidade |
| 8 | Emitir a nota de empenho da despesa | Div. de Contabilidade | Sistema orçamentário/contábil | Nota de Empenho | A definir | Despesa empenhada |

### 3.4 Saída (entregáveis)

- Pedido de despesa direcionado ao fluxo específico aplicável e, ao final, empenhado pela Div. de Contabilidade

## 4. Formulários e artefatos (agregados)

| Nome | Tipo | Sistema | Campos-chave | Preenchimento |
|---|---|---|---|---|
| Formulário de Despesa (Campus Foz) | formulario | e-Protocolo | dados do servidor, tipo de despesa, justificativa, fonte e conta orçamentária | Servidor/Requisitante |
| Declaração de Disponibilidade Orçamentária e Financeira (DDF) | documento | e-Protocolo | fonte de recursos, conta/elemento de despesa, valor disponível | Secretaria Financeira |
| Nota de Empenho | registro | Sistema orçamentário/contábil | número do empenho, credor, valor, fonte de recursos | Div. de Contabilidade |

## 5. Decisões, exceções e pontos de atenção

| Decisão | Condição | Sim → | Não → |
|---|---|---|---|
| Tipo de despesa identificado corretamente? | A etapa aplicável (diárias, passagem/hospedagem ou outra) foi corretamente identificada pelo requisitante | Seguir o fluxo específico correspondente | Consultar a Secretaria Financeira para reclassificação |
| Disponibilidade orçamentária confirmada? | Há saldo na fonte/conta indicada para a despesa | Secretaria Financeira indica fonte/conta e encaminha à Div. de Contabilidade | Devolver ao requisitante ou acionar remanejamento orçamentário |

**Pontos de atenção**

- PDF em imagem — não indexável por texto
- Visão consolidada — usar com os fluxos específicos (diárias, passagem)
- A consulta ao Cadin é obrigatória e deve ser conferida tanto pelo interessado quanto pela Secretaria Financeira antes do encaminhamento à Contabilidade.
- Utilizar sempre os links e formulários oficiais da PRAF vigentes; versões desatualizadas geram devolução do processo.
- Os formulários e a consulta ao Cadin contêm dados pessoais (CPF, nome); observar a LGPD no manuseio, na tramitação e no arquivamento.
- Visão consolidada — usar sempre em conjunto com os fluxos específicos (Diárias Nacionais, Passagem e Hospedagem); documento-fonte em PDF-imagem.

## 6. Contingência

- Se a consulta ao Cadin indicar situação irregular, suspender o processo e notificar o interessado até a regularização.
- Se não houver disponibilidade orçamentária na fonte indicada, devolver o processo ao requisitante ou acionar a Secretaria Financeira para remanejamento antes do empenho.
- Se o e-Protocolo estiver indisponível, registrar a solicitação em meio alternativo (papel/e-mail institucional) e regularizar a tramitação eletrônica assim que o sistema for restabelecido.
- Em caso de urgência da viagem, priorizar a conferência do Cadin e da disponibilidade orçamentária para evitar atraso no empenho.

## 7. Checklist

- ( ) Formulário preenchido com todos os dados obrigatórios do servidor e da viagem/despesa
- ( ) Assinaturas coletadas via e-Protocolo (servidor e chefia imediata)
- ( ) Folder/justificativa anexado
- ( ) Consulta ao Cadin realizada e anexada, com situação regular
- ( ) Disponibilidade orçamentária conferida e fonte/conta indicada
- ( ) Processo encaminhado à Contabilidade com todos os anexos

## 8. KPI / Indicadores

| Indicador | Fórmula | Meta | Fonte |
|---|---|---|---|
| Tempo médio de tramitação da despesa (abertura → empenho) | Σ(data do empenho − data de abertura no e-Protocolo) / nº de processos no período | A definir | e-Protocolo |
| Percentual de processos devolvidos por pendência no Cadin ou na documentação | processos devolvidos / total de processos abertos × 100 | A definir | e-Protocolo |

## 9. Mapa de contexto (interfaces inter-setoriais)

| Origem | Relação | Destino | Artefato | Canal |
|---|---|---|---|---|
| Servidor/Requisitante | fornece | Div. de Finanças | Formulário de despesa e documentação anexa | e-Protocolo |
| Div. de Finanças | fornece | Div. de Contabilidade | Processo de despesa com fonte/conta indicada | e-Protocolo |
| Div. de Contabilidade | informa | Div. de Finanças | Nota de empenho | e-Protocolo |

## 10. Fluxograma (BPMN 2.0 — padrão Anne Bail)

```mermaid
flowchart LR
  subgraph R1["Servidor/Requisitante"]
    direction LR
    e1(("Abertura de pedido de despesa do Campus Foz no e-Protocolo"))
    e2["Abrir o arquivo do fluxograma geral para leitura visual"]
    e3["Identificar o tipo de despesa (diárias, passagem/hospedagem ou outra)"]
    e5["Consultar a Secretaria Financeira para reclassificação do tipo de des…"]
  end
  subgraph R2["Secretaria Financeira"]
    direction LR
    e4{"Tipo de despesa identificado corretamente?"}
    e6[["✉ Seguir o fluxo específico aplicável (DFIN-01/DFIN-02/DFIN-04)"]]
    e7{"Disponibilidade orçamentária confirmada?"}
    e8["Solicitar remanejamento ou devolver ao requisitante"]
    e9((("Processo pendente de disponibilidade orçamentária")))
    e10["Indicar fonte e conta orçamentária"]
  end
  subgraph R3["Div. de Contabilidade"]
    direction LR
    e11[["✉ Encaminhar a Div. de Contabilidade"]]
    e12["Emitir nota de empenho"]
    e13((("Despesa do Campus Foz empenhada")))
  end
  e1 --> e2
  e2 --> e3
  e3 --> e4
  e4 -- Não --> e5
  e5 --> e3
  e4 -- Sim --> e6
  e6 --> e7
  e7 -- Não --> e8
  e8 --> e9
  e7 -- Sim --> e10
  e10 --> e11
  e11 --> e12
  e12 --> e13
  classDef inicio fill:#f3f4f6,stroke:#6b7280,stroke-width:1.5px,color:#374151
  classDef atividade fill:#E6F7F0,stroke:#0B7A4E,stroke-width:2px,color:#0B7A4E
  classDef decisao fill:#FFF4ED,stroke:#C9783A,stroke-width:2px,color:#C9783A
  classDef fim fill:#FDEAEE,stroke:#CC1544,stroke-width:4px,color:#CC1544
  classDef pausa fill:#FDEAEE,stroke:#CC1544,stroke-width:2px,color:#CC1544
  classDef captura fill:#E0F2F8,stroke:#0B4D66,stroke-width:2px,color:#0B4D66
  class e1 inicio
  class e2,e3,e5,e8,e10,e12 atividade
  class e4,e7 decisao
  class e6,e11 captura
  class e9,e13 fim
```

## 11. Especificação BPMN para o Miro

**Raias:** Servidor/Requisitante · Secretaria Financeira · Div. de Contabilidade

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | Abertura de pedido de despesa do Campus Foz no e-Protocolo | Servidor/Requisitante |
| e2 | atividade | Abrir o arquivo do fluxograma geral para leitura visual | Servidor/Requisitante |
| e3 | atividade | Identificar o tipo de despesa (diárias, passagem/hospedagem ou outra) | Servidor/Requisitante |
| e4 | decisao | Tipo de despesa identificado corretamente? | Secretaria Financeira |
| e5 | atividade | Consultar a Secretaria Financeira para reclassificação do tipo de despesa | Servidor/Requisitante |
| e6 | captura | Seguir o fluxo específico aplicável (DFIN-01/DFIN-02/DFIN-04) | Secretaria Financeira |
| e7 | decisao | Disponibilidade orçamentária confirmada? | Secretaria Financeira |
| e8 | atividade | Solicitar remanejamento ou devolver ao requisitante | Secretaria Financeira |
| e9 | fim | Processo pendente de disponibilidade orçamentária | Secretaria Financeira |
| e10 | atividade | Indicar fonte e conta orçamentária | Secretaria Financeira |
| e11 | captura | Encaminhar a Div. de Contabilidade | Div. de Contabilidade |
| e12 | atividade | Emitir nota de empenho | Div. de Contabilidade |
| e13 | fim | Despesa do Campus Foz empenhada | Div. de Contabilidade |

| De | Para | Rótulo |
|---|---|---|
| e1 | e2 | — |
| e2 | e3 | — |
| e3 | e4 | — |
| e4 | e5 | Não |
| e5 | e3 | — |
| e4 | e6 | Sim |
| e6 | e7 | — |
| e7 | e8 | Não |
| e8 | e9 | — |
| e7 | e10 | Sim |
| e10 | e11 | — |
| e11 | e12 | — |
| e12 | e13 | — |

_Especificação gerada a partir dos passos do POP; 1 raia(s). Revisar decisões e pausas antes de construir no Miro._

## 12. Histórico de versões

| Versão | Data | Autor | Tipo | Mudanças | Fontes |
|---|---|---|---|---|---|
| 0.1.0 | 2026-09-02 | scripts/scaffold_pops.py | patch | Esqueleto inicial gerado deterministicamente a partir das entradas 1780963200042 | 1780963200042 |
| 1.0.0 | 2026-09-03 | agente:construtor-pop (lote D1) | major | Passo 1 alterado (acao, responsavel, sistema, artefato, prazo, evento); Passo 2 alterado (acao, responsavel, sistema, artefato, prazo, evento); Passo 3 alterado (acao, responsavel, sistema, artefato, prazo, evento); Passo adicionado após 2: Consultar a Secretaria Financeira em caso de dúvida sobre o tipo de despesa; Passo adicionado após 2: Direcionar o processo ao fluxo específico aplicável (Diárias Nacionais, Passagem; Passo adicionado após 3: Verificar a disponibilidade orçamentária da despesa; Passo adicionado após 3: Indicar a fonte e a conta orçamentária e encaminhar à Div. de Contabilidade; Passo adicionado após 3: Emitir a nota de empenho da despesa; entrada_nova: +1; saida_nova: +1; artefatos_novos: +3; decisoes_novas: +2; kpis_novos: +2; mapa_contexto_novo: +3; pontos_atencao_novos: +4; contingencia_nova: +4; checklist_novo: +6; glossario_novo: +5; normativa_nova: +1; Campo identificacao.responsavel atualizado; Campo playbook.gatilho atualizado; Raias adicionadas: Servidor/Requisitante, Secretaria Financeira, Div. de Contabilidade; Elementos BPMN removidos: e1, e2, e3, e4, e5; Elementos BPMN adicionados: 13; Status promovido a em_validacao (≥ 3 passos e responsável definido) | 1780963200042 |

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

---
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/DFIN/DFIN-03.pop.json` (diretrizes v1.2)._
