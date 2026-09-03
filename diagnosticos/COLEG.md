---
id: diag-coleg-20260903
setor_codigo: S12-COLEG
data: "2026-09-03T02:00:00Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Colegiado de Curso (`S12-COLEG`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 15 entrada(s) do Canvas (hash `7175dc7d7cb8…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Colegiados e Cursos |
| Subdomínios | Comunicação, atendimento e protocolo (agente universitário), Gestão acadêmica e órgãos colegiados (coordenação de curso), Coordenação de estágio, Coordenação de TCC |
| Contextos vizinhos | CCSA — Direção de Centro, CECE — Direção de Centro, Direção de Centro (competências gerais), PROGRAD, Biblioteca |
| Sistemas | Academus, e-Protocolo, Microsoft Forms |
| Normas recorrentes | Estatuto (Res. 017/99-COU) art. 41; Lei nº 11.788/2008; Regimento de Cursos; Regulamentos de Estágio e TCC dos cursos |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.73 | COLEG-00 | Visão geral — Colegiado de Curso (transversal) | processo | 3 | 0.85 | 0.8 | 0.7 | 0.75 | gerar_pop | pop-coleg-00 |
| 0.72 | COLEG-03 | Coordenação de estágio | processo | 2 | 0.85 | 0.7 | 0.8 | 0.4 | gerar_pop | — |
| 0.70 | COLEG-02 | Gestão acadêmica da coordenação de curso | processo | 2 | 0.8 | 0.85 | 0.6 | 0.4 | gerar_pop | — |
| 0.59 | COLEG-04 | Coordenação de TCC | processo | 2 | 0.7 | 0.6 | 0.5 | 0.4 | coletar_mais | — |
| 0.57 | COLEG-01 | Rotinas do Agente Universitário do Colegiado | processo | 1 | 0.5 | 0.8 | 0.3 | 0.35 | coletar_mais | — |

### COLEG-00 — Visão geral — Colegiado de Curso (transversal)

Consolida as rotinas dos colegiados e coordenações de curso, estágio e TCC e do agente universitário: comunicação e protocolo, condução do Colegiado e do NDE, gestão acadêmica no Academus, formalização de termos e bancas de estágio, e orientação, bancas e envio de TCC à Biblioteca.

| Campo | Valor |
|---|---|
| Gatilho | Solicitação de discente/docente/concedente, pauta do Colegiado/NDE ou marco do calendário acadêmico/cronograma de estágio e TCC |
| Saída | Atendimento, deliberações, gestão acadêmica, termos de estágio e TCC concluídos conforme o calendário acadêmico |
| Atores | Coordenador(a) de Curso, Agente Universitário do Colegiado, Coordenador(a) de Estágio, Coordenador(a) de TCC, Colegiado/NDE |
| Sistemas | Academus, e-Protocolo |
| Artefatos | Pauta e ata do Colegiado/NDE, Termo de compromisso de estágio, Ata de banca de TCC |
| Interfaces | PROGRAD, Biblioteca, Direção de Centro, Concedentes de estágio |
| Evidências | pb-colegiado, 1780963200002, 1780963200003, 1780963200004, 1780963200005, 1780963200006, 1780963200007, 1780963200008, 1780963200009, 1780963200010, 1780963200018, 1780963200019, 1780963200020, 1780963200021, 1780963200032 |
| Lacunas | versao_documento, dados_pessoais_lgpd |
| Justificativa | POP transversal completado nesta rodada (v1.0.0, em_validação) com 8 passos, 2 decisões, KPIs, contingência e mapa de contexto, a partir de 15 entradas (questionários, consolidação em aba DADOS e fluxogramas por função). Dada a alta criticidade e frequência (gestão acadêmica, estágio com exposição legal, TCC), recomenda-se desdobrar em POPs específicos por função (COLEG-01 a COLEG-04, abaixo) antes da promoção a 'aprovado'. |

### COLEG-03 — Coordenação de estágio

Articulação com instituições concedentes, formalização de termos de compromisso e aditivos, organização de bancas de estágio supervisionado e observância do calendário e da legislação de estágio.

| Campo | Valor |
|---|---|
| Gatilho | Solicitação de estágio de discente ou concedente, ou vencimento/alteração de termo de compromisso vigente |
| Saída | Termo de compromisso ou aditivo formalizado e banca de estágio supervisionado realizada |
| Atores | Coordenador(a) de Estágio, Colegiado de Curso |
| Sistemas | Academus |
| Artefatos | Termo de compromisso de estágio, Aditivo de termo de compromisso, Ata de banca de estágio |
| Interfaces | Concedentes de estágio (hotéis, escolas, NRE, SEED, Itaipu), Colegiado de Curso |
| Evidências | 1780963200007, 1780963200008, 1780963200020 |
| Lacunas | sistema, prazo, kpi, contingencia, interface_setorial |
| Justificativa | Processo de maior exposição legal do lote (Lei nº 11.788/2008), com articulação documentada com concedentes variados (hotéis, escolas, NRE, SEED, Itaipu) e fluxograma próprio; recomenda-se POP específico com o passo a passo de formalização e rescisão de termos e a condução de bancas de estágio. |

### COLEG-02 — Gestão acadêmica da coordenação de curso

Gestão acadêmica no Academus (planos de ensino, matrícula, notas, horários e distribuição de disciplinas), condução do Colegiado e do NDE e deliberações via e-Protocolo (transferências, segunda chamada, dispensa, exercício domiciliar), conforme o art. 41 do Estatuto e o Regimento de Cursos.

| Campo | Valor |
|---|---|
| Gatilho | Pauta de reunião do Colegiado/NDE, marco do calendário acadêmico ou solicitação de deliberação |
| Saída | Gestão acadêmica do período concluída no Academus e deliberações do Colegiado/NDE registradas em ata |
| Atores | Coordenador(a) de Curso, Colegiado/NDE, Assistente da coordenação |
| Sistemas | Academus, e-Protocolo |
| Artefatos | Pauta e ata do Colegiado/NDE, Plano de ensino, Ata de deliberação |
| Interfaces | PROGRAD, Direção de Centro, Docentes |
| Evidências | 1780963200004, 1780963200005, 1780963200006, 1780963200019, 1780963200032 |
| Lacunas | sistema, prazo, kpi, contingencia, interface_setorial |
| Justificativa | Função mais detalhadamente evidenciada do lote: questionário respondido, planilha de consolidação com aba DADOS (percentuais por bloco de atividade) e mapeamento de tarefas da coordenação por art. 41, além de fluxograma próprio. Alta criticidade e frequência (matrícula, notas, deliberações do Colegiado/NDE); recomenda-se POP específico com o passo a passo das deliberações e da gestão acadêmica no Academus. |

### COLEG-04 — Coordenação de TCC

Indicação de orientadores, organização de bancas e defesas, editais, atas e declarações, lançamento de notas e frequências no Academus, envio da versão final à Biblioteca e cronograma anual de TCC.

| Campo | Valor |
|---|---|
| Gatilho | Abertura do cronograma anual de TCC ou solicitação de orientação/defesa de discente |
| Saída | TCC defendido, notas lançadas no Academus e versão final enviada à Biblioteca |
| Atores | Coordenador(a) de TCC, Colegiado de Curso |
| Sistemas | Academus |
| Artefatos | Edital de TCC, Ata de banca de defesa, Declaração de entrega à Biblioteca |
| Interfaces | Biblioteca, Colegiado de Curso |
| Evidências | 1780963200009, 1780963200010, 1780963200021 |
| Lacunas | sistema, prazo, kpi, contingencia, interface_setorial |
| Justificativa | Rotina bem descrita no questionário respondido (indicação de orientadores, editais, atas, envio à Biblioteca) e em fluxograma próprio, com exposição normativa menor que a do estágio; recomenda-se complementar com o Regulamento de TCC de cada curso antes de gerar o POP específico. |

### COLEG-01 — Rotinas do Agente Universitário do Colegiado

Comunicação e atendimento a discentes, docentes e concedentes, gestão de documentos e protocolo (e-Protocolo) e apoio acadêmico às coordenações de curso, estágio e TCC, exercidos pelo Agente Universitário do Colegiado.

| Campo | Valor |
|---|---|
| Gatilho | Solicitação de discente, docente, concedente ou coordenação que demande atendimento, protocolo ou apoio acadêmico |
| Saída | Atendimento realizado, documento protocolado e apoio acadêmico prestado às coordenações |
| Atores | Agente Universitário do Colegiado, Coordenador(a) de Curso |
| Sistemas | e-Protocolo, Academus |
| Artefatos | Protocolo/registro de atendimento |
| Interfaces | Discentes e docentes, Concedentes de estágio, Coordenações de curso, estágio e TCC |
| Evidências | 1780963200002, 1780963200003, 1780963200018 |
| Lacunas | responsavel, sistema, prazo, kpi, contingencia |
| Justificativa | Rotina evidenciada em dois questionários de mapeamento (mesmo instrumento, respostas e cópia — tratados como uma única evidência, lição L-005) e em fluxograma próprio entregue como imagem sem texto extraível; já resumida em COLEG-00, mas sem POP operacional detalhado. Recomenda-se revisar visualmente o fluxograma antes de gerar o POP específico. |

## 3. Lacunas do setor

- Fluxogramas por função (agente universitário, coordenador de curso, de estágio e de TCC) fornecidos como imagem, sem texto extraível — requerem revisão visual detalhada
- Regulamentos de estágio e de TCC variam entre cursos/colegiados e não foram individualmente coletados neste lote
- Cópias e planilhas de resposta vazias dos questionários de mapeamento foram identificadas e tratadas como uma única evidência por função (lição L-005)
- Política de tratamento de dados pessoais de discentes/docentes no Academus não formalizada neste levantamento

## 4. Lições propostas

| Lição | Regra proposta | Exemplo |
|---|---|---|
| Fluxogramas entregues apenas como imagem incorporada ao documento (sem texto extraível) impedem a extração automática do passo a passo do processo. | Sempre que um fluxograma for entregue apenas como imagem, registrar a lacuna 'passos' no processo correspondente e agendar revisão visual manual antes de elevar sua maturidade além do nível já coberto pelo questionário. | COLEG-01 a COLEG-04 — fluxogramas em .docx sem texto extraível (fontes 1780963200018 a 1780963200021) |

> Questionários e planilhas em branco (apenas coluna 'ID') do mesmo instrumento foram agrupados como uma única evidência por função, conforme a lição L-005, evitando dupla contagem na qualificação de maturidade e cobertura.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/COLEG.json` (diretrizes v1.0)._
