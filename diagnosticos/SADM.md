---
id: diag-sadm-20260903
setor_codigo: S03-SADM
data: "2026-09-03T01:59:01Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Sec. Administrativa — Geral (`S03-SADM`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 1 entrada(s) do Canvas (hash `e4b6eb4586a9…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Administração e Suprimentos |
| Subdomínios | Coordenação das divisões administrativas, Triagem e encaminhamento de demandas via e-Protocolo |
| Contextos vizinhos | Direção Geral do Campus, Div. de Licitação, Div. de Recursos Humanos, Div. de Manutenção e Conservação, Div. de Almoxarifado, Div. de Compras |
| Sistemas | e-Protocolo |
| Normas recorrentes | Estrutura conforme organograma do Campus Foz (Coordenação Administrativa) |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.51 | SADM-00 | Playbook — Secretaria Administrativa (visão geral) | processo | 1 | 0.5 | 0.6 | 0.3 | 0.3 | coletar_mais | SADM-00 |

### SADM-00 — Playbook — Secretaria Administrativa (visão geral)

Coordenação das divisões administrativas do Campus e triagem/encaminhamento de demandas administrativas via e-Protocolo.

| Campo | Valor |
|---|---|
| Gatilho | Recebimento de demanda administrativa própria ou de outro setor do campus |
| Saída | Demanda atendida pela divisão responsável e resultado informado ao solicitante |
| Atores | Coordenador(a) Administrativo(a), Direção Geral |
| Sistemas | e-Protocolo |
| Artefatos | Demanda administrativa (e-Protocolo), Consolidado de status das demandas |
| Interfaces | Sec. Administrativa — Geral ↔ Div. de Licitação, Sec. Administrativa — Geral ↔ Div. de Recursos Humanos, Sec. Administrativa — Geral ↔ Div. de Manutenção e Conservação, Sec. Administrativa — Geral ↔ Direção Geral |
| Evidências | pb-sec-administrativa |
| Lacunas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Justificativa | Processo de coordenação/roteamento (não finalístico), com criticidade e risco moderados; o próprio playbook não nomeia uma função específica de coordenação, apenas a estrutura organizacional ('Coordenação Administrativa'), o que limita a maturidade mensurável. Recomenda-se confirmar a função responsável em campo antes de aprovar o POP. |

## 3. Lacunas do setor

- Nenhuma entrada do Canvas nomeia a função responsável pela coordenação da Secretaria Administrativa (apenas a estrutura 'Coordenação Administrativa' no organograma)
- Não há evidência de prazo-padrão para atendimento das demandas encaminhadas às divisões
- Interfaces com Div. de Almoxarifado e Div. de Compras citadas na descrição do setor mas sem fluxo próprio evidenciado

## 4. Lições propostas

— Nenhuma

> SADM-00 é a visão geral que aponta para os playbooks das divisões (Almoxarifado, Compras, Licitação, RH, Manutenção e Conservação); o responsável foi inferido como 'Coordenador(a) Administrativo(a)' a partir da normativa já registrada ('Coordenação Administrativa'), sem criar título não evidenciado. Recomenda-se validação em campo desse título com a Direção Geral.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/SADM.json` (diretrizes v1.0)._
