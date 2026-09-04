---
id: diag-sfin-20260903
setor_codigo: S04-SFIN
data: "2026-09-03T01:41:28Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Sec. Financeira — Geral (`S04-SFIN`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 1 entrada(s) do Canvas (hash `bc32dbe5defa…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Finanças e Orçamento |
| Subdomínios | Coordenação de despesas e diárias do campus, Interlocução com Div. de Finanças e Div. de Contabilidade |
| Contextos vizinhos | Div. de Finanças, Div. de Contabilidade, Direção Geral de Campus, PRAF (Pró-Reitoria de Administração e Finanças) |
| Sistemas | e-Protocolo |
| Normas recorrentes | Estrutura conforme organograma do Campus Foz (Secretaria Financeira) |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.43 | SFIN-00 | Visão geral — Secretaria Financeira | processo | 1 | 0.45 | 0.3 | 0.4 | 0.15 | coletar_mais | SFIN-00 |

### SFIN-00 — Visão geral — Secretaria Financeira

Coordenação, pela Secretaria Financeira, das divisões de Finanças e de Contabilidade e roteamento de demandas financeiras do campus via e-Protocolo.

| Campo | Valor |
|---|---|
| Gatilho | A definir |
| Saída | A definir |
| Atores | Secretaria Financeira, Div. de Finanças, Div. de Contabilidade |
| Sistemas | e-Protocolo |
| Artefatos | — |
| Interfaces | Div. de Finanças, Div. de Contabilidade, Direção Geral de Campus |
| Evidências | pb-sec-financeira |
| Lacunas | responsavel, gatilho, entrada, saida, sistema, interface_setorial |
| Justificativa | Único registro é um roteiro de coordenação de alto nível, sem evidência operacional própria; a Secretaria Financeira já delega a execução detalhada às divisões subordinadas (DFIN, com playbook consolidado; DCONT, ainda não mapeada). |

## 3. Lacunas do setor

- Setor mapeado apenas em nível de coordenação (playbook-roteiro); sem evidências operacionais próprias no Canvas além do apontamento às divisões subordinadas
- Responsável nominal (função) pela Secretaria Financeira ainda não identificado

## 4. Lições propostas

— Nenhuma

> SFIN-00 permanece como POP-roteiro de coleta (visão geral de coordenação); a substância operacional financeira do campus está documentada nos POPs da Div. de Finanças (DFIN) e, quando mapeada, da Div. de Contabilidade (DCONT).

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/SFIN.json` (diretrizes v1.0)._
