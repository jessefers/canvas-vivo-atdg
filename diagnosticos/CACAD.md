---
id: diag-cacad-20260903
setor_codigo: S05-CACAD
data: "2026-09-03T01:41:28Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Coordenação Acadêmica — Geral (`S05-CACAD`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 2 entrada(s) do Canvas (hash `6a3a392123f2…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Gestão Acadêmica |
| Subdomínios | Tramitação de atividades de extensão no e-Protocolo (PROEX) |
| Contextos vizinhos | PROEX (Pró-Reitoria de Extensão), Div. de Pós-Graduação, Div. de Graduação, Div. de Assistência Estudantil, Direção Geral de Campus |
| Sistemas | e-Protocolo |
| Normas recorrentes | Manual de Fluxos e-Protocolo — PROEX/Unioeste |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.56 | CACAD-01 | Fluxos e-Protocolo — Extensão (PROEX) | processo | 2 | 0.6 | 0.5 | 0.55 | 0.6 | coletar_mais | CACAD-01 |
| 0.55 | CACAD-00 | Visão geral — extensão (e-Protocolo/PROEX) | processo | 2 | 0.6 | 0.5 | 0.5 | 0.55 | coletar_mais | CACAD-00 |

### CACAD-01 — Fluxos e-Protocolo — Extensão (PROEX)

Manual da Comissão e-Protocolo com os fluxos de abertura de atividades de extensão (programas, projetos, cursos e eventos), com e sem recursos, propostas por docente ou agente universitário, e atividades com fomento externo.

| Campo | Valor |
|---|---|
| Gatilho | Abertura de nova atividade de extensão pelo proponente |
| Saída | Atividade de extensão aprovada pela PROEX |
| Atores | Proponente/Coordenador da atividade, Coordenação Acadêmica, PROEX |
| Sistemas | e-Protocolo |
| Artefatos | Formulário de atividade de extensão |
| Interfaces | PROEX |
| Evidências | 1780963200039 |
| Lacunas | sistema, interface_setorial, versao_documento |
| Justificativa | Fonte primária (manual oficial da PROEX); maior detalhamento sobre modalidades e fomento externo que a visão geral. |

### CACAD-00 — Visão geral — extensão (e-Protocolo/PROEX)

Guia consolidado da tramitação de atividades de extensão (programas, projetos, cursos e eventos), com e sem recursos e com fomento externo, no e-Protocolo (PROEX).

| Campo | Valor |
|---|---|
| Gatilho | Proposição de atividade de extensão |
| Saída | Atividade de extensão aprovada/registrada na PROEX |
| Atores | Proponente/Coordenador da atividade, Coordenação Acadêmica, PROEX |
| Sistemas | e-Protocolo |
| Artefatos | Formulário de atividade de extensão |
| Interfaces | PROEX |
| Evidências | pb-coord-academica |
| Lacunas | sistema, interface_setorial, versao_documento |
| Justificativa | Visão consolidada com boa cobertura textual, alinhada ao manual oficial da PROEX (CACAD-01); recomenda-se completar o playbook. |

## 3. Lacunas do setor

- Responsável nominal (função) da Coordenação Acadêmica pela tramitação de extensão ainda não formalizado
- SLA de deliberação da PROEX não evidenciado

## 4. Lições propostas

— Nenhuma

> Nenhum processo adicional de extensão foi evidenciado no Canvas além dos dois já mapeados em POP (visão geral e fluxo detalhado PROEX). Ambos pontuam 'coletar_mais' pela fórmula (prioridade < 0,70), mas, por integrarem o esqueleto já existente do Lote D1, seus POPs são completados nesta leva conforme escopo definido.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/CACAD.json` (diretrizes v1.0)._
