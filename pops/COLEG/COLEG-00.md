---
codigo: COLEG-00
titulo: "Visão geral — Colegiado de Curso (transversal)"
versao: "0.1.0"
status: rascunho
setor_codigo: S12-COLEG
setor: "Colegiado de Curso"
atualizado_em: "2026-09-02T17:55:55Z"
agente: —
versao_diretrizes: "1.0"
---

# POP COLEG-00 — Visão geral — Colegiado de Curso (transversal)

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **0.1.0** · Status **rascunho** · Atualizado em 2026-09-02

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Colegiado de Curso (transversal) | Colegiado de Curso (transversal) | Guia das rotinas dos colegiados e coordenações de curso, estágio e TCC, e do agente universitário: comunicação, protocolo, gestão acadêmica e órgãos colegiados. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Colegiados e Cursos | Visão geral do setor (playbook) | core | S12-COLEG |

### 0.3 Linguagem ubíqua (glossário do processo)

Herda integralmente o glossário institucional (`diretrizes/09-glossario-institucional.md`); sem termos locais adicionais.

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | COLEG-00 |
| Setor | Colegiado de Curso (`S12-COLEG`) |
| Responsável (função) | A definir |
| Periodicidade | A definir |
| Subordinação | Direção Geral de Campus |
| Normativa | Estatuto (Res. 017/99-COU) art. 41; Lei nº 11.788/2008; Regulamentos de Estágio e TCC dos cursos |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | pb-colegiado |
| Lacunas abertas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Agente responsável | — (não moldado) |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S12_COLEG["S12-COLEG<br/>Colegiado de Curso (transversal)"]
  S01_DG --> S12_COLEG
  P["COLEG-00<br/>Visão geral — Colegiado de Curso (transversal)"]
  S12_COLEG --> P
  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747
  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747
  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66
  class S01_DG,S12_COLEG setor
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
| 1 | Comunicação, atendimento e gestão de documentos/e-Protocolo | A definir | — | — | A definir | — |
| 2 | Condução de Colegiado e NDE, com atas e pautas | A definir | — | — | A definir | — |
| 3 | Gestão acadêmica no Academus (planos, matrícula, notas, horários) | A definir | — | — | A definir | — |
| 4 | Estágio: termos, bancas e articulação com concedentes | A definir | — | — | A definir | — |
| 5 | TCC: orientadores, bancas, defesas e envio à biblioteca | A definir | — | — | A definir | — |

### 3.4 Saída (entregáveis)

— A definir

## 4. Formulários e artefatos (agregados)

— A definir

## 5. Decisões, exceções e pontos de atenção

— Sem decisões registradas

**Pontos de atenção**

- Forte vínculo com prazos do calendário acadêmico
- Observar a Lei de Estágio (11.788/2008) e os regulamentos dos cursos
- Manter vínculos corretos no Academus; LGPD

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
  subgraph R1["Colegiado de Curso"]
    direction LR
    e1(("A definir"))
    e2["Comunicação, atendimento e gestão de documentos/e-Protocolo"]
    e3["Condução de Colegiado e NDE, com atas e pautas"]
    e4["Gestão acadêmica no Academus (planos, matrícula, notas, horários)"]
    e5["Estágio: termos, bancas e articulação com concedentes"]
    e6["TCC: orientadores, bancas, defesas e envio à biblioteca"]
    e7((("Concluído")))
  end
  e1 --> e2
  e2 --> e3
  e3 --> e4
  e4 --> e5
  e5 --> e6
  e6 --> e7
  classDef inicio fill:#f3f4f6,stroke:#6b7280,stroke-width:1.5px,color:#374151
  classDef atividade fill:#E6F7F0,stroke:#0B7A4E,stroke-width:2px,color:#0B7A4E
  classDef decisao fill:#FFF4ED,stroke:#C9783A,stroke-width:2px,color:#C9783A
  classDef fim fill:#FDEAEE,stroke:#CC1544,stroke-width:4px,color:#CC1544
  classDef pausa fill:#FDEAEE,stroke:#CC1544,stroke-width:2px,color:#CC1544
  classDef captura fill:#E0F2F8,stroke:#0B4D66,stroke-width:2px,color:#0B4D66
  class e1 inicio
  class e2,e3,e4,e5,e6 atividade
  class e7 fim
```

## 11. Especificação BPMN para o Miro

**Raias:** Colegiado de Curso

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | A definir | Colegiado de Curso |
| e2 | atividade | Comunicação, atendimento e gestão de documentos/e-Protocolo | Colegiado de Curso |
| e3 | atividade | Condução de Colegiado e NDE, com atas e pautas | Colegiado de Curso |
| e4 | atividade | Gestão acadêmica no Academus (planos, matrícula, notas, horários) | Colegiado de Curso |
| e5 | atividade | Estágio: termos, bancas e articulação com concedentes | Colegiado de Curso |
| e6 | atividade | TCC: orientadores, bancas, defesas e envio à biblioteca | Colegiado de Curso |
| e7 | fim | Concluído | Colegiado de Curso |

| De | Para | Rótulo |
|---|---|---|
| e1 | e2 | — |
| e2 | e3 | — |
| e3 | e4 | — |
| e4 | e5 | — |
| e5 | e6 | — |
| e6 | e7 | — |

_Especificação gerada a partir dos passos do POP; 1 raia(s). Revisar decisões e pausas antes de construir no Miro._

## 12. Histórico de versões

| Versão | Data | Autor | Tipo | Mudanças | Fontes |
|---|---|---|---|---|---|
| 0.1.0 | 2026-09-02 | scripts/scaffold_pops.py | patch | Esqueleto inicial gerado deterministicamente a partir das entradas pb-colegiado | pb-colegiado |

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
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/COLEG/COLEG-00.pop.json` (diretrizes v1.0)._
