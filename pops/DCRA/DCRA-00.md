---
codigo: DCRA-00
titulo: "Visão geral — Div. Circulação, Referência e Acervo"
versao: "0.1.0"
status: rascunho
setor_codigo: S06.01-DCRA
setor: "Div. Circulação, Referência e Acervo"
atualizado_em: "2026-09-02T17:55:55Z"
agente: —
versao_diretrizes: "1.0"
---

# POP DCRA-00 — Visão geral — Div. Circulação, Referência e Acervo

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **0.1.0** · Status **rascunho** · Atualizado em 2026-09-02

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Biblioteca | Div. Circulação, Referência e Acervo | Divisão de Circulação, Referência, Preservação e Conservação do Acervo (Biblioteca). Playbook em construção. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Informação e Acervo | Visão geral do setor (playbook) | suporte | S06.01-DCRA |

### 0.3 Linguagem ubíqua (glossário do processo)

Herda integralmente o glossário institucional (`diretrizes/09-glossario-institucional.md`); sem termos locais adicionais.

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | DCRA-00 |
| Setor | Div. Circulação, Referência e Acervo (`S06.01-DCRA`) |
| Responsável (função) | A definir |
| Periodicidade | A definir |
| Subordinação | Biblioteca |
| Normativa | A definir (regulamentos do Sistema de Bibliotecas da Unioeste) |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | pb-biblioteca-acervo |
| Lacunas abertas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Agente responsável | — (não moldado) |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S06_BIB["S06-BIB<br/>Biblioteca"]
  S01_DG --> S06_BIB
  S06_01_DCRA["S06.01-DCRA<br/>Div. Circulação, Referência e Acervo"]
  S06_BIB --> S06_01_DCRA
  P["DCRA-00<br/>Visão geral — Div. Circulação, Referência e Acervo"]
  S06_01_DCRA --> P
  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747
  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747
  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66
  class S01_DG,S06_BIB,S06_01_DCRA setor
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
| 1 | A documentar: levantar atividades e rotinas da área | A definir | — | — | A definir | — |
| 2 | Mapear fluxos e responsáveis por etapa | A definir | — | — | A definir | — |
| 3 | Identificar normas aplicáveis e pontos de atenção | A definir | — | — | A definir | — |

### 3.4 Saída (entregáveis)

— A definir

## 4. Formulários e artefatos (agregados)

— A definir

## 5. Decisões, exceções e pontos de atenção

— Sem decisões registradas

**Pontos de atenção**

- Área ainda não mapeada — playbook em construção

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
  subgraph R1["Div. Circulação, Referência e Acervo"]
    direction LR
    e1(("A definir"))
    e2["A documentar: levantar atividades e rotinas da área"]
    e3["Mapear fluxos e responsáveis por etapa"]
    e4["Identificar normas aplicáveis e pontos de atenção"]
    e5((("Concluído")))
  end
  e1 --> e2
  e2 --> e3
  e3 --> e4
  e4 --> e5
  classDef inicio fill:#f3f4f6,stroke:#6b7280,stroke-width:1.5px,color:#374151
  classDef atividade fill:#E6F7F0,stroke:#0B7A4E,stroke-width:2px,color:#0B7A4E
  classDef decisao fill:#FFF4ED,stroke:#C9783A,stroke-width:2px,color:#C9783A
  classDef fim fill:#FDEAEE,stroke:#CC1544,stroke-width:4px,color:#CC1544
  classDef pausa fill:#FDEAEE,stroke:#CC1544,stroke-width:2px,color:#CC1544
  classDef captura fill:#E0F2F8,stroke:#0B4D66,stroke-width:2px,color:#0B4D66
  class e1 inicio
  class e2,e3,e4 atividade
  class e5 fim
```

## 11. Especificação BPMN para o Miro

**Raias:** Div. Circulação, Referência e Acervo

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | A definir | Div. Circulação, Referência e Acervo |
| e2 | atividade | A documentar: levantar atividades e rotinas da área | Div. Circulação, Referência e Acervo |
| e3 | atividade | Mapear fluxos e responsáveis por etapa | Div. Circulação, Referência e Acervo |
| e4 | atividade | Identificar normas aplicáveis e pontos de atenção | Div. Circulação, Referência e Acervo |
| e5 | fim | Concluído | Div. Circulação, Referência e Acervo |

| De | Para | Rótulo |
|---|---|---|
| e1 | e2 | — |
| e2 | e3 | — |
| e3 | e4 | — |
| e4 | e5 | — |

_Especificação gerada a partir dos passos do POP; 1 raia(s). Revisar decisões e pausas antes de construir no Miro._

## 12. Histórico de versões

| Versão | Data | Autor | Tipo | Mudanças | Fontes |
|---|---|---|---|---|---|
| 0.1.0 | 2026-09-02 | scripts/scaffold_pops.py | patch | Esqueleto inicial gerado deterministicamente a partir das entradas pb-biblioteca-acervo | pb-biblioteca-acervo |

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
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/DCRA/DCRA-00.pop.json` (diretrizes v1.0)._
