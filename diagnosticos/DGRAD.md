---
id: diag-dgrad-20260903
setor_codigo: S05.02-DGRAD
data: "2026-09-03T01:41:28Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Div. de Graduação (`S05.02-DGRAD`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 3 entrada(s) do Canvas (hash `019626e05ffd…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Gestão Acadêmica |
| Subdomínios | Tramitação de processos de ensino de graduação no e-Protocolo (PROGRAD) |
| Contextos vizinhos | PROGRAD (Pró-Reitoria de Ensino), Colegiado de Curso, Direção de Centro, Coordenação Acadêmica — Geral |
| Sistemas | e-Protocolo |
| Normas recorrentes | Manual de Fluxos e-Protocolo — PROGRAD/Unioeste |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.63 | DGRAD-01 | Fluxos e-Protocolo — Ensino (PROGRAD) | processo | 2 | 0.75 | 0.5 | 0.65 | 0.6 | coletar_mais | DGRAD-01 |
| 0.60 | DGRAD-00 | Visão geral — ensino de graduação (PROGRAD) | processo | 2 | 0.7 | 0.5 | 0.6 | 0.55 | coletar_mais | DGRAD-00 |

### DGRAD-01 — Fluxos e-Protocolo — Ensino (PROGRAD)

Manual da Comissão e-Protocolo com os fluxos de ensino sob a PROGRAD: alteração de resoluções/regulamentos, PPP, reconhecimento/renovação de curso, regulamentos de estágio/TCC/internato, projetos de ensino e monitorias.

| Campo | Valor |
|---|---|
| Gatilho | Abertura de processo de ensino de graduação no e-Protocolo |
| Saída | Processo deliberado pela PROGRAD, com arquivamento ou retorno para ajustes |
| Atores | Colegiado de Curso, Direção de Centro, Coordenação Acadêmica, PROGRAD |
| Sistemas | e-Protocolo |
| Artefatos | Processo de ensino (PPP/regulamento/projeto/monitoria) |
| Interfaces | Direção de Centro, PROGRAD |
| Evidências | 1780963200038, 1780963200064 |
| Lacunas | sistema, interface_setorial, versao_documento |
| Justificativa | Fonte primária (manual oficial da PROGRAD), com maior detalhamento dos tipos de processo de ensino; há cópia duplicada do mesmo arquivo no acervo (ver lição proposta). |

### DGRAD-00 — Visão geral — ensino de graduação (PROGRAD)

Guia consolidado da tramitação dos processos de ensino de graduação (PPP, reconhecimento de curso, regulamentos, projetos de ensino e monitorias) no e-Protocolo (PROGRAD).

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de tramitar processo de ensino de graduação |
| Saída | Processo deliberado pela PROGRAD e arquivado/publicado |
| Atores | Colegiado de Curso, Direção de Centro, Coordenação Acadêmica, PROGRAD |
| Sistemas | e-Protocolo |
| Artefatos | Processo de ensino (PPP/regulamento/projeto/monitoria) |
| Interfaces | Direção de Centro, PROGRAD |
| Evidências | pb-graduacao |
| Lacunas | sistema, interface_setorial, versao_documento |
| Justificativa | Visão consolidada alinhada ao manual oficial da PROGRAD (DGRAD-01); alta criticidade por afetar credenciamento/reconhecimento de cursos. |

## 3. Lacunas do setor

- Responsável nominal (função) da Div. de Graduação ainda não formalizado
- SLA de deliberação da PROGRAD e do Colegiado de Curso não evidenciado

## 4. Lições propostas

| Lição | Regra proposta | Exemplo |
|---|---|---|
| O manual de Fluxos e-Protocolo — Ensino (PROGRAD) está duplicado no acervo do Canvas em duas pastas distintas ('Ensino' e 'Fluxos Internos'), com o mesmo arquivo-fonte. | Ao identificar duplicidade de arquivo-fonte entre pastas do Canvas, registrar nas fontes do POP apenas o arquivo mestre e citar a duplicata como ponto de atenção (risco de divergência de versão), sem gerar um processo/POP separado para a cópia. | DGRAD-01 — entradas 1780963200038 (original) e 1780963200064 (cópia) |

> Nenhum processo adicional de ensino foi evidenciado no Canvas além dos dois já mapeados em POP; a entrada 1780963200064 é cópia idêntica de 1780963200038 e não constitui processo distinto. Ambos pontuam 'coletar_mais' pela fórmula (prioridade < 0,70), mas, por integrarem o esqueleto já existente do Lote D1, seus POPs são completados nesta leva conforme escopo definido.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/DGRAD.json` (diretrizes v1.0)._
