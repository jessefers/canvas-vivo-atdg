---
id: diag-cece-20260903
setor_codigo: S08-CECE
data: "2026-09-03T02:00:00Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — CECE — Direção de Centro (`S08-CECE`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 2 entrada(s) do Canvas (hash `6b64a933856b…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Ensino, Pesquisa e Extensão (Centro) |
| Subdomínios | Articulação e governança do Centro, Gestão da base de contatos por função (colegiados, mestrados e laboratórios), Encaminhamento e acompanhamento de demandas via e-Protocolo |
| Contextos vizinhos | Colegiado de Curso, Direção de Centro (competências gerais), CCSA — Direção de Centro, Direção Geral de Campus |
| Sistemas | e-Protocolo |
| Normas recorrentes | Estatuto (Res. 017/99-COU) art. 37 e 41 |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.62 | CECE-00 | Visão geral — CECE — Direção de Centro | processo | 3 | 0.7 | 0.7 | 0.5 | 0.75 | coletar_mais | pop-cece-00 |

### CECE-00 — Visão geral — CECE — Direção de Centro

Articulação da Direção do Centro de Engenharias e Ciências Exatas com os colegiados de Ciência da Computação, Engenharia Elétrica, Engenharia Mecânica e Matemática, com os Mestrados (PPGEEC e PPGTGS) e com os laboratórios do Centro, manutenção da base de contatos por função e encaminhamento e acompanhamento das demandas do Centro.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de articulação com colegiados/mestrados/laboratórios, atualização da base de contatos ou encaminhamento de demanda do Centro |
| Saída | Base de contatos atualizada e demandas do Centro encaminhadas e acompanhadas até a resposta |
| Atores | Diretor(a) de Centro, Coordenador(a) de Curso |
| Sistemas | e-Protocolo |
| Artefatos | Lista de contatos por função do CECE, Ofício/memorando de encaminhamento de demanda do Centro |
| Interfaces | Colegiado de Curso, Direção Geral de Campus |
| Evidências | pb-cece, 1780963200013 |
| Lacunas | formulario, dados_pessoais_lgpd |
| Justificativa | POP completado nesta rodada (v1.0.0, em_validação) com 6 passos, responsável, decisão, KPIs, contingência e mapa de contexto, a partir da lista de contatos dos colegiados do Centro; restam o mapeamento das rotinas dos laboratórios e a política de tratamento dos dados pessoais de contato antes da promoção a 'aprovado'. |

## 3. Lacunas do setor

- Política de acesso e atualização da lista de contatos (dados pessoais) não formalizada
- Rotinas dos laboratórios do Centro ainda não mapeadas
- Periodicidade de validação dos contatos de colegiados e mestrados não normatizada

## 4. Lições propostas

— Nenhuma

> As rotinas específicas de gestão acadêmica, estágio e TCC de cada colegiado do CECE são tratadas no POP transversal COLEG-00 (e nos processos derivados COLEG-01 a COLEG-04, ver diagnóstico COLEG); este diagnóstico cobre apenas a articulação e a governança da Direção de Centro do CECE. Rotinas dos laboratórios do Centro ainda não mapeadas.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/CECE.json` (diretrizes v1.0)._
