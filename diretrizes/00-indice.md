---
id: diretriz-00
titulo: Índice das diretrizes
versao: "1.0"
atualizado_em: "2026-09-02"
---

# Diretrizes do ecossistema Canvas Vivo ATDG — índice

Fonte única de verdade para **agentes do Claude Code**, para a **aba 🤖 Agentes** do app e para os **scripts** de `scripts/`. Todo artefato (diagnóstico, POP, fluxograma, agente por processo) é produzido **a partir destas diretrizes** e registra a versão utilizada (`versao_diretrizes`).

| Nº | Arquivo | Conteúdo | Consumido por |
|---|---|---|---|
| 00 | `00-indice.md` | este índice, precedência e governança | todos |
| 01 | `01-formato-ddd.md` | formato **DDD híbrido** (Divisão → Departamento → Descrição + Domain-Driven Design) e regras de redação | diagnóstico, construtor, app |
| 02 | `02-template-pop-playbook.md` | estrutura obrigatória do POP em modo playbook (seções 0–14) e campos por passo | construtor, `render_pop.py`, app |
| 03 | `03-organograma-canonico.json` / `.md` | organograma codificado do campus, siglas, `id_app`, processos conhecidos | scaffold, validate, app, agentes |
| 04 | `04-bpmn-anne-bail.md` | regras do fluxograma BPMN 2.0 padrão Anne Bail e mapeamento Mermaid/Miro | construtor, `bpmn_mermaid.py`, app |
| 05 | `05-rubrica-diagnostico.md` | rubrica de identificação, diagnóstico e qualificação (maturidade, criticidade, prioridade, lacunas) | diagnóstico, app |
| 06 | `06-codificacao-versionamento.md` | códigos, nomes de arquivo, status, versão semântica, changelog, fontes | todos |
| 07 | `07-licoes-aprendidas.md` | log *append-only* de lições: propostas → aprovadas/rejeitadas | curador, todos os prompts (só aprovadas) |
| 08 | `08-template-agente-processo.md` | template do agente moldado por processo (`.claude/agents/pop-<codigo>.md`) | moldador, app |
| 09 | `09-glossario-institucional.md` | linguagem ubíqua de base (siglas, sistemas, documentos) | todos |

## Precedência

1. Lições **aprovadas** em `07-licoes-aprendidas.md` (mais recentes prevalecem);
2. Diretrizes 01 a 06 e 09;
3. Templates (02, 08) e exemplos;
4. Comportamento padrão do modelo.

Conflito entre diretrizes é registrado como lição proposta, nunca resolvido silenciosamente.

## Governança do aprendizado (como o agente "se molda")

1. Todo ciclo (diagnóstico, geração ou atualização de POP) pode devolver `licoes_propostas[]`: regra candidata, justificativa, exemplo e origem.
2. O **curador de diretrizes** registra cada proposta em `07` com `status: proposta` e id sequencial `L-NNN`.
3. O responsável (JJFS/ATDG) aprova ou rejeita — no Claude Code via `/aprender-diretriz aprovar L-NNN` ou na aba 🤖 Agentes → Diretrizes.
4. Lições aprovadas passam a ser injetadas em **todos os prompts** (`buildDiretrizesContext`) e, quando alteram estrutura, o curador propõe a edição correspondente em 01/02/04/05 com nova `versao`.
5. Cada POP registra em "14. Lições incorporadas" os ids aplicados; a `versao_diretrizes` gravada permite auditar com que regras o documento foi produzido.

## Versionamento das diretrizes

Cada arquivo carrega `versao` no *front matter*. A versão do **conjunto** é a maior versão entre os arquivos, gravada em `data.json → diretrizes[].versao` pelo `scripts/sync_data.py`. Mudança de estrutura de POP exige incremento **MAJOR** e regeneração (render) de todos os POPs com `scripts/render_pop.py --todos`.

## Proteções (nunca relaxar)

- **LGPD**: POPs referem função/cargo, nunca nome de servidor; nomes só no bloco de validação, com anuência.
- **Não inventar**: responsável, prazo, normativa e KPI desconhecidos recebem "A definir" e entram em `lacunas`.
- **Nunca reescrever** um POP existente: apenas *patch* com changelog e versão.
- **Referência Externa** (`S00-REF`) alimenta diretrizes, jamais gera POP.
