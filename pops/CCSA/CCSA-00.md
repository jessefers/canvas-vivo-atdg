---
codigo: CCSA-00
titulo: "Visão geral — Centro de Ciências Sociais Aplicadas — Direção de Centro"
versao: "0.1.0"
status: rascunho
setor_codigo: S07-CCSA
setor: "CCSA — Direção de Centro"
atualizado_em: "2026-09-02T17:55:55Z"
agente: —
versao_diretrizes: "1.0"
---

# POP CCSA-00 — Visão geral — Centro de Ciências Sociais Aplicadas — Direção de Centro

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **0.1.0** · Status **rascunho** · Atualizado em 2026-09-02

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Centro de Ciências Sociais Aplicadas — Direção de Centro | Centro de Ciências Sociais Aplicadas — Direção de Centro | Visão do Centro de Ciências Sociais Aplicadas: colegiados de Administração, Ciências Contábeis, Direito, Hotelaria e Turismo, núcleos (NPJ, NUTUR, NUPESA) e contatos por função. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Ensino, Pesquisa e Extensão (Centro) | Visão geral do setor (playbook) | core | S07-CCSA |

### 0.3 Linguagem ubíqua (glossário do processo)

Herda integralmente o glossário institucional (`diretrizes/09-glossario-institucional.md`); sem termos locais adicionais.

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | CCSA-00 |
| Setor | CCSA — Direção de Centro (`S07-CCSA`) |
| Responsável (função) | A definir |
| Periodicidade | A definir |
| Subordinação | Direção Geral de Campus |
| Normativa | Estatuto (Res. 017/99-COU) art. 37 e 41 |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | pb-ccsa |
| Lacunas abertas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Agente responsável | — (não moldado) |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S07_CCSA["S07-CCSA<br/>Centro de Ciências Sociais Aplicadas — Direção de Centro"]
  S01_DG --> S07_CCSA
  P["CCSA-00<br/>Visão geral — Centro de Ciências Sociais Aplicadas — Direçã…"]
  S07_CCSA --> P
  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747
  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747
  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66
  class S01_DG,S07_CCSA setor
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
| 1 | Articular Direção de Centro, colegiados e coordenações | A definir | — | — | A definir | — |
| 2 | Manter a base de contatos por função do Centro | A definir | — | — | A definir | — |
| 3 | Encaminhar demandas do Centro via e-Protocolo | A definir | — | — | A definir | — |

### 3.4 Saída (entregáveis)

— A definir

## 4. Formulários e artefatos (agregados)

— A definir

## 5. Decisões, exceções e pontos de atenção

— Sem decisões registradas

**Pontos de atenção**

- Contatos institucionais — uso interno (LGPD)
- Atualizar a cada troca de coordenação/direção

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
  subgraph R1["CCSA — Direção de Centro"]
    direction LR
    e1(("A definir"))
    e2["Articular Direção de Centro, colegiados e coordenações"]
    e3["Manter a base de contatos por função do Centro"]
    e4["Encaminhar demandas do Centro via e-Protocolo"]
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

**Raias:** CCSA — Direção de Centro

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | A definir | CCSA — Direção de Centro |
| e2 | atividade | Articular Direção de Centro, colegiados e coordenações | CCSA — Direção de Centro |
| e3 | atividade | Manter a base de contatos por função do Centro | CCSA — Direção de Centro |
| e4 | atividade | Encaminhar demandas do Centro via e-Protocolo | CCSA — Direção de Centro |
| e5 | fim | Concluído | CCSA — Direção de Centro |

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
| 0.1.0 | 2026-09-02 | scripts/scaffold_pops.py | patch | Esqueleto inicial gerado deterministicamente a partir das entradas pb-ccsa | pb-ccsa |

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
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/CCSA/CCSA-00.pop.json` (diretrizes v1.0)._
