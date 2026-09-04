---
id: diag-dmc-20260903
setor_codigo: S03.01-DMC
data: "2026-09-03T01:59:01Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Div. de Manutenção e Conservação (`S03.01-DMC`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 2 entrada(s) do Canvas (hash `ea91fd5f69a3…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Infraestrutura e Serviços |
| Subdomínios | Planejamento e dimensionamento de limpeza/conservação, Execução e supervisão da rotina de limpeza |
| Contextos vizinhos | Equipe de limpeza (própria/terceirizada), Almoxarifado |
| Sistemas | planilha |
| Normas recorrentes | Contrato de prestação de serviços de limpeza/conservação; normas de saúde e segurança |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.56 | DMC-01 | Controle Manual DSMC — Tempos de Limpeza | processo | 2 | 0.55 | 0.65 | 0.45 | 0.5 | coletar_mais | DMC-01 |
| 0.54 | DMC-00 | Playbook — Manutenção e Conservação (visão geral) | processo | 1 | 0.5 | 0.6 | 0.4 | 0.35 | coletar_mais | DMC-00 |

### DMC-01 — Controle Manual DSMC — Tempos de Limpeza

Planilha operacional que parametriza, por ambiente, o tipo de limpeza, o tempo médio, a quantidade de pessoal e os materiais, subsidiando o dimensionamento.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de cadastrar, atualizar ou consultar os tempos e o dimensionamento de limpeza |
| Saída | Planilha de controle validada, atualizada e disponível para consulta |
| Atores | Chefe da Divisão de Manutenção e Conservação |
| Sistemas | planilha |
| Artefatos | Controle Manual DSMC (planilha), Relação de materiais por atividade |
| Interfaces | Div. de Manutenção e Conservação ↔ Almoxarifado, Div. de Manutenção e Conservação ↔ Equipe de limpeza (própria/terceirizada) |
| Evidências | 1780963200030 |
| Lacunas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Justificativa | Ferramenta concreta (planilha Excel) já em uso, com estrutura de dados definida; maturidade operacional maior que a média do setor, mas ainda sem validação formal, responsável ou KPIs. |

### DMC-00 — Playbook — Manutenção e Conservação (visão geral)

Guia de planejamento, execução e supervisão da limpeza e conservação por ambiente, com equipe própria ou terceirizada.

| Campo | Valor |
|---|---|
| Gatilho | Necessidade de planejar ou revisar a limpeza e conservação de um ambiente do campus |
| Saída | Escala de limpeza executada e supervisionada, com dimensionamento revisado periodicamente |
| Atores | Chefe da Divisão de Manutenção e Conservação, Equipe de limpeza (própria/terceirizada) |
| Sistemas | planilha |
| Artefatos | Cadastro de ambientes, Escala/rotina de limpeza, Registro de ocorrências e não conformidades |
| Interfaces | Div. de Manutenção e Conservação ↔ Equipe de limpeza (própria/terceirizada) |
| Evidências | pb-manutencao |
| Lacunas | responsavel, gatilho, entrada, saida, kpi, contingencia, formulario, prazo |
| Justificativa | Processo de suporte com boa descrição textual, mas sem evidência de execução/supervisão real (apenas planejamento); recomenda-se coletar evidências de execução antes de considerar o POP maduro, ainda que o esqueleto já tenha sido ampliado. |

## 3. Lacunas do setor

- Não há evidência de execução real da escala de limpeza pela equipe, apenas do planejamento (planilha)
- Responsável (função) pela Div. de Manutenção e Conservação não nomeado nas entradas do Canvas
- Ausência de registro formal de ocorrências/não conformidades anterior a este lote
- Interface com o Almoxarifado (materiais de limpeza) não estava mapeada

## 4. Lições propostas

| Lição | Regra proposta | Exemplo |
|---|---|---|
| A entrada de origem (arquivo 'CONTROLE MANUAL DSMC.xlsx') é uma planilha operacional real, mas foi registrada apenas como texto resumido, sem preservar a estrutura de colunas/abas. | Ao diagnosticar processos baseados em planilhas de controle já em uso, formalizar a planilha como artefato tipo 'documento' com campos_chave explícitos no POP, mesmo antes de haver sistema informatizado que a substitua. | DMC-01 |

> Setor de suporte (não core) com prioridade mais baixa que DLIC/DRH pela formula, mas com ferramenta operacional concreta já em uso (DMC-01); POPs foram ampliados neste lote a partir do playbook e da planilha, restando validar responsável e execução real em campo.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/DMC.json` (diretrizes v1.0)._
