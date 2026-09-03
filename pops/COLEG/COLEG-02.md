---
codigo: COLEG-02
titulo: "Gestão acadêmica da coordenação de curso"
versao: "0.1.0"
status: rascunho
setor_codigo: S12-COLEG
setor: "Colegiado de Curso"
atualizado_em: "2026-09-03T02:08:03Z"
agente: pop-coleg-02
versao_diretrizes: "1.12"
---

# POP COLEG-02 — Gestão acadêmica da coordenação de curso

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **0.1.0** · Status **rascunho** · Atualizado em 2026-09-03

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Colegiado de Curso (transversal) | Colegiado de Curso (transversal) | Gestão acadêmica no Academus (planos de ensino, matrícula, notas, horários e distribuição de disciplinas), condução do Colegiado e do NDE e deliberações via e-Protocolo (transferências, segunda chamada, dispensa, exercício domiciliar), conforme o art. 41 do Estatuto e o Regimento de Cursos. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Colegiados e Cursos | Gestão acadêmica da coordenação de curso | core | S12-COLEG |

### 0.3 Linguagem ubíqua (glossário do processo)

Herda integralmente o glossário institucional (`diretrizes/09-glossario-institucional.md`); sem termos locais adicionais.

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | COLEG-02 |
| Setor | Colegiado de Curso (`S12-COLEG`) |
| Responsável (função) | A definir |
| Periodicidade | A definir |
| Subordinação | Direção Geral de Campus |
| Normativa | A definir |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | 1780963200004, 1780963200005, 1780963200006, 1780963200019, 1780963200032 |
| Lacunas abertas | passos, responsavel, entrada, kpi, contingencia, formulario, prazo, normativa, sistema, interface_setorial |
| Agente responsável | pop-coleg-02 |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S12_COLEG["S12-COLEG<br/>Colegiado de Curso (transversal)"]
  S01_DG --> S12_COLEG
  P["COLEG-02<br/>Gestão acadêmica da coordenação de curso"]
  S12_COLEG --> P
  V1["PROGRAD"]
  P -. interface .-> V1
  V2["Direção de Centro"]
  P -. interface .-> V2
  V3["Docentes"]
  P -. interface .-> V3
  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747
  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747
  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66
  class S01_DG,S12_COLEG setor
  class P destaque
  class V1,V2,V3 vizinho
```

## 3. Playbook

### 3.1 Gatilho (evento de domínio)

**Pauta de reunião do Colegiado/NDE, marco do calendário acadêmico ou solicitação de deliberação**

### 3.2 Entrada

— A definir

### 3.3 Passo a passo

— A documentar (nenhum passo registrado)

### 3.4 Saída (entregáveis)

- Gestão acadêmica do período concluída no Academus e deliberações do Colegiado/NDE registradas em ata

## 4. Formulários e artefatos (agregados)

| Nome | Tipo | Sistema | Campos-chave | Preenchimento |
|---|---|---|---|---|
| Pauta e ata do Colegiado/NDE | documento | — | — | — |
| Plano de ensino | documento | — | — | — |
| Ata de deliberação | documento | — | — | — |

## 5. Decisões, exceções e pontos de atenção

— Sem decisões registradas

**Pontos de atenção**

— Nenhum registrado

## 6. Contingência

— A definir

## 7. Checklist

— A definir

## 8. KPI / Indicadores

— A definir

## 9. Mapa de contexto (interfaces inter-setoriais)

| Origem | Relação | Destino | Artefato | Canal |
|---|---|---|---|---|
| Colegiado de Curso | informa | PROGRAD | — | A definir |
| Colegiado de Curso | informa | Direção de Centro | — | A definir |
| Colegiado de Curso | informa | Docentes | — | A definir |

## 10. Fluxograma (BPMN 2.0 — padrão Anne Bail)

```mermaid
flowchart LR
  subgraph R1["Colegiado de Curso"]
    direction LR
    e1(("Pauta de reunião do Colegiado/NDE, marco do calendário acadêmico ou s…"))
    e5((("Gestão acadêmica do período concluída no Academus e deliberações do C…")))
  end
  subgraph R2["PROGRAD"]
    direction LR
    e2[["✉ Informar PROGRAD"]]
  end
  subgraph R3["Direção de Centro"]
    direction LR
    e3[["✉ Informar Direção de Centro"]]
  end
  subgraph R4["Docentes"]
    direction LR
    e4[["✉ Informar Docentes"]]
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
  class e2,e3,e4 captura
  class e5 fim
```

## 11. Especificação BPMN para o Miro

**Raias:** Colegiado de Curso · PROGRAD · Direção de Centro · Docentes

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | Pauta de reunião do Colegiado/NDE, marco do calendário acadêmico ou solicitação de deliberação | Colegiado de Curso |
| e2 | captura | Informar PROGRAD | PROGRAD |
| e3 | captura | Informar Direção de Centro | Direção de Centro |
| e4 | captura | Informar Docentes | Docentes |
| e5 | fim | Gestão acadêmica do período concluída no Academus e deliberações do Colegiado/NDE registradas em ata | Colegiado de Curso |

| De | Para | Rótulo |
|---|---|---|
| e1 | e2 | — |
| e2 | e3 | — |
| e3 | e4 | — |
| e4 | e5 | — |

_Especificação gerada a partir dos passos do POP; 4 raia(s). Revisar decisões e pausas antes de construir no Miro._

## 12. Histórico de versões

| Versão | Data | Autor | Tipo | Mudanças | Fontes |
|---|---|---|---|---|---|
| 0.1.0 | 2026-09-03 | scripts/scaffold_pops.py | patch | Esqueleto gerado a partir do diagnóstico diag-coleg-20260903 (recomendação: gerar_pop) | 1780963200004, 1780963200005, 1780963200006, 1780963200019, 1780963200032 |

## 13. Validação e aprovação

| Papel | Função / unidade | Data |
|---|---|---|
| Elaboração | ATDG — Assessoria Técnica da Direção Geral | 2026-09-03 |
| Revisão | A definir (responsável do setor) | ___/___/______ |
| Aprovação | Direção Geral do Campus | ___/___/______ |

## 14. Lições incorporadas

- **L-001** — Referir sempre função/cargo; nomes apenas no bloco 13 (Validação), com anuência (LGPD).
- **L-004** — Nunca regenerar POP existente: aplicar patch com changelog, fontes e versão.
- **L-006** — Preservar códigos legados como códigos de processo; não renumerar.
- **L-007** — Referência Externa é benchmark; normativa do POP só cita atos da Unioeste, do Estado do Paraná ou federais aplicáveis.

> **Observações:** Esqueleto herdado do diagnóstico diag-coleg-20260903 (processo identificado sem POP); gatilho, saída, artefatos e interfaces provisórios — inferência a validar (lição L-008).

---
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/COLEG/COLEG-02.pop.json` (diretrizes v1.12)._
