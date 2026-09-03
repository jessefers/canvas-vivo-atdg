---
id: diag-dg-20260903
setor_codigo: S01-DG
data: "2026-09-03T02:02:00Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Direção Geral de Campus (`S01-DG`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 5 entrada(s) do Canvas (hash `b9b63cf1a01f…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Governança e Direção do Campus |
| Subdomínios | Referência normativa institucional (Estatuto e Instruções de Serviço do GRE), Aplicação da norma a casos concretos |
| Contextos vizinhos | ATDG — Assessoria Técnica da Direção Geral, Gabinete da Reitoria (GRE), Setores do Campus |
| Sistemas | e-Protocolo, OneDrive ATDG |
| Normas recorrentes | Resolução nº 017/1999-COU (Estatuto da Unioeste); Resolução nº 194/2024-COU (altera a Resolução nº 017/1999-COU); Instruções de Serviço do Gabinete da Reitoria (GRE) |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.60 | DG-01 | Aplicação do Estatuto e das Instruções de Serviço do GRE | processo | 1 | 0.7 | 0.35 | 0.6 | 0.65 | coletar_mais | pop-dg-01 |
| 0.55 | DG-00 | Visão geral — Direção Geral de Campus | processo | 2 | 0.65 | 0.4 | 0.5 | 0.7 | coletar_mais | pop-dg-00 |

### DG-01 — Aplicação do Estatuto e das Instruções de Serviço do GRE

Aplica, caso a caso, o Estatuto ou Instrução de Serviço do GRE a situações concretas do Campus, mediante parecer técnico da ATDG e decisão da Direção Geral.

| Campo | Valor |
|---|---|
| Gatilho | Situação concreta do Campus que exige aplicação ou interpretação do Estatuto ou de Instrução de Serviço do GRE |
| Saída | Despacho/portaria de aplicação da norma e precedente registrado |
| Atores | Setor demandante, Assessoria Técnica da Direção Geral (ATDG), Direção Geral do Campus |
| Sistemas | e-Protocolo, OneDrive ATDG |
| Artefatos | Parecer técnico de enquadramento normativo, Despacho/portaria de aplicação da norma |
| Interfaces | Assessoria Técnica da Direção Geral (ATDG), Direção Geral do Campus |
| Evidências | pb-direcao-geral, 1780963200023, 1780963200024, 1780963200028, 1780963200029 |
| Lacunas | formulario, prazo |
| Justificativa | Processo codificado no manual institucional da ATDG; POP completo elaborado (v1.0.0, em_validacao) a partir do mesmo acervo normativo de DG-00, com fluxo de parecer técnico e decisão da Direção Geral. |

### DG-00 — Visão geral — Direção Geral de Campus

Mantém e disponibiliza o acervo normativo institucional (Estatuto e Instruções de Serviço do GRE) e responde a consultas de setores sobre sua aplicação, sob validação da Direção Geral.

| Campo | Valor |
|---|---|
| Gatilho | Norma institucional nova, revisada ou consultada identificada pela Direção Geral, pela ATDG ou por setor do Campus |
| Saída | Acervo normativo consolidado e resposta formal à consulta |
| Atores | Setor demandante, Assessoria Técnica da Direção Geral (ATDG), Direção Geral do Campus |
| Sistemas | e-Protocolo, OneDrive ATDG |
| Artefatos | Acervo normativo da ATDG, Nota técnica/orientação normativa |
| Interfaces | Assessoria Técnica da Direção Geral (ATDG), Direção Geral do Campus |
| Evidências | pb-direcao-geral, 1780963200023, 1780963200024, 1780963200028, 1780963200029 |
| Lacunas | formulario, prazo |
| Justificativa | Processo de referência normativa já elaborado em POP completo (playbook v1.0.0, em_validacao), com passos, responsáveis, decisão e mapa de contexto definidos a partir das entradas do Canvas (Estatuto Res. 017/99 e 194/2024-COU; Instruções de Serviço GRE). |

## 3. Lacunas do setor

- Formulário/modelo padronizado de registro de consultas normativas não formalizado
- Prazos de resposta a consultas e de decisão normativa não normatizados

## 4. Lições propostas

— Nenhuma

> Diagnóstico do lote DG (2 processos) elaborado a partir de 5 entradas do Canvas (playbook e normas — Estatuto Res. 017/99 e 194/2024-COU; Instruções de Serviço GRE). Os 2 processos foram elaborados em POP completo (playbook DDD híbrido, v1.0.0, em_validacao) no lote B.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/DG.json` (diretrizes v1.0)._
