---
codigo: DPG-03
titulo: "Fluxos e-Protocolo — PRPPG CEUAP"
versao: "1.0.0"
status: em_validacao
setor_codigo: S05.01-DPG
setor: "Div. de Pós-Graduação"
atualizado_em: "2026-09-03T01:52:54Z"
agente: —
versao_diretrizes: "1.2"
---

# POP DPG-03 — Fluxos e-Protocolo — PRPPG CEUAP

> **Documento vivo** · ATDG — Assessoria Técnica da Direção Geral · UNIOESTE Campus Foz do Iguaçu · Formato DDD híbrido + BPMN 2.0 padrão Anne Bail · Versão **1.0.0** · Status **em_validacao** · Atualizado em 2026-09-03

## 0. Cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Coordenação Acadêmica | Div. de Pós-Graduação | Manual da Comissão e-Protocolo com os fluxos do Comitê de Ética no Uso de Animais de Produção (CEUAP). Define a tramitação para projetos novos, alteração de projetos e relatórios finais, com abertura pelo docente responsável (protocolo unificado e termo de responsabilidade) e encaminhamento ao responsável pelo campo de estudo/coordenador. Projetos com propriedade intelectual tramitam como sigilosos. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Gestão Acadêmica | Fluxos e-Protocolo — PRPPG CEUAP | core | S05.01-DPG |

### 0.3 Linguagem ubíqua (glossário do processo)

| Termo | Definição | Sistema |
|---|---|---|
| e-Protocolo | Sistema institucional de tramitação eletrônica de processos e documentos da Unioeste. | e-Protocolo |
| PRPPG | Pró-Reitoria de Pesquisa e Pós-Graduação da Unioeste, responsável por deliberar sobre afastamento/capacitação docente, cursos de pós-graduação e ética em pesquisa. | — |
| CEUA | Comitê de Ética no Uso de Animais, responsável por autorizar e acompanhar projetos de pesquisa que envolvam animais. | — |
| CEUAP | Comitê de Ética no Uso de Animais de Produção, responsável por autorizar e acompanhar projetos que envolvam animais de produção. | — |
| Lato sensu | Pós-graduação de especialização, com carga horária e regras próprias definidas pela Resolução nº 071/2021-CEPE. | — |
| Stricto sensu | Pós-graduação de mestrado ou doutorado, com programas regidos pela Resolução nº 078/2016-CEPE. | — |

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | DPG-03 |
| Setor | Div. de Pós-Graduação (`S05.01-DPG`) |
| Responsável (função) | Coordenação Acadêmica |
| Periodicidade | A definir |
| Subordinação | Coordenação Acadêmica |
| Normativa | Manual de Fluxos e-Protocolo — PRPPG/CEUAP; FLUXO_-_PRPPG_-_CEUAP.pdf — Manual da Comissão e-Protocolo (documento-fonte) |
| Produto ATDG | POP |
| Pasta OneDrive | 03_MAPEAMENTO DE PROCESSOS |
| Fontes (entradas do Canvas) | 1780963200045 |
| Lacunas abertas | interface_setorial, versao_documento |
| Agente responsável | — (não moldado) |

## 2. Organograma

```mermaid
graph TD
  S01_DG["S01-DG<br/>Direção Geral de Campus"]
  S05_CACAD["S05-CACAD<br/>Coordenação Acadêmica"]
  S01_DG --> S05_CACAD
  S05_01_DPG["S05.01-DPG<br/>Div. de Pós-Graduação"]
  S05_CACAD --> S05_01_DPG
  P["DPG-03<br/>Fluxos e-Protocolo — PRPPG CEUAP"]
  S05_01_DPG --> P
  V1["Proponente/Coordenador da atividade"]
  P -. interface .-> V1
  V2["CEUA/CEUAP"]
  P -. interface .-> V2
  V3["Coordenação Acadêmica"]
  P -. interface .-> V3
  classDef setor fill:#EEF0F7,stroke:#1B2747,stroke-width:1.5px,color:#1B2747
  classDef destaque fill:#FDEAEE,stroke:#CC1544,stroke-width:3px,color:#1B2747
  classDef vizinho fill:#E0F2F8,stroke:#0B4D66,stroke-width:1.5px,color:#0B4D66
  class S01_DG,S05_CACAD,S05_01_DPG setor
  class P destaque
  class V1,V2,V3 vizinho
```

## 3. Playbook

### 3.1 Gatilho (evento de domínio)

**Proposição de projeto de pesquisa com uso de animais de produção** — origem: Proponente/Coordenador da atividade

### 3.2 Entrada

- Protocolo unificado e termo de responsabilidade do projeto

### 3.3 Passo a passo

| Nº | Ação | Responsável | Sistema | Artefato | Prazo | Evento |
|---|---|---|---|---|---|---|
| 1 | Abrir o e-Protocolo com o protocolo unificado e o termo de responsabilidade | Proponente/Coordenador da atividade | e-Protocolo | Protocolo unificado; Termo de responsabilidade | Antes do início do projeto | e-Protocolo aberto |
| 2 | Verificar se o projeto envolve propriedade intelectual e, em caso positivo, marcar o processo como sigiloso | Proponente/Coordenador da atividade | e-Protocolo | Processo e-Protocolo (sigiloso) | No ato da abertura do e-Protocolo | Sigilo classificado |
| 3 | Encaminhar ao responsável pelo campo de estudo/coordenador para análise | Proponente/Coordenador da atividade | e-Protocolo | Processo e-Protocolo | A definir | Processo analisado |
| 4 | Tramitar ao Presidente do CEUAP para autorização | CEUA/CEUAP | e-Protocolo | Processo e-Protocolo | A definir | Autorização solicitada |
| 5 | Aguardar a deliberação do Presidente do CEUAP | CEUA/CEUAP | e-Protocolo | Processo e-Protocolo | A definir | Deliberação aguardada |
| 6 | Devolver ao proponente para ajustes quando o CEUAP não autorizar | CEUA/CEUAP | e-Protocolo | Parecer do comitê | A definir | Processo devolvido |
| 7 | Executar o projeto sob acompanhamento do CEUAP quando autorizado | Proponente/Coordenador da atividade | e-Protocolo | Processo e-Protocolo | Conforme cronograma do projeto | Projeto em execução |
| 8 | Submeter alterações e relatórios finais pelos fluxos próprios do CEUAP | Proponente/Coordenador da atividade | e-Protocolo | Relatório final | Conforme cronograma do projeto | Relatório final submetido |

### 3.4 Saída (entregáveis)

- Projeto autorizado (ou não) pelo Presidente do CEUAP, com relatório final ao término

## 4. Formulários e artefatos (agregados)

| Nome | Tipo | Sistema | Campos-chave | Preenchimento |
|---|---|---|---|---|
| Protocolo unificado | formulario | e-Protocolo | proponente, campo de estudo, espécie/finalidade, sigilo (S/N) | Proponente/Coordenador da atividade |
| Termo de responsabilidade | documento | e-Protocolo | responsável pelo projeto, compromissos éticos assumidos | Proponente/Coordenador da atividade |
| Relatório final de projeto | documento | e-Protocolo | resultados, conformidade ética, data de encerramento | Proponente/Coordenador da atividade |

## 5. Decisões, exceções e pontos de atenção

| Decisão | Condição | Sim → | Não → |
|---|---|---|---|
| Projeto envolve propriedade intelectual? | O projeto de pesquisa envolve propriedade intelectual | Marcar e tramitar o e-Protocolo como sigiloso | Tramitar pelo fluxo ordinário (não sigiloso) |
| Presidente do CEUAP autoriza? | O Presidente do CEUAP aprova o protocolo unificado e o termo de responsabilidade | Executar o projeto sob acompanhamento do comitê e, ao final, submeter relatório final | Devolver ao proponente para ajustes e nova submissão |

**Pontos de atenção**

- Projetos com propriedade intelectual: tramitar como sigiloso
- Distinguir CEUAP (animais de produção) de CEUA
- Anexar os termos obrigatórios desde a abertura

## 6. Contingência

- Se o e-Protocolo estiver indisponível, registrar a solicitação em meio alternativo e regularizar a tramitação eletrônica assim que o sistema for restabelecido.
- Se a documentação estiver incompleta, devolver ao proponente/coordenador com a relação de pendências antes de encaminhar à PRPPG.
- Em caso de dúvida sobre o fluxo aplicável, consultar a Comissão e-Protocolo ou a PRPPG antes de tramitar.
- Projetos com propriedade intelectual devem ser marcados como sigilosos desde a abertura; se identificado após a abertura, corrigir a classificação de sigilo imediatamente.

## 7. Checklist

- ( ) Ato/modalidade corretamente identificado
- ( ) e-Protocolo aberto conforme o fluxo específico
- ( ) Documentação obrigatória anexada
- ( ) Classificação de sigilo (propriedade intelectual) verificada, quando aplicável
- ( ) Encaminhamento à PRPPG realizado e acompanhamento registrado

## 8. KPI / Indicadores

| Indicador | Fórmula | Meta | Fonte |
|---|---|---|---|
| Tempo médio de tramitação (abertura no e-Protocolo → deliberação da PRPPG) | Σ(data da deliberação − data de abertura) / nº de processos no período | A definir | e-Protocolo |
| Percentual de processos devolvidos por pendência documental ou fluxo incorreto | processos devolvidos / total de processos abertos × 100 | A definir | e-Protocolo |
| Percentual de projetos corretamente classificados como sigilosos na abertura | projetos com classificação correta / total de projetos com propriedade intelectual × 100 | 100% | e-Protocolo |

## 9. Mapa de contexto (interfaces inter-setoriais)

| Origem | Relação | Destino | Artefato | Canal |
|---|---|---|---|---|
| Proponente/Coordenador da atividade | fornece | CEUA/CEUAP | Protocolo unificado e termo de responsabilidade | e-Protocolo |
| CEUA/CEUAP | aprova | Proponente/Coordenador da atividade | Autorização/parecer do comitê de ética | e-Protocolo |
| Proponente/Coordenador da atividade | informa | Coordenação Acadêmica | Situação do projeto perante o comitê | e-Protocolo |

## 10. Fluxograma (BPMN 2.0 — padrão Anne Bail)

```mermaid
flowchart LR
  subgraph R1["Proponente/Coordenador da atividade"]
    direction LR
    e1(("Proposição de projeto de pesquisa com uso de animais de produção"))
    e2["Elaborar o protocolo unificado e o termo de responsabilidade"]
    e3{"Projeto envolve propriedade intelectual?"}
    e4["Marcar o processo como sigiloso no e-Protocolo"]
    e5["Abrir o e-Protocolo com o protocolo unificado e o termo de responsabi…"]
    e6[["✉ Encaminhar ao responsável pelo campo de estudo/coordenador"]]
    e7["Analisar o protocolo e solicitar ajustes, se necessário"]
    e11["Devolver ao proponente para ajustes e nova submissão"]
    e12((("Projeto devolvido para ajustes")))
    e13["Executar o projeto sob acompanhamento do CEUAP"]
  end
  subgraph R2["CEUA/CEUAP"]
    direction LR
    e8[["✉ Tramitar ao Presidente do CEUAP para autorização"]]
    e9(["⏱ Aguardar autorização do Presidente do CEUAP"])
    e10{"Presidente do CEUAP autoriza?"}
    e14[["✉ Submeter alterações e relatório final ao CEUAP pelos fluxos próprios"]]
    e15((("Projeto autorizado e encerrado com relatório final")))
  end
  e1 --> e2
  e2 --> e3
  e3 -- Sim --> e4
  e4 --> e5
  e3 -- Não --> e5
  e5 --> e6
  e6 --> e7
  e7 --> e8
  e8 --> e9
  e9 --> e10
  e10 -- Não --> e11
  e11 --> e12
  e10 -- Sim --> e13
  e13 --> e14
  e14 --> e15
  classDef inicio fill:#f3f4f6,stroke:#6b7280,stroke-width:1.5px,color:#374151
  classDef atividade fill:#E6F7F0,stroke:#0B7A4E,stroke-width:2px,color:#0B7A4E
  classDef decisao fill:#FFF4ED,stroke:#C9783A,stroke-width:2px,color:#C9783A
  classDef fim fill:#FDEAEE,stroke:#CC1544,stroke-width:4px,color:#CC1544
  classDef pausa fill:#FDEAEE,stroke:#CC1544,stroke-width:2px,color:#CC1544
  classDef captura fill:#E0F2F8,stroke:#0B4D66,stroke-width:2px,color:#0B4D66
  class e1 inicio
  class e2,e4,e5,e7,e11,e13 atividade
  class e3,e10 decisao
  class e6,e8,e14 captura
  class e9 pausa
  class e12,e15 fim
```

## 11. Especificação BPMN para o Miro

**Raias:** Div. de Pós-Graduação · Proponente/Coordenador da atividade · CEUA/CEUAP

| Id | Tipo | Elemento | Raia |
|---|---|---|---|
| e1 | inicio | Proposição de projeto de pesquisa com uso de animais de produção | Proponente/Coordenador da atividade |
| e2 | atividade | Elaborar o protocolo unificado e o termo de responsabilidade | Proponente/Coordenador da atividade |
| e3 | decisao | Projeto envolve propriedade intelectual? | Proponente/Coordenador da atividade |
| e4 | atividade | Marcar o processo como sigiloso no e-Protocolo | Proponente/Coordenador da atividade |
| e5 | atividade | Abrir o e-Protocolo com o protocolo unificado e o termo de responsabilidade | Proponente/Coordenador da atividade |
| e6 | captura | Encaminhar ao responsável pelo campo de estudo/coordenador | Proponente/Coordenador da atividade |
| e7 | atividade | Analisar o protocolo e solicitar ajustes, se necessário | Proponente/Coordenador da atividade |
| e8 | captura | Tramitar ao Presidente do CEUAP para autorização | CEUA/CEUAP |
| e9 | pausa | Aguardar autorização do Presidente do CEUAP | CEUA/CEUAP |
| e10 | decisao | Presidente do CEUAP autoriza? | CEUA/CEUAP |
| e11 | atividade | Devolver ao proponente para ajustes e nova submissão | Proponente/Coordenador da atividade |
| e12 | fim | Projeto devolvido para ajustes | Proponente/Coordenador da atividade |
| e13 | atividade | Executar o projeto sob acompanhamento do CEUAP | Proponente/Coordenador da atividade |
| e14 | captura | Submeter alterações e relatório final ao CEUAP pelos fluxos próprios | CEUA/CEUAP |
| e15 | fim | Projeto autorizado e encerrado com relatório final | CEUA/CEUAP |

| De | Para | Rótulo |
|---|---|---|
| e1 | e2 | — |
| e2 | e3 | — |
| e3 | e4 | Sim |
| e4 | e5 | — |
| e3 | e5 | Não |
| e5 | e6 | — |
| e6 | e7 | — |
| e7 | e8 | — |
| e8 | e9 | — |
| e9 | e10 | — |
| e10 | e11 | Não |
| e11 | e12 | — |
| e10 | e13 | Sim |
| e13 | e14 | — |
| e14 | e15 | — |

_Especificação gerada a partir dos passos do POP; 1 raia(s). Revisar decisões e pausas antes de construir no Miro._

## 12. Histórico de versões

| Versão | Data | Autor | Tipo | Mudanças | Fontes |
|---|---|---|---|---|---|
| 0.1.0 | 2026-09-02 | scripts/scaffold_pops.py | patch | Esqueleto inicial gerado deterministicamente a partir das entradas 1780963200045 | 1780963200045 |
| 1.0.0 | 2026-09-03 | agente:construtor-pop (lote D1) | major | Passo 1 alterado (acao, responsavel, sistema, artefato, prazo, evento); Passo 2 alterado (acao, responsavel, sistema, artefato, prazo, evento); Passo 3 alterado (acao, responsavel, sistema, artefato, prazo, evento); Passo 4 alterado (acao, responsavel, sistema, artefato, prazo, evento); Passo adicionado após 1: Verificar se o projeto envolve propriedade intelectual e, em caso positivo, marc; Passo adicionado após 3: Aguardar a deliberação do Presidente do CEUAP; Passo adicionado após 3: Devolver ao proponente para ajustes quando o CEUAP não autorizar; Passo adicionado após 3: Executar o projeto sob acompanhamento do CEUAP quando autorizado; entrada_nova: +1; saida_nova: +1; artefatos_novos: +3; decisoes_novas: +2; kpis_novos: +3; mapa_contexto_novo: +3; pontos_atencao_novos: +3; contingencia_nova: +4; checklist_novo: +5; glossario_novo: +6; normativa_nova: +1; Campo identificacao.responsavel atualizado; Campo playbook.gatilho atualizado; Raias adicionadas: Proponente/Coordenador da atividade, CEUA/CEUAP; Elementos BPMN removidos: e1, e2, e3, e4, e5, e6; Elementos BPMN adicionados: 15; Status promovido a em_validacao (≥ 3 passos e responsável definido) | 1780963200045 |

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
_Canvas Vivo — Base de Conhecimento Institucional · ATDG · UNIOESTE Campus Foz do Iguaçu · gerado por `scripts/render_pop.py` a partir de `pops/DPG/DPG-03.pop.json` (diretrizes v1.2)._
