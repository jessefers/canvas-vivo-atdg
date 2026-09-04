---
id: diag-dpat-20260903
setor_codigo: S03.05-DPAT
data: "2026-09-03T01:59:01Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Div. de Patrimônio e Equipamentos (`S03.05-DPAT`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 1 entrada(s) do Canvas (hash `4aaf5aa16ed9…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Suprimentos e Materiais |
| Subdomínios | A definir (playbook em construção — tombamento, controle e desfazimento de bens) |
| Contextos vizinhos | A definir |
| Sistemas | — |
| Normas recorrentes | A definir (normas de patrimônio; TCE-PR) |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.49 | DPAT-00 | Visão geral — Div. de Patrimônio e Equipamentos (roteiro de coleta) | processo | 0 | 0.5 | 0.3 | 0.55 | 0.05 | coletar_mais | DPAT-00 |

### DPAT-00 — Visão geral — Div. de Patrimônio e Equipamentos (roteiro de coleta)

Setor sem mapeamento de processos no Canvas; o único registro é o playbook-esqueleto genérico, que já cita tombamento, controle e desfazimento de bens como escopo provável, sem procedimento detalhado.

| Campo | Valor |
|---|---|
| Gatilho | A definir |
| Saída | A definir |
| Atores | A definir |
| Sistemas | — |
| Artefatos | — |
| Interfaces | — |
| Evidências | pb-patrimonio |
| Lacunas | responsavel, gatilho, entrada, saida, passos, sistema, formulario, prazo, kpi, contingencia, interface_setorial |
| Justificativa | Nenhuma entrada real do Canvas além do playbook-esqueleto genérico; risco de conformidade um pouco mais alto que os demais setores em construção por envolver controle patrimonial sujeito a fiscalização do TCE-PR. POP tratado como roteiro de coleta, mantendo o status rascunho. |

## 3. Lacunas do setor

- sem entradas no Canvas

## 4. Lições propostas

| Lição | Regra proposta | Exemplo |
|---|---|---|
| O campo de normativa do esqueleto de DPAT-00 ('A definir (normas de patrimônio; TCE-PR)') foi persistido como dois itens de array separados por vírgula ('A definir (normas de patrimônio' e 'TCE-PR)'), quebrando o parêntese ao meio. | Ao extrair automaticamente campos de normativa em texto livre para o esqueleto inicial, usar apenas ';' como separador de múltiplas normas (nunca ',') e validar que parênteses abertos sejam fechados no mesmo item antes de gravar o array. | pops/DPAT/DPAT-00.pop.json, identificacao.normativa |

> Setor ainda não mapeado — roteiro de coleta. Identificado defeito de formatação herdado do esqueleto original em identificacao.normativa (ver lição proposta); não corrigido neste lote por estar fora do escopo de campos autorizados para patch (campos.normativa não faz parte da lista de campos editáveis por este protocolo).

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/DPAT.json` (diretrizes v1.0)._
