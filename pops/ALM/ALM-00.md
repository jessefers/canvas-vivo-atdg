---
codigo: ALM-00
titulo: "Visão geral — Div. de Almoxarifado"
versao: "0.1.0"
status: rascunho
setor_codigo: S03.04-ALM
setor: "Div. de Almoxarifado"
atualizado_em: "2026-09-02T17:55:54Z"
agente: —
versao_diretrizes: "1.0"
---

# POP ALM-00 — Visão geral — Div. de Almoxarifado

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **0.1.0** · Status **rascunho** · Atualizado em 2026-09-02

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Secretaria Administrativa | Div. de Almoxarifado | Guia operacional do Almoxarifado, do recebimento ao desfazimento de materiais de consumo. Integra o Manual de Gestão (regras) e o Manual de Mapeamento (fluxos e indicadores), com 8 processos em BPMN 2.0. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Suprimentos e Materiais | Visão geral do setor (playbook) | core | S03.04-ALM |

### 0.3 Linguagem ubíqua (glossário do processo)

Herda integralmente o glossário institucional (`diretrizes/09-glossario-institucional.md`); sem termos locais adicionais.

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | ALM-00 |
| Setor | Div. de Almoxarifado (`S03.04-ALM`) |
| Responsável (função) | A definir |
| Periodicidade | A definir |
| Subordinação | Secretaria Administrativa |
| Normativa | Manuais de Gestão e de Mapeamento do Almoxarifado; legislação federal de materiais; normativas TCE-PR |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | pb-almoxarifado |
| Lacunas abertas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Agente responsável | — (não moldado) |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S03_SADM["S03-SADM<br/>Secretaria Administrativa"]
  S01_DG --> S03_SADM
  S03_04_ALM["S03.04-ALM<br/>Div. de Almoxarifado"]
  S03_SADM --> S03_04_ALM
  P["ALM-00<br/>Visão geral — Div. de Almoxarifado"]
  S03_04_ALM --> P
  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747
  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747
  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66
  class S01_DG,S03_SADM,S03_04_ALM setor
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
| 1 | Recebimento de materiais (conferência da NF, quantitativa e qualitativa, lançamento no GMS/ERP) | A definir | — | — | A definir | — |
| 2 | Armazenagem e guarda | A definir | — | — | A definir | — |
| 3 | Distribuição para departamentos | A definir | — | — | A definir | — |
| 4 | Inventário rotativo e geral | A definir | — | — | A definir | — |
| 5 | Conciliação físico-contábil | A definir | — | — | A definir | — |
| 6 | Desfazimento regulamentado de inservíveis | A definir | — | — | A definir | — |
| 7 | Relatórios e prestação de contas | A definir | — | — | A definir | — |

### 3.4 Saída (entregáveis)

— A definir

## 4. Formulários e artefatos (agregados)

— A definir

## 5. Decisões, exceções e pontos de atenção

— Sem decisões registradas

**Pontos de atenção**

- Material só vai ao armazenamento definitivo após registro no sistema
- Conhecimento obrigatório de toda a equipe do setor
- Sujeito a auditorias e conformidade TCE-PR/PRAF

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
  subgraph R1["Div. de Almoxarifado"]
    direction LR
    e1(("A definir"))
    e2["Recebimento de materiais (conferência da NF, quantitativa e qualitati…"]
    e3["Armazenagem e guarda"]
    e4["Distribuição para departamentos"]
    e5["Inventário rotativo e geral"]
    e6["Conciliação físico-contábil"]
    e7["Desfazimento regulamentado de inservíveis"]
    e8["Relatórios e prestação de contas"]
    e9((("Concluído")))
  end
  e1 --> e2
  e2 --> e3
  e3 --> e4
  e4 --> e5
  e5 --> e6
  e6 --> e7
  e7 --> e8
  e8 --> e9
  classDef inicio fill:#f3f4f6,stroke:#6b7280,stroke-width:1.5px,color:#374151
  classDef atividade fill:#E6F7F0,stroke:#0B7A4E,stroke-width:2px,color:#0B7A4E
  classDef decisao fill:#FFF4ED,stroke:#C9783A,stroke-width:2px,color:#C9783A
  classDef fim fill:#FDEAEE,stroke:#CC1544,stroke-width:4px,color:#CC1544
  classDef pausa fill:#FDEAEE,stroke:#CC1544,stroke-width:2px,color:#CC1544
  classDef captura fill:#E0F2F8,stroke:#0B4D66,stroke-width:2px,color:#0B4D66
  class e1 inicio
  class e2,e3,e4,e5,e6,e7,e8 atividade
  class e9 fim
```

## 11. Especificação BPMN para o Miro

**Raias:** Div. de Almoxarifado

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | A definir | Div. de Almoxarifado |
| e2 | atividade | Recebimento de materiais (conferência da NF, quantitativa e qualitativa, lançamento no GMS/ERP) | Div. de Almoxarifado |
| e3 | atividade | Armazenagem e guarda | Div. de Almoxarifado |
| e4 | atividade | Distribuição para departamentos | Div. de Almoxarifado |
| e5 | atividade | Inventário rotativo e geral | Div. de Almoxarifado |
| e6 | atividade | Conciliação físico-contábil | Div. de Almoxarifado |
| e7 | atividade | Desfazimento regulamentado de inservíveis | Div. de Almoxarifado |
| e8 | atividade | Relatórios e prestação de contas | Div. de Almoxarifado |
| e9 | fim | Concluído | Div. de Almoxarifado |

| De | Para | Rótulo |
|---|---|---|
| e1 | e2 | — |
| e2 | e3 | — |
| e3 | e4 | — |
| e4 | e5 | — |
| e5 | e6 | — |
| e6 | e7 | — |
| e7 | e8 | — |
| e8 | e9 | — |

_Especificação gerada a partir dos passos do POP; 1 raia(s). Revisar decisões e pausas antes de construir no Miro._

## 12. Histórico de versões

| Versão | Data | Autor | Tipo | Mudanças | Fontes |
|---|---|---|---|---|---|
| 0.1.0 | 2026-09-02 | scripts/scaffold_pops.py | patch | Esqueleto inicial gerado deterministicamente a partir das entradas pb-almoxarifado | pb-almoxarifado |

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
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/ALM/ALM-00.pop.json` (diretrizes v1.0)._
