---
id: diag-dst-20260903
setor_codigo: S03.02-DST
data: "2026-09-03T01:59:01Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Div. de Segurança e Transportes (`S03.02-DST`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 1 entrada(s) do Canvas (hash `dc6392f2f1f0…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Infraestrutura e Serviços |
| Subdomínios | A definir (playbook em construção) |
| Contextos vizinhos | A definir |
| Sistemas | — |
| Normas recorrentes | — |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.43 | DST-00 | Visão geral — Div. de Segurança e Transportes (roteiro de coleta) | processo | 0 | 0.4 | 0.3 | 0.4 | 0.05 | coletar_mais | DST-00 |

### DST-00 — Visão geral — Div. de Segurança e Transportes (roteiro de coleta)

Setor sem mapeamento de processos no Canvas; o único registro é o playbook-esqueleto genérico apontando para o levantamento inicial de atividades, fluxos e normas aplicáveis.

| Campo | Valor |
|---|---|
| Gatilho | A definir |
| Saída | A definir |
| Atores | A definir |
| Sistemas | — |
| Artefatos | — |
| Interfaces | — |
| Evidências | pb-seguranca-transportes |
| Lacunas | responsavel, normativa, gatilho, entrada, saida, passos, sistema, formulario, prazo, kpi, contingencia, interface_setorial |
| Justificativa | Nenhuma entrada real do Canvas além do playbook-esqueleto genérico ('classe PLAYBOOK', sem procedimento específico); o POP foi tratado como roteiro de coleta (contingência e checklist de levantamento), mantendo o status rascunho até que atividades reais sejam mapeadas. |

## 3. Lacunas do setor

- sem entradas no Canvas

## 4. Lições propostas

| Lição | Regra proposta | Exemplo |
|---|---|---|
| Setores como DST, DINF, DPAT, DATL e DSA têm apenas um registro de playbook-esqueleto genérico (mesmo texto padrão 'A documentar: levantar atividades...'), sem nenhuma entrada real do Canvas. | Quando o hash de fontes de um setor corresponder apenas a um único registro de classe 'PLAYBOOK' genérico e sem procedimento específico, tratar o patch como roteiro de coleta (sistema/artefato nos 3 passos genéricos, contingência e checklist de levantamento, responsável 'A definir'), com tipo_mudanca 'minor' e sem promover o status — nunca como POP operacional completo. | DST-00, DINF-00, DPAT-00, DATL-00, DSA-00 |

> Setor ainda não mapeado — roteiro de coleta. A mesma situação se repete em DINF, DPAT, DATL e DSA (ver lição proposta).

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/DST.json` (diretrizes v1.0)._
