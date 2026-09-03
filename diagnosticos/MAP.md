---
id: diag-map-20260903
setor_codigo: S02.06-MAP
data: "2026-09-03T02:02:00Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — ATDG — Assessoria Técnica da Direção Geral (`S02.06-MAP`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 8 entrada(s) do Canvas (hash `6c982fb325dd…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Assessoria Técnica e Gestão por Processos |
| Subdomínios | Levantamento de setores, cargos e funções, Aplicação de checklist (Microsoft Forms), Consolidação e padronização de respostas, Elaboração de POP/IT/Manual/Fluxo |
| Contextos vizinhos | Direção Geral do Campus, Setores, Centros e Colegiados do Campus (setor respondente) |
| Sistemas | Microsoft Forms, OneDrive ATDG |
| Normas recorrentes | Plano Diretor Unioeste 2017-2026; Lei nº 13.709/2018 (Lei Geral de Proteção de Dados Pessoais — LGPD) |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.57 | MAP-04 | Elaboração de POP, Instrução de Trabalho, Manual e Fluxos | processo | 1 | 0.65 | 0.5 | 0.35 | 0.65 | coletar_mais | pop-map-04 |
| 0.55 | MAP-03 | Consolidação e padronização das respostas do mapeamento | processo | 1 | 0.6 | 0.4 | 0.45 | 0.6 | coletar_mais | pop-map-03 |
| 0.53 | MAP-02 | Aplicação de checklist/questionário por função (Microsoft Forms) | processo | 2 | 0.55 | 0.4 | 0.55 | 0.7 | coletar_mais | pop-map-02 |
| 0.52 | MAP-00 | Visão geral — ATDG — Mapeamento de Processos | processo | 2 | 0.65 | 0.35 | 0.4 | 0.7 | coletar_mais | pop-map-00 |
| 0.47 | MAP-01 | Levantamento de setores, cargos, funções e servidores | processo | 2 | 0.55 | 0.3 | 0.35 | 0.65 | coletar_mais | pop-map-01 |

### MAP-04 — Elaboração de POP, Instrução de Trabalho, Manual e Fluxos

Elabora POP, Instrução de Trabalho e fluxograma de cada processo mapeado, valida com o setor respondente e consolida no Manual de Gestão de Processos.

| Campo | Valor |
|---|---|
| Gatilho | Planilha consolidada e padronizada de atividades por função disponível (MAP-03) |
| Saída | POP/IT/Fluxo publicados e Manual de Gestão de Processos atualizado |
| Atores | Assessoria Técnica da Direção Geral (ATDG), Setor respondente, Direção Geral do Campus |
| Sistemas | OneDrive ATDG |
| Artefatos | Procedimento Operacional Padrão (POP), Manual de Gestão de Processos do Campus |
| Interfaces | Setor respondente, Direção Geral do Campus |
| Evidências | pb-atdg, 1780963200014, 1780963200015, 1780963200016, 1780963200017, 1780963200031, 1780963200034, 1780963200035 |
| Lacunas | formulario, prazo |
| Justificativa | Etapa final do projeto de mapeamento, evidenciada pelo documento de projeto do Manual de Gestão de Processos; POP completo elaborado (v1.0.0, em_validacao). |

### MAP-03 — Consolidação e padronização das respostas do mapeamento

Importa, normaliza, agrupa e padroniza as respostas do checklist em planilha consolidada, validada pelo setor respondente.

| Campo | Valor |
|---|---|
| Gatilho | Base de respostas do checklist exportada (MAP-02) para consolidação |
| Saída | Planilha consolidada e padronizada de atividades por função |
| Atores | Assessoria Técnica da Direção Geral (ATDG), Setor respondente |
| Sistemas | OneDrive ATDG |
| Artefatos | Planilha consolidada de atividades por função, Controle de versões da consolidação |
| Interfaces | Setor respondente, Direção Geral do Campus |
| Evidências | pb-atdg, 1780963200014, 1780963200015, 1780963200016, 1780963200017, 1780963200031, 1780963200034, 1780963200035 |
| Lacunas | formulario, prazo, versao_documento |
| Justificativa | Entradas mostram múltiplas versões e cópias de teste de planilhas de consolidação, indicando controle de versão ainda informal; POP completo elaborado (v1.0.0, em_validacao). |

### MAP-02 — Aplicação de checklist/questionário por função (Microsoft Forms)

Elabora, envia, monitora e encerra a coleta do checklist de atividades por função via Microsoft Forms.

| Campo | Valor |
|---|---|
| Gatilho | Relação de setores, cargos e funções disponibilizada (MAP-01) para aplicação do checklist |
| Saída | Respostas do checklist coletadas e prontas para consolidação |
| Atores | Assessoria Técnica da Direção Geral (ATDG), Setor respondente |
| Sistemas | Microsoft Forms |
| Artefatos | Formulário de checklist por função, Painel de respostas do checklist |
| Interfaces | Setor respondente |
| Evidências | pb-atdg, 1780963200014, 1780963200015, 1780963200016, 1780963200017, 1780963200031, 1780963200034, 1780963200035 |
| Lacunas | prazo, dados_pessoais_lgpd |
| Justificativa | Evidenciado por múltiplas planilhas de checklist (versões e cópias de teste) nas entradas; POP completo elaborado (v1.0.0, em_validacao), com atenção à LGPD. |

### MAP-00 — Visão geral — ATDG — Mapeamento de Processos

Conduz o ciclo de Mapeamento de Processos do Campus: define escopo, levanta setores/funções, aplica checklist, consolida respostas e elabora POP/IT/Manual/Fluxo de cada processo.

| Campo | Valor |
|---|---|
| Gatilho | Definição, pela Direção Geral ou pela ATDG, do início ou de novo ciclo do projeto de Mapeamento de Processos |
| Saída | Manual de Gestão de Processos do Campus consolidado |
| Atores | Assessoria Técnica da Direção Geral (ATDG), Setor respondente, Direção Geral do Campus |
| Sistemas | Microsoft Forms, OneDrive ATDG |
| Artefatos | Checklist de atividades por função, Manual de Gestão de Processos |
| Interfaces | Setor respondente, Direção Geral do Campus |
| Evidências | pb-atdg, 1780963200014, 1780963200015, 1780963200016, 1780963200017, 1780963200031, 1780963200034, 1780963200035 |
| Lacunas | prazo, dados_pessoais_lgpd |
| Justificativa | Projeto institucional já em curso (documento de projeto, checklists e planilhas de consolidação identificados nas entradas); POP completo elaborado (v1.0.0, em_validacao) cobrindo o ciclo geral. |

### MAP-01 — Levantamento de setores, cargos, funções e servidores

Levanta a estrutura de setores, centros, colegiados, cargos, funções e quantitativo de servidores, e mantém a lista de contatos por função.

| Campo | Valor |
|---|---|
| Gatilho | Início de novo ciclo de mapeamento de processos definido pela ATDG/Direção Geral |
| Saída | Relação consolidada de setores, cargos, funções e servidores disponibilizada |
| Atores | Assessoria Técnica da Direção Geral (ATDG), Setor respondente |
| Sistemas | OneDrive ATDG |
| Artefatos | Relação de setores, cargos, funções e servidores, Lista de contatos institucionais por função |
| Interfaces | Setor respondente |
| Evidências | pb-atdg, 1780963200014, 1780963200015, 1780963200016, 1780963200017, 1780963200031, 1780963200034, 1780963200035 |
| Lacunas | formulario, prazo |
| Justificativa | Etapa evidenciada por lista de contatos por função e documento de mapeamento já existentes; POP completo elaborado (v1.0.0, em_validacao). |

## 3. Lacunas do setor

- Prazos-padrão de cada etapa do ciclo de mapeamento não normatizados
- Tratamento formal de dados pessoais dos respondentes (LGPD) não documentado em política específica
- Controle de versionamento de planilhas e documentos ainda informal (cópias de teste em circulação)

## 4. Lições propostas

— Nenhuma

> Diagnóstico do lote MAP (5 processos) elaborado a partir de 8 entradas do Canvas (playbook, contatos por função, checklists, documento de mapeamento e projeto do Manual de Gestão de Processos). Os 5 processos foram elaborados em POP completo (playbook DDD híbrido, v1.0.0, em_validacao) no lote B. Nomes e e-mails de servidores presentes nas entradas não foram reproduzidos, por força da LGPD.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/MAP.json` (diretrizes v1.0)._
