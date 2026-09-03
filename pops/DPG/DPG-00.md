---
codigo: DPG-00
titulo: "Visão geral — Div. de Pós-Graduação"
versao: "0.1.0"
status: rascunho
setor_codigo: S05.01-DPG
setor: "Div. de Pós-Graduação"
atualizado_em: "2026-09-02T17:55:55Z"
agente: —
versao_diretrizes: "1.0"
---

# POP DPG-00 — Visão geral — Div. de Pós-Graduação

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **0.1.0** · Status **rascunho** · Atualizado em 2026-09-02

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Coordenação Acadêmica | Div. de Pós-Graduação | Guia dos fluxos de pós-graduação e pesquisa no e-Protocolo (PRPPG): capacitação/afastamento docente, ética no uso de animais (CEUA/CEUAP) e cursos lato e stricto sensu. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Gestão Acadêmica | Visão geral do setor (playbook) | core | S05.01-DPG |

### 0.3 Linguagem ubíqua (glossário do processo)

Herda integralmente o glossário institucional (`diretrizes/09-glossario-institucional.md`); sem termos locais adicionais.

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | DPG-00 |
| Setor | Div. de Pós-Graduação (`S05.01-DPG`) |
| Responsável (função) | A definir |
| Periodicidade | A definir |
| Subordinação | Coordenação Acadêmica |
| Normativa | Resoluções CEPE 029/2013, 071/2021 e 078/2016; Manuais de Fluxos e-Protocolo PRPPG |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | pb-pos-graduacao |
| Lacunas abertas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Agente responsável | — (não moldado) |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S05_CACAD["S05-CACAD<br/>Coordenação Acadêmica"]
  S01_DG --> S05_CACAD
  S05_01_DPG["S05.01-DPG<br/>Div. de Pós-Graduação"]
  S05_CACAD --> S05_01_DPG
  P["DPG-00<br/>Visão geral — Div. de Pós-Graduação"]
  S05_01_DPG --> P
  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747
  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747
  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66
  class S01_DG,S05_CACAD,S05_01_DPG setor
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
| 1 | Identificar o ato (afastamento, proposta/alteração de curso, projeto de ética) | A definir | — | — | A definir | — |
| 2 | Instruir o e-Protocolo conforme o fluxo aplicável | A definir | — | — | A definir | — |
| 3 | Anexar a documentação exigida | A definir | — | — | A definir | — |
| 4 | Encaminhar à PRPPG para deliberação | A definir | — | — | A definir | — |

### 3.4 Saída (entregáveis)

— A definir

## 4. Formulários e artefatos (agregados)

— A definir

## 5. Decisões, exceções e pontos de atenção

— Sem decisões registradas

**Pontos de atenção**

- Observar as Resoluções CEPE aplicáveis (029/2013, 071/2021, 078/2016)
- Projetos com propriedade intelectual tramitam como sigilosos
- Afastamento para o exterior tem requisitos adicionais

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
  subgraph R1["Div. de Pós-Graduação"]
    direction LR
    e1(("A definir"))
    e2["Identificar o ato (afastamento, proposta/alteração de curso, projeto…"]
    e3["Instruir o e-Protocolo conforme o fluxo aplicável"]
    e4["Anexar a documentação exigida"]
    e5["Encaminhar à PRPPG para deliberação"]
    e6((("Concluído")))
  end
  e1 --> e2
  e2 --> e3
  e3 --> e4
  e4 --> e5
  e5 --> e6
  classDef inicio fill:#f3f4f6,stroke:#6b7280,stroke-width:1.5px,color:#374151
  classDef atividade fill:#E6F7F0,stroke:#0B7A4E,stroke-width:2px,color:#0B7A4E
  classDef decisao fill:#FFF4ED,stroke:#C9783A,stroke-width:2px,color:#C9783A
  classDef fim fill:#FDEAEE,stroke:#CC1544,stroke-width:4px,color:#CC1544
  classDef pausa fill:#FDEAEE,stroke:#CC1544,stroke-width:2px,color:#CC1544
  classDef captura fill:#E0F2F8,stroke:#0B4D66,stroke-width:2px,color:#0B4D66
  class e1 inicio
  class e2,e3,e4,e5 atividade
  class e6 fim
```

## 11. Especificação BPMN para o Miro

**Raias:** Div. de Pós-Graduação

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | A definir | Div. de Pós-Graduação |
| e2 | atividade | Identificar o ato (afastamento, proposta/alteração de curso, projeto de ética) | Div. de Pós-Graduação |
| e3 | atividade | Instruir o e-Protocolo conforme o fluxo aplicável | Div. de Pós-Graduação |
| e4 | atividade | Anexar a documentação exigida | Div. de Pós-Graduação |
| e5 | atividade | Encaminhar à PRPPG para deliberação | Div. de Pós-Graduação |
| e6 | fim | Concluído | Div. de Pós-Graduação |

| De | Para | Rótulo |
|---|---|---|
| e1 | e2 | — |
| e2 | e3 | — |
| e3 | e4 | — |
| e4 | e5 | — |
| e5 | e6 | — |

_Especificação gerada a partir dos passos do POP; 1 raia(s). Revisar decisões e pausas antes de construir no Miro._

## 12. Histórico de versões

| Versão | Data | Autor | Tipo | Mudanças | Fontes |
|---|---|---|---|---|---|
| 0.1.0 | 2026-09-02 | scripts/scaffold_pops.py | patch | Esqueleto inicial gerado deterministicamente a partir das entradas pb-pos-graduacao | pb-pos-graduacao |

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
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/DPG/DPG-00.pop.json` (diretrizes v1.0)._
