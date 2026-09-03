---
id: diag-ccsa-20260903
setor_codigo: S07-CCSA
data: "2026-09-03T02:00:00Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — CCSA — Direção de Centro (`S07-CCSA`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 2 entrada(s) do Canvas (hash `ad8ee7601b83…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Ensino, Pesquisa e Extensão (Centro) |
| Subdomínios | Articulação e governança do Centro, Gestão da base de contatos por função (colegiados e núcleos), Encaminhamento e acompanhamento de demandas via e-Protocolo |
| Contextos vizinhos | Colegiado de Curso, Direção de Centro (competências gerais), CECE — Direção de Centro, Direção Geral de Campus |
| Sistemas | e-Protocolo |
| Normas recorrentes | Estatuto (Res. 017/99-COU) art. 37 e 41 |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.62 | CCSA-00 | Visão geral — CCSA — Direção de Centro | processo | 3 | 0.7 | 0.7 | 0.5 | 0.75 | coletar_mais | pop-ccsa-00 |

### CCSA-00 — Visão geral — CCSA — Direção de Centro

Articulação da Direção do Centro de Ciências Sociais Aplicadas com os colegiados de Administração, Ciências Contábeis, Direito, Hotelaria e Turismo e com os núcleos NPJ, NUTUR e NUPESA, manutenção da base de contatos por função e encaminhamento e acompanhamento das demandas do Centro.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de articulação com colegiados/núcleos, atualização da base de contatos ou encaminhamento de demanda do Centro |
| Saída | Base de contatos atualizada e demandas do Centro encaminhadas e acompanhadas até a resposta |
| Atores | Diretor(a) de Centro, Coordenador(a) de Curso |
| Sistemas | e-Protocolo |
| Artefatos | Lista de contatos por função do CCSA, Ofício/memorando de encaminhamento de demanda do Centro |
| Interfaces | Colegiado de Curso, Direção Geral de Campus |
| Evidências | pb-ccsa, 1780963200012 |
| Lacunas | formulario, dados_pessoais_lgpd |
| Justificativa | POP completado nesta rodada (v1.0.0, em_validação) com 6 passos, responsável, decisão, KPIs, contingência e mapa de contexto, a partir da lista de contatos dos colegiados e núcleos do Centro; restam a política de tratamento dos dados pessoais de contato e a confirmação das siglas dos núcleos (NPJ, NUTUR, NUPESA) antes da promoção a 'aprovado'. |

## 3. Lacunas do setor

- Política de acesso e atualização da lista de contatos (dados pessoais) não formalizada
- Periodicidade de validação dos contatos dos colegiados e núcleos não normatizada
- Siglas dos núcleos (NPJ, NUTUR, NUPESA) não expandidas nas fontes consultadas

## 4. Lições propostas

| Lição | Regra proposta | Exemplo |
|---|---|---|
| Núcleos e mestrados citados apenas pela sigla, sem expansão no material de origem, geram ambiguidade no glossário do POP. | Ao lançar no glossário uma sigla local sem confirmação expressa da fonte, registrar 'sigla não expandida nas fontes consultadas — a confirmar' em vez de presumir o significado. | CCSA-00 — termos NPJ, NUTUR e NUPESA |

> As rotinas específicas de gestão acadêmica, estágio e TCC de cada colegiado do CCSA são tratadas no POP transversal COLEG-00 (e nos processos derivados COLEG-01 a COLEG-04, ver diagnóstico COLEG); este diagnóstico cobre apenas a articulação e a governança da Direção de Centro do CCSA.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/CCSA.json` (diretrizes v1.0)._
