---
id: diag-dcen-20260903
setor_codigo: S13-DCEN
data: "2026-09-03T02:00:00Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Direção de Centro (`S13-DCEN`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 2 entrada(s) do Canvas (hash `cacc150654c0…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Ensino, Pesquisa e Extensão (Centro) |
| Subdomínios | Representação institucional do Centro, Delegação de competências às Assessorias (área, ensino e extensão), Condução e deliberação do Conselho de Centro, Articulação do ensino com a PROGRAD e da extensão com a PROEX |
| Contextos vizinhos | CCSA — Direção de Centro, CECE — Direção de Centro, Colegiado de Curso, Direção Geral de Campus, PROGRAD, PROEX |
| Sistemas | e-Protocolo |
| Normas recorrentes | Estatuto (Res. 017/99-COU) art. 37 |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.54 | DCEN-00 | Visão geral — Direção de Centro (competências gerais) | processo | 3 | 0.6 | 0.5 | 0.5 | 0.75 | coletar_mais | pop-dcen-00 |

### DCEN-00 — Visão geral — Direção de Centro (competências gerais)

Competências do(a) Diretor(a) de Centro e das Assessorias de área, de ensino e de extensão: representação institucional, indicação de representantes, delegação de atividades, condução e deliberação do Conselho de Centro e articulação do ensino com a PROGRAD e da extensão com a PROEX (art. 37 do Estatuto), aplicável de forma transversal às Direções dos Centros do Campus.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de representação, indicação de representante, delegação de atividade ou deliberação de matéria do Conselho de Centro |
| Saída | Centro representado, representantes designados, deliberações do Conselho de Centro registradas e demandas de ensino/extensão articuladas com PROGRAD/PROEX |
| Atores | Diretor(a) de Centro, Assessoria de Ensino/Extensão do Centro, Conselho de Centro |
| Sistemas | e-Protocolo |
| Artefatos | Mapeamento de tarefas da Direção de Centro, Ata do Conselho de Centro, Edital de convocação do Conselho de Centro |
| Interfaces | PROGRAD, PROEX, Colegiado de Curso, Direção Geral de Campus |
| Evidências | pb-direcao-centro, 1780963200033 |
| Lacunas | formulario |
| Justificativa | POP transversal completado nesta rodada (v1.0.0, em_validação) com 8 passos (incluindo delegação às Assessorias e deliberação do Conselho de Centro), decisão, KPIs, contingência e mapa de contexto, a partir do mapeamento de tarefas da Direção de Centro (art. 37); resta confirmar com as Direções de Centro a periodicidade e o quórum regimentais do Conselho de Centro. |

## 3. Lacunas do setor

- Regimento do Conselho de Centro (periodicidade e quórum) não localizado nas fontes consultadas
- Instrumento de substituição do Diretor(a) de Centro em caso de impedimento não evidenciado
- Distinção fina de competências entre as Assessorias de área, de ensino e de extensão não detalhada nas fontes

## 4. Lições propostas

— Nenhuma

> POP transversal aplicável às Direções de Centro do Campus (CCSA e CECE); as particularidades de cada Centro constam dos playbooks próprios CCSA-00 e CECE-00.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/DCEN.json` (diretrizes v1.0)._
