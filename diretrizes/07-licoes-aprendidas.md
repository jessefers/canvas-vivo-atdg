---
id: diretriz-07
titulo: Lições aprendidas (log append-only)
versao: "1.24"
atualizado_em: "2026-09-03"
---

# 07 — Lições aprendidas

Log **append-only**. Somente lições com `status: aprovada` são injetadas nos prompts dos agentes e do app. Ids sequenciais `L-NNN`. Nunca editar linhas anteriores: para reverter, registrar nova lição com `substitui: L-NNN`.

## Regras vigentes (aprovadas)

| id | data | origem | lição | regra | status |
|---|---|---|---|---|---|
| L-001 | 2026-09-02 | curador | POPs anteriores citavam servidores pelo nome, expondo dados pessoais em documentos amplamente distribuídos. | Referir sempre função/cargo; nomes apenas no bloco 13 (Validação), com anuência (LGPD). | aprovada |
| L-002 | 2026-09-02 | curador | Passos compostos ("conferir e lançar") dificultam a atribuição de responsável e a medição. | Um passo = uma ação; ações compostas viram passos distintos. | aprovada |
| L-003 | 2026-09-02 | curador | Interfaces com outros setores apareciam só no texto e sumiam do fluxograma. | Cada linha do mapa de contexto gera um elemento `captura` no BPMN e um passo na raia de destino. | aprovada |
| L-004 | 2026-09-02 | curador | Manuais regenerados do zero perdiam ajustes validados pelo setor. | Nunca regenerar POP existente: aplicar patch com changelog, fontes e versão. | aprovada |
| L-005 | 2026-09-02 | curador | Entradas do Canvas repetiam documentos com versões duplicadas ("(2)", "cópia", "teste"). | No diagnóstico, agrupar versões do mesmo documento e registrar lacuna `versao_documento`. | aprovada |
| L-006 | 2026-09-02 | curador | Códigos legados (CON-01, CTR-01, Almoxarifado 01–08) já circulam no manual institucional. | Preservar códigos legados como códigos de processo; não renumerar. | aprovada |
| L-007 | 2026-09-02 | curador | Referências externas (UFPR, UFABC, UNILA, IFPR) foram tratadas como norma em rascunhos. | Referência Externa é benchmark; normativa do POP só cita atos da Unioeste, do Estado do Paraná ou federais aplicáveis. | aprovada |
| L-008 | 2026-09-03 | lote ALM | Playbooks multiprocesso (ex.: ALM-00 + ALM-01..08) nascem do scaffold sem herdar gatilho, entrada e saída do manual-fonte. | O scaffold de processos conhecidos deve herdar do manual-fonte, quando existir, gatilho e saída provisórios por processo (marcados como inferência). | aprovada |
| L-009 | 2026-09-03 | lote ALM | Processos de baixa frequência e altíssimo risco de conformidade (inventário geral, desfazimento) ficam no limiar de priorização porque a frequência pesa tanto quanto o risco. | Quando risco_conformidade ≥ 0,90 com evidência de auditoria externa, aplicar piso de prioridade 0,70 independentemente da frequência. | aprovada |
| L-010 | 2026-09-03 | lote DCOM | Passos do esqueleto frequentemente unem ações de responsáveis diferentes numa só frase (ponto e vírgula). | Todo passo com mais de um responsável no texto deve ser desdobrado em passos distintos (alterar o existente e adicionar os demais com apos_n); nunca manter responsável ambíguo. | aprovada |
| L-011 | 2026-09-03 | lote DCOM | Prazos de espera explícitos (aguardar N dias) aparecem fundidos com a ação seguinte, ocultando a pausa exigida por norma. | Todo prazo de espera explícito gera um elemento BPMN pausa dedicado e, quando houver condição de prosseguimento, uma decisão Sim/Não correspondente. | aprovada |
| L-012 | 2026-09-03 | lote DCOM | Siglas do setor (ex.: DDF) aparecem sem expansão nas fontes. | O glossário do POP registra a função observada da sigla e marca a expansão como pendente de confirmação; nunca presumir o significado. | aprovada |
| L-013 | 2026-09-03 | lote D2 | Fluxogramas entregues apenas como imagem (sem texto extraível) impedem a extração automática do passo a passo. | Registrar a lacuna passos e agendar revisão visual manual do fluxograma antes de elevar a maturidade do processo. | aprovada |
| L-014 | 2026-09-03 | lote D1 | Documentos de outras instituições (ex.: subprocesso financeiro de hospital) foram anexados ao acervo como exemplo metodológico, sem descrever processo real da Unioeste. | Registrar documentos de outras instituições apenas em ecossistema.benchmarks; nunca como evidência de processo próprio nem como normativa institucional. | aprovada |
| L-015 | 2026-09-03 | lote D1 | Manual PROGRAD duplicado em duas pastas do Canvas (mesmo arquivo-fonte). | Ao identificar duplicidade de arquivo-fonte, citar apenas o arquivo mestre nas fontes do POP e registrar a duplicata como ponto de atenção (risco de divergência de versão), sem gerar POP separado. | aprovada |
| L-016 | 2026-09-03 | lote C | Planilha real de controle (ex.: tempos de limpeza da DMC) foi registrada apenas como texto resumido. | Formalizar planilhas de controle já em uso como artefato do tipo documento, com campos-chave, mesmo sem sistema informatizado. | aprovada |
| L-017 | 2026-09-03 | lote C | Setores com apenas o playbook-esqueleto genérico (DST, DINF, DPAT, DATL, DSA) não têm evidência operacional. | Setor cujas fontes se resumem a um único registro genérico de playbook recebe POP-roteiro de coleta (status rascunho), nunca POP operacional completo. | aprovada |
| L-018 | 2026-09-03 | lote B | bpmn_delta.raias_add/elementos_add escala o tipo de mudança para major mesmo em POPs inferidos que deveriam permanecer rascunho. | Em POPs sem evidência, reconstruir o fluxograma com bpmn_delta.regenerar_de_passos (raias derivadas do responsável de cada passo e capturas do mapa de contexto); reservar a reconstrução manual para POPs evidenciados. | aprovada |
| L-019 | 2026-09-03 | lote B | Responsável do processo 'A definir' impede a promoção automática a em_validacao mesmo com passos completos. | Em setores sem entradas no Canvas, preencher o responsável por função em cada passo, mas manter identificacao.responsavel 'A definir' até validação formal, preservando a distinção entre POP evidenciado e inferido. | aprovada |

## Propostas pendentes

| id | data | origem | lição | regra proposta | status |
|---|---|---|---|---|---|













## Rejeitadas

| id | data | origem | lição | motivo da rejeição | status |
|---|---|---|---|---|---|
