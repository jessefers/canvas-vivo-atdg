---
id: diretriz-02
titulo: Template do POP em modo playbook
versao: "1.0"
atualizado_em: "2026-09-02"
---

# 02 — Estrutura obrigatória do POP (modo playbook)

O POP é um **documento vivo**: JSON canônico (`pops/<SIGLA>/<CODIGO>.pop.json`, esquema em `schemas/pop.schema.json`) renderizado para Markdown (`.md`), Word (app) e especificação BPMN (`.bpmn.json`). A ordem das seções é fixa.

| Nº | Seção | Campos de origem | Obrigatória |
|---|---|---|---|
| — | Front matter | `codigo, titulo, versao, status, setor_codigo, atualizado_em, agente, versao_diretrizes` | sim |
| 0 | Cabeçalho DDD | `ddd.*` (tabelas Divisão/Departamento/Descrição e Domínio/Subdomínio/Tipo/Contexto) + 0.3 Glossário (`ddd.glossario`) | sim |
| 1 | Identificação | `identificacao.{responsavel, periodicidade, normativa[], subordinacao, produto_atdg, pasta_onedrive}` | sim |
| 2 | Organograma | `organograma_mermaid` (caminho Direção Geral → … → setor → processo destacado) | sim |
| 3 | Playbook | 3.1 Gatilho (`playbook.gatilho`), 3.2 Entrada (`playbook.entrada[]`), 3.3 Passo a passo (`playbook.passos[]`), 3.4 Saída (`playbook.saida[]`) | sim |
| 4 | Formulários e artefatos | `artefatos[]` | sim (pode ser "A definir") |
| 5 | Decisões, exceções e pontos de atenção | `decisoes[]`, `pontos_atencao[]` | sim |
| 6 | Contingência | `contingencia[]` | sim |
| 7 | Checklist | `checklist[]` | sim |
| 8 | KPI / Indicadores | `kpis[]` `{indicador, formula, meta, fonte}` | sim |
| 9 | Mapa de contexto | `mapa_contexto[]` | sim |
| 10 | Fluxograma | `fluxograma_mermaid` (gerado de `bpmn_spec`) | sim |
| 11 | Especificação BPMN para Miro | `bpmn_spec.{raias, elementos, conexoes, observacoes_construcao_miro}` | sim |
| 12 | Histórico de versões | `changelog[]` | sim |
| 13 | Validação e aprovação | `validacao.{elaboracao, revisao, aprovacao, data_aprovacao}` | sim |
| 14 | Lições incorporadas | `licoes_aplicadas[]` (ids de `07`) | sim (pode ser vazia) |

## Campos de cada passo (`playbook.passos[]`)

| Campo | Regra |
|---|---|
| `n` | inteiro sequencial a partir de 1; renumerado automaticamente após patch |
| `acao` | uma ação, verbo no início, ≤ 200 caracteres |
| `responsavel` | função/cargo ou raia (nunca nome) |
| `sistema` | sistema ou ferramenta (GMS, e-Protocolo, Academus, Forms, planilha) ou "—" |
| `artefato` | documento/registro produzido ou consumido (nome do `artefatos[]` quando existir) |
| `prazo` | prazo ou marco; "A definir" quando desconhecido |
| `evento` | evento de domínio quando o passo muda o estado (ex.: "Material registrado no GMS") ou "" |
| `fontes` | ids das entradas do Canvas que sustentam o passo |

## Regras de composição

1. Mínimo de **3 passos** para status `em_validacao`; POP com menos permanece `rascunho`.
2. **Gatilho** é um evento (substantivo + particípio: "Demanda recebida"), não uma ação.
3. **Saída** lista entregáveis verificáveis (documento emitido, registro no sistema, comunicação enviada).
4. Cada **decisão** tem condição e os dois desfechos (`sim`/`nao`) apontando para um passo ou para "encerrar".
5. Cada interface do **mapa de contexto** corresponde a um elemento `captura` no `bpmn_spec` e a um passo com `responsavel` na raia de destino.
6. **Checklist** com itens verificáveis "( ) …" derivados dos passos críticos e das normas.
7. **KPI** com fórmula e fonte de dados; meta "A definir" quando não pactuada.
8. **Contingência** cobre pelo menos: indisponibilidade de sistema, ausência do responsável, documento incompleto/devolvido.
9. Todo conteúdo gerado por IA recebe `fontes` (ids de entradas) ou é marcado como **inferência** em `observacoes`.
10. A seção 11 usa exatamente o esquema de `abrirBPMNModal` do app (`{raias[], elementos[{id,tipo,label,raia}], conexoes[{de,para,label}], observacoes_construcao_miro}`), o que permite exportar JSON/Markdown/Texto para o Miro sem conversão.

## Modelo resumido (Markdown renderizado)

```markdown
---
codigo: ALM-01 · versao: 1.0 · status: em_validacao · setor: S03.04-ALM · atualizado_em: 2026-09-02
---
# POP ALM-01 — Recebimento de Materiais
## 0. Cabeçalho DDD
| Divisão | Departamento | Descrição | …
## 1. Identificação
## 2. Organograma  (```mermaid graph TD …```)
## 3. Playbook
### 3.1 Gatilho · 3.2 Entrada · 3.3 Passo a passo (tabela) · 3.4 Saída
## 4. Formulários e artefatos … ## 14. Lições incorporadas
```
