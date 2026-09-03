---
codigo: DCOM-02
titulo: "Fluxo — Dispensa Emergencial (com Ordem de Compra)"
versao: "0.1.0"
status: rascunho
setor_codigo: S03.10-DCOM
setor: "Div. de Compras"
atualizado_em: "2026-09-02T17:55:54Z"
agente: —
versao_diretrizes: "1.0"
---

# POP DCOM-02 — Fluxo — Dispensa Emergencial (com Ordem de Compra)

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **0.1.0** · Status **rascunho** · Atualizado em 2026-09-02

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Secretaria Administrativa | Div. de Compras | Fluxo da contratação por dispensa emergencial com ordem de compra. O interessado elabora memorando, cotações e tabela comparativa e envia ao Planejamento, que analisa e submete à Direção Geral. Compras faz pesquisa de preços e checa regularidade fiscal; o Jurídico emite parecer; o Financeiro empenha; e Compras emite a Ordem de Compra, publica no DIOE e encaminha à empresa e ao interessado. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Contratações Públicas | Fluxo — Dispensa Emergencial (com Ordem de Compra) | core | S03.10-DCOM |

### 0.3 Linguagem ubíqua (glossário do processo)

Herda integralmente o glossário institucional (`diretrizes/09-glossario-institucional.md`); sem termos locais adicionais.

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | DCOM-02 |
| Setor | Div. de Compras (`S03.10-DCOM`) |
| Responsável (função) | A definir |
| Periodicidade | A definir |
| Subordinação | Secretaria Administrativa |
| Normativa | Lei nº 14.133/2021; normas internas Unioeste |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | 1780963200051 |
| Lacunas abertas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Agente responsável | — (não moldado) |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S03_SADM["S03-SADM<br/>Secretaria Administrativa"]
  S01_DG --> S03_SADM
  S03_10_DCOM["S03.10-DCOM<br/>Div. de Compras"]
  S03_SADM --> S03_10_DCOM
  P["DCOM-02<br/>Fluxo — Dispensa Emergencial (com Ordem de Compra)"]
  S03_10_DCOM --> P
  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747
  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747
  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66
  class S01_DG,S03_SADM,S03_10_DCOM setor
  class P destaque
```

## 3. Playbook

### 3.1 Gatilho (evento de domínio)

**A definir**

### 3.2 Entrada

— A definir

### 3.3 Passo a passo

| Nº | Ação | Responsável | Sistema | Artefato | Prazo | Evento |
|---|---|---|---|---|---|---|
| 1 | Interessado elabora memorando, cotações e tabela comparativa | A definir | — | — | A definir | — |
| 2 | Planejamento analisa e submete à autorização da Direção Geral | A definir | — | — | A definir | — |
| 3 | Compras faz pesquisa de preços e verifica regularidade fiscal | A definir | — | — | A definir | — |
| 4 | Jurídico emite parecer; Financeiro empenha a despesa | A definir | — | — | A definir | — |
| 5 | Compras emite a Ordem de Compra e publica no DIOE | A definir | — | — | A definir | — |
| 6 | Encaminhar OC à empresa e ao interessado | A definir | — | — | A definir | — |

### 3.4 Saída (entregáveis)

— A definir

## 4. Formulários e artefatos (agregados)

— A definir

## 5. Decisões, exceções e pontos de atenção

— Sem decisões registradas

**Pontos de atenção**

- Dispensa emergencial exige justificativa da urgência
- Modalidade com OC (sem contrato formal) — observar limites legais
- Verificar regularidade fiscal antes do empenho

## 6. Contingência

— A definir

## 7. Checklist

— A definir

## 8. KPI / Indicadores

— A definir

## 9. Mapa de contexto (interfaces inter-setoriais)

— Sem interfaces registradas

## 10. Fluxograma (BPMN 2.0 — padrão Anne Bail)

```mermaid
flowchart LR
  subgraph R1["Div. de Compras"]
    direction LR
    e1(("A definir"))
    e2["Interessado elabora memorando, cotações e tabela comparativa"]
    e3["Planejamento analisa e submete à autorização da Direção Geral"]
    e4["Compras faz pesquisa de preços e verifica regularidade fiscal"]
    e5["Jurídico emite parecer; Financeiro empenha a despesa"]
    e6["Compras emite a Ordem de Compra e publica no DIOE"]
    e7["Encaminhar OC à empresa e ao interessado"]
    e8((("Concluído")))
  end
  e1 --> e2
  e2 --> e3
  e3 --> e4
  e4 --> e5
  e5 --> e6
  e6 --> e7
  e7 --> e8
  classDef inicio fill:#f3f4f6,stroke:#6b7280,stroke-width:1.5px,color:#374151
  classDef atividade fill:#E6F7F0,stroke:#0B7A4E,stroke-width:2px,color:#0B7A4E
  classDef decisao fill:#FFF4ED,stroke:#C9783A,stroke-width:2px,color:#C9783A
  classDef fim fill:#FDEAEE,stroke:#CC1544,stroke-width:4px,color:#CC1544
  classDef pausa fill:#FDEAEE,stroke:#CC1544,stroke-width:2px,color:#CC1544
  classDef captura fill:#E0F2F8,stroke:#0B4D66,stroke-width:2px,color:#0B4D66
  class e1 inicio
  class e2,e3,e4,e5,e6,e7 atividade
  class e8 fim
```

## 11. Especificação BPMN para o Miro

**Raias:** Div. de Compras

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | A definir | Div. de Compras |
| e2 | atividade | Interessado elabora memorando, cotações e tabela comparativa | Div. de Compras |
| e3 | atividade | Planejamento analisa e submete à autorização da Direção Geral | Div. de Compras |
| e4 | atividade | Compras faz pesquisa de preços e verifica regularidade fiscal | Div. de Compras |
| e5 | atividade | Jurídico emite parecer; Financeiro empenha a despesa | Div. de Compras |
| e6 | atividade | Compras emite a Ordem de Compra e publica no DIOE | Div. de Compras |
| e7 | atividade | Encaminhar OC à empresa e ao interessado | Div. de Compras |
| e8 | fim | Concluído | Div. de Compras |

| De | Para | Rótulo |
|---|---|---|
| e1 | e2 | — |
| e2 | e3 | — |
| e3 | e4 | — |
| e4 | e5 | — |
| e5 | e6 | — |
| e6 | e7 | — |
| e7 | e8 | — |

_Especificação gerada a partir dos passos do POP; 1 raia(s). Revisar decisões e pausas antes de construir no Miro._

## 12. Histórico de versões

| Versão | Data | Autor | Tipo | Mudanças | Fontes |
|---|---|---|---|---|---|
| 0.1.0 | 2026-09-02 | scripts/scaffold_pops.py | patch | Esqueleto inicial gerado deterministicamente a partir das entradas 1780963200051 | 1780963200051 |

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

---
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/DCOM/DCOM-02.pop.json` (diretrizes v1.0)._
