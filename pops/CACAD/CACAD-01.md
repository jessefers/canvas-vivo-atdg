---
codigo: CACAD-01
titulo: "Fluxos e-Protocolo — Extensão (PROEX)"
versao: "1.0.0"
status: em_validacao
setor_codigo: S05-CACAD
setor: "Coordenação Acadêmica — Geral"
atualizado_em: "2026-09-03T01:52:54Z"
agente: pop-cacad-01
versao_diretrizes: "1.2"
---

# POP CACAD-01 — Fluxos e-Protocolo — Extensão (PROEX)

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **1.0.0** · Status **em_validacao** · Atualizado em 2026-09-03

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Coordenação Acadêmica | Coordenação Acadêmica | Manual da Comissão e-Protocolo com os fluxos da área de Extensão (PROEX). Detalha a abertura de novas atividades de extensão (programas, projetos, cursos e eventos) com e sem recursos financeiros, propostas por docente ou agente universitário, e atividades com fomento externo. Orienta a tramitação correta de cada modalidade no e-Protocolo. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Gestão Acadêmica | Fluxos e-Protocolo — Extensão (PROEX) | core | S05-CACAD |

### 0.3 Linguagem ubíqua (glossário do processo)

| Termo | Definição | Sistema |
|---|---|---|
| e-Protocolo | Sistema institucional de tramitação eletrônica de processos e documentos da Unioeste. | e-Protocolo |
| PROEX | Pró-Reitoria de Extensão da Unioeste, responsável por aprovar e acompanhar as atividades de extensão (programas, projetos, cursos e eventos). | — |
| Fomento externo | Financiamento de atividade de extensão por agência ou instituição externa à Unioeste, que segue fluxo próprio de tramitação no e-Protocolo. | — |
| Atividade de extensão | Programa, projeto, curso ou evento de extensão universitária, com ou sem recursos financeiros, proposto por docente ou agente universitário. | — |

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | CACAD-01 |
| Setor | Coordenação Acadêmica — Geral (`S05-CACAD`) |
| Responsável (função) | Coordenação Acadêmica |
| Periodicidade | A definir |
| Subordinação | Direção Geral de Campus |
| Normativa | Manual de Fluxos e-Protocolo — PROEX/Unioeste; FLUXO_PROEX_-_ATUAL.pdf — Manual da Comissão e-Protocolo (documento-fonte, PROEX) |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | 1780963200039 |
| Lacunas abertas | interface_setorial, versao_documento |
| Agente responsável | pop-cacad-01 |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S05_CACAD["S05-CACAD<br/>Coordenação Acadêmica"]
  S01_DG --> S05_CACAD
  P["CACAD-01<br/>Fluxos e-Protocolo — Extensão (PROEX)"]
  S05_CACAD --> P
  V1["Proponente/Coordenador da atividade"]
  P -. interface .-> V1
  V2["Coordenação Acadêmica"]
  P -. interface .-> V2
  V3["PROEX"]
  P -. interface .-> V3
  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747
  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747
  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66
  class S01_DG,S05_CACAD setor
  class P destaque
  class V1,V2,V3 vizinho
```

## 3. Playbook

### 3.1 Gatilho (evento de domínio)

**Abertura de nova atividade de extensão pelo proponente** — origem: Proponente/Coordenador da atividade

### 3.2 Entrada

- Proposta de atividade de extensão (programa, projeto, curso ou evento), com ou sem recursos, de docente ou agente universitário

### 3.3 Passo a passo

| Nº | Ação | Responsável | Sistema | Artefato | Prazo | Evento |
|---|---|---|---|---|---|---|
| 1 | Classificar a atividade de extensão quanto à modalidade (programa/projeto/curso/evento) e ao proponente (docente ou agente universitário) | Proponente/Coordenador da atividade | e-Protocolo | Formulário de Atividade de Extensão | Antes da abertura do e-Protocolo | Atividade classificada |
| 2 | Confirmar a possibilidade de proposição por agente universitário para a modalidade escolhida, quando aplicável | Proponente/Coordenador da atividade | e-Protocolo | Formulário de Atividade de Extensão | A definir | Proponente confirmado |
| 3 | Verificar se a atividade prevê recursos financeiros e/ou fomento externo | Proponente/Coordenador da atividade | e-Protocolo | Formulário de Atividade de Extensão | A definir | Recursos/fomento verificados |
| 4 | Abrir o e-Protocolo conforme o fluxo da modalidade identificada | Proponente/Coordenador da atividade | e-Protocolo | Processo e-Protocolo | A definir | e-Protocolo aberto |
| 5 | Anexar o projeto/plano de trabalho e a documentação exigida pela modalidade e encaminhar às instâncias previstas | Proponente/Coordenador da atividade | e-Protocolo | Documentação da atividade de extensão | Antes do encaminhamento à Coordenação Acadêmica | Documentação anexada |
| 6 | Encaminhar o processo à Coordenação Acadêmica | Proponente/Coordenador da atividade | e-Protocolo | Processo e-Protocolo | A definir | Processo encaminhado |
| 7 | Acompanhar a aprovação na PROEX | Coordenação Acadêmica | e-Protocolo | Processo e-Protocolo | A definir | Aprovação acompanhada |
| 8 | Registrar o resultado da deliberação da PROEX e comunicar ao proponente | Coordenação Acadêmica | e-Protocolo | Processo e-Protocolo | A definir | Resultado comunicado |

### 3.4 Saída (entregáveis)

- Atividade de extensão aprovada pela PROEX e apta a ser executada

## 4. Formulários e artefatos (agregados)

| Nome | Tipo | Sistema | Campos-chave | Preenchimento |
|---|---|---|---|---|
| Formulário de Atividade de Extensão | formulario | e-Protocolo | modalidade (programa/projeto/curso/evento), proponente, com/sem recursos, fomento externo (S/N) | Proponente/Coordenador da atividade |
| Documentação da atividade de extensão | documento | e-Protocolo | projeto/plano de trabalho, cronograma, público-alvo | Proponente/Coordenador da atividade |

## 5. Decisões, exceções e pontos de atenção

| Decisão | Condição | Sim → | Não → |
|---|---|---|---|
| Proponente é agente universitário (e não docente)? | A atividade é proposta por servidor técnico-administrativo (agente universitário) | Confirmar a possibilidade de proposição por agente universitário para a modalidade escolhida antes de abrir o e-Protocolo | Seguir o fluxo padrão de proposição por docente |
| Atividade com recursos financeiros? | A atividade de extensão prevê captação/uso de recursos financeiros | Instruir o e-Protocolo pelo fluxo de atividade COM recursos (inclui análise orçamentária/financeira) | Instruir o e-Protocolo pelo fluxo de atividade SEM recursos |
| Há fomento externo? | A atividade é financiada por agência de fomento externa à Unioeste | Seguir o fluxo próprio de atividades com fomento externo | Seguir o fluxo padrão da modalidade (programa/projeto/curso/evento) |

**Pontos de atenção**

- Distinguir corretamente atividades com e sem recursos financeiros
- Atividades com fomento externo têm fluxo próprio

## 6. Contingência

- Se o e-Protocolo estiver indisponível, registrar a solicitação em meio alternativo e regularizar a tramitação eletrônica assim que o sistema for restabelecido.
- Se a documentação estiver incompleta, devolver ao proponente/coordenador com a relação de pendências antes de encaminhar à PROEX.
- Em caso de dúvida sobre o fluxo aplicável à modalidade, consultar a Comissão e-Protocolo ou a PROEX antes de tramitar.
- Atividades com fomento externo abertas erroneamente pelo fluxo padrão devem ser reclassificadas e reabertas pelo fluxo próprio de fomento externo.

## 7. Checklist

- ( ) Modalidade da atividade de extensão corretamente identificada (programa, projeto, curso ou evento)
- ( ) Classificação quanto a recursos financeiros e fomento externo definida
- ( ) e-Protocolo aberto conforme o fluxo específico da modalidade
- ( ) Documentação obrigatória anexada
- ( ) Encaminhamento às instâncias na ordem prevista

## 8. KPI / Indicadores

| Indicador | Fórmula | Meta | Fonte |
|---|---|---|---|
| Tempo médio de tramitação (abertura no e-Protocolo → deliberação da PROEX) | Σ(data da deliberação − data de abertura) / nº de processos no período | A definir | e-Protocolo |
| Percentual de processos devolvidos por pendência documental ou fluxo incorreto | processos devolvidos / total de processos abertos × 100 | A definir | e-Protocolo |

## 9. Mapa de contexto (interfaces inter-setoriais)

| Origem | Relação | Destino | Artefato | Canal |
|---|---|---|---|---|
| Proponente/Coordenador da atividade | fornece | Coordenação Acadêmica | Proposta de atividade de extensão | e-Protocolo |
| Coordenação Acadêmica | aprova | PROEX | Processo de extensão instruído | e-Protocolo |
| PROEX | informa | Coordenação Acadêmica | Decisão da PROEX sobre a atividade | e-Protocolo |

## 10. Fluxograma (BPMN 2.0 — padrão Anne Bail)

```mermaid
flowchart LR
  subgraph R1["Proponente/Coordenador da atividade"]
    direction LR
    e1(("Abertura de nova atividade de extensão pelo proponente"))
    e2["Classificar a modalidade da atividade (programa/projeto/curso/evento)"]
    e3{"Proponente é agente universitário (e não docente)?"}
    e4["Confirmar a possibilidade de proposição por agente universitário para…"]
    e5{"Atividade com recursos financeiros?"}
    e6{"Há fomento externo?"}
    e8["Abrir o e-Protocolo conforme o fluxo da modalidade"]
    e9["Anexar o projeto/plano de trabalho conforme a modalidade"]
  end
  subgraph R2["PROEX"]
    direction LR
    e7[["✉ Encaminhar pelo fluxo de fomento externo"]]
    e12[["✉ Encaminhar à PROEX para aprovação"]]
    e13(["⏱ Aguardar deliberação da PROEX"])
  end
  subgraph R3["Coordenação Acadêmica"]
    direction LR
    e10[["✉ Encaminhar à Coordenação Acadêmica"]]
    e11["Encaminhar o processo às instâncias previstas"]
    e14[["✉ Informar resultado à Coordenação Acadêmica"]]
    e15((("Atividade de extensão aprovada pela PROEX")))
  end
  e1 --> e2
  e2 --> e3
  e3 -- Sim --> e4
  e4 --> e5
  e3 -- Não --> e5
  e5 -- Sim --> e6
  e5 -- Não --> e8
  e6 -- Sim --> e7
  e6 -- Não --> e8
  e7 --> e9
  e8 --> e9
  e9 --> e10
  e10 --> e11
  e11 --> e12
  e12 --> e13
  e13 --> e14
  e14 --> e15
  classDef inicio fill:#f3f4f6,stroke:#6b7280,stroke-width:1.5px,color:#374151
  classDef atividade fill:#E6F7F0,stroke:#0B7A4E,stroke-width:2px,color:#0B7A4E
  classDef decisao fill:#FFF4ED,stroke:#C9783A,stroke-width:2px,color:#C9783A
  classDef fim fill:#FDEAEE,stroke:#CC1544,stroke-width:4px,color:#CC1544
  classDef pausa fill:#FDEAEE,stroke:#CC1544,stroke-width:2px,color:#CC1544
  classDef captura fill:#E0F2F8,stroke:#0B4D66,stroke-width:2px,color:#0B4D66
  class e1 inicio
  class e2,e4,e8,e9,e11 atividade
  class e3,e5,e6 decisao
  class e7,e10,e12,e14 captura
  class e13 pausa
  class e15 fim
```

## 11. Especificação BPMN para o Miro

**Raias:** Proponente/Coordenador da atividade · PROEX · Coordenação Acadêmica

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | Abertura de nova atividade de extensão pelo proponente | Proponente/Coordenador da atividade |
| e2 | atividade | Classificar a modalidade da atividade (programa/projeto/curso/evento) | Proponente/Coordenador da atividade |
| e3 | decisao | Proponente é agente universitário (e não docente)? | Proponente/Coordenador da atividade |
| e4 | atividade | Confirmar a possibilidade de proposição por agente universitário para a modalidade escolhida | Proponente/Coordenador da atividade |
| e5 | decisao | Atividade com recursos financeiros? | Proponente/Coordenador da atividade |
| e6 | decisao | Há fomento externo? | Proponente/Coordenador da atividade |
| e7 | captura | Encaminhar pelo fluxo de fomento externo | PROEX |
| e8 | atividade | Abrir o e-Protocolo conforme o fluxo da modalidade | Proponente/Coordenador da atividade |
| e9 | atividade | Anexar o projeto/plano de trabalho conforme a modalidade | Proponente/Coordenador da atividade |
| e10 | captura | Encaminhar à Coordenação Acadêmica | Coordenação Acadêmica |
| e11 | atividade | Encaminhar o processo às instâncias previstas | Coordenação Acadêmica |
| e12 | captura | Encaminhar à PROEX para aprovação | PROEX |
| e13 | pausa | Aguardar deliberação da PROEX | PROEX |
| e14 | captura | Informar resultado à Coordenação Acadêmica | Coordenação Acadêmica |
| e15 | fim | Atividade de extensão aprovada pela PROEX | Coordenação Acadêmica |

| De | Para | Rótulo |
|---|---|---|
| e1 | e2 | — |
| e2 | e3 | — |
| e3 | e4 | Sim |
| e4 | e5 | — |
| e3 | e5 | Não |
| e5 | e6 | Sim |
| e5 | e8 | Não |
| e6 | e7 | Sim |
| e6 | e8 | Não |
| e7 | e9 | — |
| e8 | e9 | — |
| e9 | e10 | — |
| e10 | e11 | — |
| e11 | e12 | — |
| e12 | e13 | — |
| e13 | e14 | — |
| e14 | e15 | — |

_Especificação gerada a partir dos passos do POP; 1 raia(s). Revisar decisões e pausas antes de construir no Miro._

## 12. Histórico de versões

| Versão | Data | Autor | Tipo | Mudanças | Fontes |
|---|---|---|---|---|---|
| 0.1.0 | 2026-09-02 | scripts/scaffold_pops.py | patch | Esqueleto inicial gerado deterministicamente a partir das entradas 1780963200039 | 1780963200039 |
| 1.0.0 | 2026-09-03 | agente:construtor-pop (lote D1) | major | Passo 1 alterado (acao, responsavel, sistema, artefato, prazo, evento); Passo 2 alterado (acao, responsavel, sistema, artefato, prazo, evento); Passo 3 alterado (acao, responsavel, sistema, artefato, prazo, evento); Passo 4 alterado (acao, responsavel, sistema, artefato, prazo, evento); Passo adicionado após 1: Confirmar a possibilidade de proposição por agente universitário para a modalida; Passo adicionado após 1: Verificar se a atividade prevê recursos financeiros e/ou fomento externo; Passo adicionado após 3: Encaminhar o processo à Coordenação Acadêmica; Passo adicionado após 4: Registrar o resultado da deliberação da PROEX e comunicar ao proponente; entrada_nova: +1; saida_nova: +1; artefatos_novos: +2; decisoes_novas: +3; kpis_novos: +2; mapa_contexto_novo: +3; pontos_atencao_novos: +2; contingencia_nova: +4; checklist_novo: +5; glossario_novo: +4; normativa_nova: +1; Campo identificacao.responsavel atualizado; Campo playbook.gatilho atualizado; Raias adicionadas: Proponente/Coordenador da atividade, PROEX, Coordenação Acadêmica; Elementos BPMN removidos: e1, e2, e3, e4, e5, e6; Elementos BPMN adicionados: 15; Status promovido a em_validacao (≥ 3 passos e responsável definido) | 1780963200039 |

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
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/CACAD/CACAD-01.pop.json` (diretrizes v1.2)._
