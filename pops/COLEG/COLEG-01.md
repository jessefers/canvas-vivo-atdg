---
codigo: COLEG-01
titulo: "Rotinas do Agente Universitário do Colegiado"
versao: "0.1.0"
status: rascunho
setor_codigo: S12-COLEG
setor: "Colegiado de Curso"
atualizado_em: "2026-09-03T02:08:03Z"
agente: pop-coleg-01
versao_diretrizes: "1.12"
---

# POP COLEG-01 — Rotinas do Agente Universitário do Colegiado

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **0.1.0** · Status **rascunho** · Atualizado em 2026-09-03

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Colegiado de Curso (transversal) | Colegiado de Curso (transversal) | Comunicação e atendimento a discentes, docentes e concedentes, gestão de documentos e protocolo (e-Protocolo) e apoio acadêmico às coordenações de curso, estágio e TCC, exercidos pelo Agente Universitário do Colegiado. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Colegiados e Cursos | Rotinas do Agente Universitário do Colegiado | suporte | S12-COLEG |

### 0.3 Linguagem ubíqua (glossário do processo)

Herda integralmente o glossário institucional (`diretrizes/09-glossario-institucional.md`); sem termos locais adicionais.

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | COLEG-01 |
| Setor | Colegiado de Curso (`S12-COLEG`) |
| Responsável (função) | A definir |
| Periodicidade | A definir |
| Subordinação | Direção Geral de Campus |
| Normativa | A definir |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | 1780963200002, 1780963200003, 1780963200018 |
| Lacunas abertas | passos, responsavel, entrada, kpi, contingencia, formulario, prazo, normativa, sistema |
| Agente responsável | pop-coleg-01 |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S12_COLEG["S12-COLEG<br/>Colegiado de Curso (transversal)"]
  S01_DG --> S12_COLEG
  P["COLEG-01<br/>Rotinas do Agente Universitário do Colegiado"]
  S12_COLEG --> P
  V1["Discentes e docentes"]
  P -. interface .-> V1
  V2["Concedentes de estágio"]
  P -. interface .-> V2
  V3["Coordenações de curso, estágio e TCC"]
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

**Solicitação de discente, docente, concedente ou coordenação que demande atendimento, protocolo ou apoio acadêmico**

### 3.2 Entrada

— A definir

### 3.3 Passo a passo

— A documentar (nenhum passo registrado)

### 3.4 Saída (entregáveis)

- Atendimento realizado, documento protocolado e apoio acadêmico prestado às coordenações

## 4. Formulários e artefatos (agregados)

| Nome | Tipo | Sistema | Campos-chave | Preenchimento |
|---|---|---|---|---|
| Protocolo/registro de atendimento | documento | — | — | — |

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
| Colegiado de Curso | informa | Discentes e docentes | — | A definir |
| Colegiado de Curso | informa | Concedentes de estágio | — | A definir |
| Colegiado de Curso | informa | Coordenações de curso, estágio e TCC | — | A definir |

## 10. Fluxograma (BPMN 2.0 — padrão Anne Bail)

```mermaid
flowchart LR
  subgraph R1["Colegiado de Curso"]
    direction LR
    e1(("Solicitação de discente, docente, concedente ou coordenação que deman…"))
    e5((("Atendimento realizado, documento protocolado e apoio acadêmico presta…")))
  end
  subgraph R2["Discentes e docentes"]
    direction LR
    e2[["✉ Informar Discentes e docentes"]]
  end
  subgraph R3["Concedentes de estágio"]
    direction LR
    e3[["✉ Informar Concedentes de estágio"]]
  end
  subgraph R4["Coordenações de curso, estágio e TCC"]
    direction LR
    e4[["✉ Informar Coordenações de curso, estágio e TCC"]]
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

**Raias:** Colegiado de Curso · Discentes e docentes · Concedentes de estágio · Coordenações de curso, estágio e TCC

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | Solicitação de discente, docente, concedente ou coordenação que demande atendimento, protocolo ou apoio acadêmico | Colegiado de Curso |
| e2 | captura | Informar Discentes e docentes | Discentes e docentes |
| e3 | captura | Informar Concedentes de estágio | Concedentes de estágio |
| e4 | captura | Informar Coordenações de curso, estágio e TCC | Coordenações de curso, estágio e TCC |
| e5 | fim | Atendimento realizado, documento protocolado e apoio acadêmico prestado às coordenações | Colegiado de Curso |

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
| 0.1.0 | 2026-09-03 | scripts/scaffold_pops.py | patch | Esqueleto gerado a partir do diagnóstico diag-coleg-20260903 (recomendação: coletar_mais) | 1780963200002, 1780963200003, 1780963200018 |

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
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/COLEG/COLEG-01.pop.json` (diretrizes v1.12)._
