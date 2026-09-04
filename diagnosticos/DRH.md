---
id: diag-drh-20260903
setor_codigo: S03.07-DRH
data: "2026-09-03T01:59:01Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Div. de Recursos Humanos (`S03.07-DRH`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 8 entrada(s) do Canvas (hash `086ee148d16d…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Gestão de Pessoas |
| Subdomínios | Controle de frequência (ponto eletrônico), Tramitação de processos funcionais (e-Protocolo/PRORH) |
| Contextos vizinhos | Chefia imediata, PRORH/GRE (Reitoria), Servidor |
| Sistemas | ponto eletrônico, e-Protocolo |
| Normas recorrentes | Lei nº 6.174/1970; IS 001/2024-DRH/Foz; Instrução 002/2019; Edital 096/2023-GRE (Anexo I); Fluxos e-Protocolo PRORH v3.0 |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.81 | DRH-02 | Registro e apuração de frequência (ponto eletrônico) | processo | 1 | 0.85 | 0.95 | 0.85 | 0.3 | gerar_pop | — |
| 0.78 | DRH-00 | Playbook — Recursos Humanos (visão geral) | processo | 1 | 0.8 | 0.9 | 0.8 | 0.35 | gerar_pop | DRH-00 |
| 0.71 | DRH-01 | Fluxos e-Protocolo — RH (PRORH) v3.0 | processo | 2 | 0.85 | 0.65 | 0.8 | 0.4 | gerar_pop | DRH-01 |
| 0.64 | DRH-03 | Instrução de processos de RH no e-Protocolo (licenças, afastamentos, progressões) | processo | 2 | 0.75 | 0.55 | 0.7 | 0.45 | coletar_mais | — |

### DRH-02 — Registro e apuração de frequência (ponto eletrônico)

Registro diário do ponto eletrônico, apuração semanal pela chefia imediata e comunicação de falhas/justificativas em até 48h via e-Protocolo, conforme IS 001/2024-DRH/Foz e Instrução 002/2019.

| Campo | Valor |
|---|---|
| Gatilho | Início da jornada de trabalho do servidor |
| Saída | Frequência apurada e eventuais falhas justificadas e registradas dentro do prazo |
| Atores | Servidor, Chefia imediata, Chefe da Divisão de Recursos Humanos |
| Sistemas | ponto eletrônico, e-Protocolo |
| Artefatos | Registro de ponto, Apuração semanal de frequência, Justificativa de frequência |
| Interfaces | Div. de Recursos Humanos ↔ Chefia imediata, Div. de Recursos Humanos ↔ Servidor |
| Evidências | 1780963200022, 1780963200025, 1780963200026, pb-rh |
| Lacunas | responsavel, passos, sistema, formulario, interface_setorial |
| Justificativa | Processo evidenciado por três normas (IS 001/2024-DRH/Foz, Instrução 002/2019, Lei nº 6.174/1970) e pelo playbook geral, mas sem POP dedicado; frequência diária/semanal e vedação de prestação de serviço sem registro elevam o risco. Recomenda-se gerar POP específico (DRH-02) a partir das normas já mapeadas. |

### DRH-00 — Playbook — Recursos Humanos (visão geral)

Guia consolidado do controle diário/semanal de frequência e da instrução de processos funcionais de RH no e-Protocolo.

| Campo | Valor |
|---|---|
| Gatilho | Início da jornada de trabalho do servidor ou necessidade de instruir processo funcional de RH |
| Saída | Frequência apurada (com justificativa quando houver falha) e processo funcional instruído e deliberado |
| Atores | Servidor, Chefia imediata, Chefe da Divisão de Recursos Humanos, PRORH |
| Sistemas | ponto eletrônico, e-Protocolo |
| Artefatos | Registro de ponto, Apuração semanal de frequência, Justificativa de frequência, Processo e-Protocolo de RH |
| Interfaces | Div. de Recursos Humanos ↔ Chefia imediata, Div. de Recursos Humanos ↔ Servidor, Div. de Recursos Humanos ↔ PRORH |
| Evidências | pb-rh |
| Lacunas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Justificativa | Alta frequência (diária/semanal) e criticidade funcional/disciplinar, sem responsável, KPIs ou contingências definidos antes deste lote. |

### DRH-01 — Fluxos e-Protocolo — RH (PRORH) v3.0

Instrução dos processos funcionais de RH no e-Protocolo conforme o fluxo vigente (v3.0), consolidando as versões e cópias anteriores como histórico.

| Campo | Valor |
|---|---|
| Gatilho | Servidor ou chefia solicita processo funcional de RH |
| Saída | Processo de RH instruído, encaminhado e deliberado pela PRORH conforme o fluxo vigente (v3.0) |
| Atores | Servidor, Chefe da Divisão de Recursos Humanos, PRORH |
| Sistemas | e-Protocolo |
| Artefatos | Processo e-Protocolo de RH, Documentação funcional |
| Interfaces | Div. de Recursos Humanos ↔ Servidor, Div. de Recursos Humanos ↔ PRORH |
| Evidências | 1780963200048, 1780963200065, 1780963200066 |
| Lacunas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Justificativa | Três entradas do Canvas registram versões (v2.0, v3.0) e uma cópia do mesmo manual (lição L-005): risco de uso de versão superada torna prioritário consolidar o POP na versão vigente. |

### DRH-03 — Instrução de processos de RH no e-Protocolo (licenças, afastamentos, progressões)

Tramitação, por tipo de demanda funcional (licença, afastamento, progressão e demais), dos processos de RH no e-Protocolo, com apoio do perfil profissiográfico das funções (Edital 096/2023-GRE).

| Campo | Valor |
|---|---|
| Gatilho | Servidor ou chefia solicita processo funcional de RH por tipo específico de demanda |
| Saída | Processo de RH instruído e encaminhado às instâncias competentes conforme o tipo de demanda |
| Atores | Servidor, Chefia imediata, Chefe da Divisão de Recursos Humanos, PRORH |
| Sistemas | e-Protocolo |
| Artefatos | Processo e-Protocolo, Perfil profissiográfico da função, Documentação funcional |
| Interfaces | Div. de Recursos Humanos ↔ PRORH |
| Evidências | 1780963200048, 1780963200065, 1780963200066, 1780963200027, pb-rh |
| Lacunas | passos, formulario, prazo, kpi, interface_setorial |
| Justificativa | O fluxo genérico de e-Protocolo já está coberto por DRH-01; falta evidência específica por tipo de demanda (licença, afastamento, progressão) para justificar POP(s) dedicado(s) sem duplicar DRH-01. Recomenda-se coletar exemplos por tipo antes de desdobrar. |

## 3. Lacunas do setor

- Não há POP dedicado ao registro e apuração de frequência, apenas referências dentro do playbook geral (DRH-00) e normas isoladas
- Vigência da Lei nº 6.174/1970 não confirmada frente a alterações posteriores
- Fluxo de instrução de processos de RH (DRH-01) não distingue os passos específicos por tipo de demanda (licença, afastamento, progressão)
- Responsável (função) pelos processos de RH não definido nos POPs até este lote

## 4. Lições propostas

| Lição | Regra proposta | Exemplo |
|---|---|---|
| O acervo do Canvas registrou o mesmo manual de fluxos de RH em duas pastas diferentes ('RH' e 'Fluxos Internos'), como se fossem entradas distintas, além de duas versões (v2.0 e v3.0). | Ao consolidar entradas para diagnóstico, tratar cópias do mesmo arquivo (mesmo nome/conteúdo) em pastas diferentes como uma única fonte de evidência para fins de contagem de maturidade e cobertura, mantendo apenas o registro de origem múltipla como observação. | DRH, entradas 1780963200048/1780963200065/1780963200066 |

> Setor com forte base normativa (5 normas evidenciadas) mas processos operacionais (frequência, instrução por tipo de demanda) ainda pouco desdobrados em POPs próprios; DRH-02 e DRH-03 ficam sugeridos para geração/aprofundamento em lote futuro.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/DRH.json` (diretrizes v1.0)._
