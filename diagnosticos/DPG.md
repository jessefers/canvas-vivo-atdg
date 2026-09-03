---
id: diag-dpg-20260903
setor_codigo: S05.01-DPG
data: "2026-09-03T01:41:28Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Div. de Pós-Graduação (`S05.01-DPG`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 6 entrada(s) do Canvas (hash `38d6e6358c68…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Gestão Acadêmica |
| Subdomínios | Capacitação e afastamento docente, Ética no uso de animais (CEUA/CEUAP), Pós-graduação lato sensu, Pós-graduação stricto sensu |
| Contextos vizinhos | PRPPG (Pró-Reitoria de Pesquisa e Pós-Graduação), CEUA/CEUAP, Coordenação Acadêmica — Geral, Direção Geral de Campus |
| Sistemas | e-Protocolo |
| Normas recorrentes | Resolução nº 029/2013-CEPE; Resolução nº 071/2021-CEPE; Resolução nº 078/2016-CEPE; Manuais de Fluxos e-Protocolo — PRPPG |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.62 | DPG-02 | Fluxos e-Protocolo — PRPPG CEUA | processo | 2 | 0.8 | 0.3 | 0.8 | 0.55 | gerar_pop | DPG-02 |
| 0.59 | DPG-00 | Visão geral — pós-graduação e pesquisa (PRPPG) | processo | 2 | 0.7 | 0.4 | 0.7 | 0.55 | gerar_pop | DPG-00 |
| 0.58 | DPG-01 | Fluxos e-Protocolo — PRPPG Capacitação de Servidores | processo | 2 | 0.75 | 0.3 | 0.65 | 0.55 | gerar_pop | DPG-01 |
| 0.58 | DPG-03 | Fluxos e-Protocolo — PRPPG CEUAP | processo | 2 | 0.75 | 0.2 | 0.8 | 0.55 | gerar_pop | DPG-03 |
| 0.58 | DPG-05 | Fluxos e-Protocolo — PRPPG Stricto Sensu | processo | 2 | 0.75 | 0.25 | 0.75 | 0.5 | gerar_pop | DPG-05 |
| 0.56 | DPG-04 | Fluxos e-Protocolo — PRPPG Lato Sensu | processo | 2 | 0.7 | 0.3 | 0.7 | 0.5 | gerar_pop | DPG-04 |

### DPG-02 — Fluxos e-Protocolo — PRPPG CEUA

Tramitação de projetos novos, alterações e relatórios finais no Comitê de Ética no Uso de Animais (CEUA), com protocolo unificado e termo de responsabilidade.

| Campo | Valor |
|---|---|
| Gatilho | Proposição de projeto de pesquisa com uso de animais |
| Saída | Projeto autorizado (ou não) pelo Presidente do CEUA |
| Atores | Proponente/Coordenador da atividade, CEUA/CEUAP |
| Sistemas | e-Protocolo |
| Artefatos | Protocolo unificado/formulário específico |
| Interfaces | CEUA/CEUAP |
| Evidências | 1780963200044 |
| Lacunas | sistema, interface_setorial, dados_pessoais_lgpd |
| Justificativa | Alto risco ético/regulatório (bem-estar animal, sigilo de propriedade intelectual); baixa frequência mas alta criticidade. |

### DPG-00 — Visão geral — pós-graduação e pesquisa (PRPPG)

Guia consolidado dos fluxos de pós-graduação e pesquisa no e-Protocolo (PRPPG).

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de afastamento/capacitação, projeto de ética ou proposta/alteração de curso de pós-graduação |
| Saída | Processo deliberado pela PRPPG |
| Atores | Proponente/Coordenador da atividade, Coordenação Acadêmica, PRPPG |
| Sistemas | e-Protocolo |
| Artefatos | Protocolo unificado/formulário específico |
| Interfaces | PRPPG |
| Evidências | pb-pos-graduacao |
| Lacunas | sistema, interface_setorial |
| Justificativa | Consolida os cinco fluxos específicos já evidenciados (01 a 05); alta criticidade por envolver afastamento docente, ética em pesquisa e credenciamento de cursos. |

### DPG-01 — Fluxos e-Protocolo — PRPPG Capacitação de Servidores

Fluxos de afastamento e qualificação docente (Resolução nº 029/2013-CEPE): parcial/integral, exterior, prorrogação, transformação, troca de programa e retorno.

| Campo | Valor |
|---|---|
| Gatilho | Interesse do docente em afastamento/qualificação |
| Saída | Afastamento/qualificação deliberado pela PRPPG |
| Atores | Proponente/Coordenador da atividade, Coordenação Acadêmica, PRPPG |
| Sistemas | e-Protocolo |
| Artefatos | Protocolo unificado/formulário específico |
| Interfaces | PRPPG |
| Evidências | 1780963200043 |
| Lacunas | sistema, interface_setorial, versao_documento |
| Justificativa | Processo de alto impacto em RH e orçamento (afastamento docente com ônus); requisitos adicionais para o exterior aumentam o risco de não conformidade. |

### DPG-03 — Fluxos e-Protocolo — PRPPG CEUAP

Tramitação de projetos novos, alterações e relatórios finais no Comitê de Ética no Uso de Animais de Produção (CEUAP).

| Campo | Valor |
|---|---|
| Gatilho | Proposição de projeto de pesquisa com uso de animais de produção |
| Saída | Projeto autorizado (ou não) pelo Presidente do CEUAP |
| Atores | Proponente/Coordenador da atividade, CEUA/CEUAP |
| Sistemas | e-Protocolo |
| Artefatos | Protocolo unificado/formulário específico |
| Interfaces | CEUA/CEUAP |
| Evidências | 1780963200045 |
| Lacunas | sistema, interface_setorial, dados_pessoais_lgpd |
| Justificativa | Espelha o fluxo do CEUA para animais de produção; risco ético/regulatório equivalente, frequência ainda menor. |

### DPG-05 — Fluxos e-Protocolo — PRPPG Stricto Sensu

Fluxos de proposta de novo programa/curso, implantação, modificação de projeto pedagógico/regulamento e criação de disciplinas (Resolução nº 078/2016-CEPE).

| Campo | Valor |
|---|---|
| Gatilho | Proposta ou alteração de programa/curso stricto sensu |
| Saída | Proposta/alteração deliberada pela PRPPG |
| Atores | Proponente/Coordenador da atividade, Coordenação Acadêmica, PRPPG |
| Sistemas | e-Protocolo |
| Artefatos | Protocolo unificado/formulário específico |
| Interfaces | PRPPG |
| Evidências | 1780963200047 |
| Lacunas | sistema, interface_setorial, versao_documento |
| Justificativa | Impacta credenciamento/avaliação de programas de mestrado e doutorado; documentação ampliada para novos programas. |

### DPG-04 — Fluxos e-Protocolo — PRPPG Lato Sensu

Fluxos de proposta, alteração/prorrogação, mudança de cronograma/docentes, substituição de coordenador e alteração financeira de cursos lato sensu (Resolução nº 071/2021-CEPE).

| Campo | Valor |
|---|---|
| Gatilho | Proposta de curso, alteração ou substituição na pós-graduação lato sensu |
| Saída | Proposta/alteração deliberada pela PRPPG |
| Atores | Proponente/Coordenador da atividade, Coordenação Acadêmica, PRPPG |
| Sistemas | e-Protocolo |
| Artefatos | Protocolo unificado/formulário específico |
| Interfaces | PRPPG |
| Evidências | 1780963200046 |
| Lacunas | sistema, interface_setorial, versao_documento |
| Justificativa | Envolve gestão financeira de cursos (planilha) e credenciamento; risco de conformidade moderado-alto. |

## 3. Lacunas do setor

- Responsável nominal (função) da Div. de Pós-Graduação ainda não formalizado
- SLA de deliberação da PRPPG e dos comitês de ética não evidenciado

## 4. Lições propostas

— Nenhuma

> Os cinco fluxos específicos (01 a 05) e a visão geral (00) cobrem integralmente os temas evidenciados no Canvas para a Div. de Pós-Graduação; nenhum processo adicional sem POP foi identificado nesta leva.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/DPG.json` (diretrizes v1.0)._
