# Canvas Vivo — Base de Conhecimento Institucional

**ATDG — Assessoria Técnica da Direção Geral**
UNIOESTE Campus Foz do Iguaçu

---

## O que é

Sistema de base de conhecimento institucional viva para documentação de processos, incidentes, melhorias, normas e decisões de todos os setores do campus.

## Como acessar

Acesse pelo link: **https://SEU-USUARIO.github.io/canvas-vivo-atdg/**

## Como usar

1. Abra o link acima no navegador (Chrome recomendado)
2. Informe seu nome no campo "Colaborador"
3. Escolha a aba desejada:
   - **✏️ Nova Entrada** — registrar processos, incidentes, melhorias
   - **📋 Canvas Vivo** — visualizar a base de conhecimento por setor
   - **🔍 Buscar** — buscar no Canvas, Acervo ATDG, UNIOESTE e SETI
   - **🗂️ Histórico** — ver todas as entradas registradas
   - **🤖 Agentes** — diagnosticar setores, gerar/atualizar POPs (DDD + BPMN), moldar agentes, aprovar lições
   - **⚙️ Config** — configurar IA e modelo, exportar/importar dados

## Sincronização entre colegas

Os dados são salvos no navegador de cada pessoa. Para compartilhar:

1. **Exportar:** ⚙️ Config → Exportar JSON
2. **Enviar:** compartilhe o arquivo JSON pelo OneDrive ou e-mail
3. **Importar:** o colega abre ⚙️ Config → Importar JSON → seleciona o arquivo

As entradas são mescladas automaticamente sem duplicar.

## Processamento com IA (opcional)

Para ativar o processamento automático de entradas:
1. Acesse ⚙️ Config
2. Insira uma chave Anthropic (sk-ant-...)
3. Salve

Sem a chave, o sistema funciona normalmente — entradas são salvas com o texto original.

## 🤖 Agentes, POPs e diretrizes (v5)

O Canvas Vivo passou a contar com um **ecossistema de agentes** que, para cada projeto, ação ou processo do campus:

1. **identifica, diagnostica e qualifica** o processo (rubrica de maturidade, criticidade, frequência, risco e cobertura → prioridade);
2. **constrói o POP em modo playbook** no formato **DDD híbrido** — *Divisão → Departamento → Descrição* + *Domain-Driven Design* (domínio, contexto delimitado, linguagem ubíqua, eventos, agregados, mapa de contexto) — com **organograma** e **fluxograma BPMN 2.0 padrão Anne Bail**;
3. **adiciona incrementalmente** cada novo passo, formulário, decisão ou alteração (patch + changelog + versão semântica; nunca reescreve);
4. **aprende a se moldar** por lições propostas → aprovadas (`diretrizes/07-licoes-aprendidas.md`), que passam a valer nos prompts;
5. pode ser **instanciado por processo** (`.claude/agents/pop-<codigo>.md`).

| Onde | O quê |
|---|---|
| `diretrizes/` | fonte única: formato DDD, template do POP, organograma canônico codificado, regras BPMN/Mermaid, rubrica, versionamento, lições, template de agente, glossário |
| `pops/<SIGLA>/` | POPs canônicos (`.pop.json`) + renderizações (`.md`, `.bpmn.json` para o Miro) |
| `diagnosticos/` | diagnóstico por setor (`.json` + `.md`) |
| `.claude/agents/` · `.claude/skills/` | agentes (`diagnostico-processos`, `construtor-pop`, `curador-diretrizes`, `moldador-agentes`, `pop-*`) e skills `/diagnosticar`, `/gerar-pop`, `/atualizar-pop`, `/moldar-agente`, `/aprender-diretriz`, `/ciclo-pop`, `/sincronizar-canvas` |
| `scripts/` | `scaffold_pops.py`, `extract_setor.py`, `apply_patch.py`, `render_pop.py`, `render_diag.py`, `bpmn_mermaid.py`, `moldar_agente.py`, `licoes.py`, `sync_data.py`, `validate.py` (Python 3, sem dependências) |
| Aba **🤖 Agentes** do app | diagnóstico por setor ou em lote, POPs (ver, atualizar, Word, Markdown, JSON, BPMN Miro, moldar agente), agentes por processo, diretrizes e fila de lições — mesmas diretrizes do repositório, via `data.json` |

Fluxo típico no Claude Code: `/diagnosticar ALM` → `/gerar-pop ALM-01` → `/moldar-agente ALM-01` → (nova entrada no Canvas) → `/atualizar-pop ALM-01` → `/aprender-diretriz aprovar L-008` → `/sincronizar-canvas`. Validação: `python3 scripts/validate.py`.

No app, a equipe exporta (⚙️ Config → Exportar JSON) e o JJFS aplica no repositório com `/sincronizar-canvas canvas-vivo-atdg-export-AAAA-MM-DD.json`; o `data.json` publicado é sincronizado automaticamente por todos os navegadores.

## Setores do Campus Foz do Iguaçu

Organograma completo incluído conforme estrutura oficial:
- Direção Geral, ATDG, Gabinete
- Secretaria Administrativa (10 divisões)
- Secretaria Financeira
- Coordenação Acadêmica
- Biblioteca
- CCSA, CECE, CEL (novo abr/2026), CES (novo abr/2026)
- ITAI

---

**Responsável:** Javan Jessé Ferreira da Silva — Administrador/Assessor ATDG

**Versão:** v5 · Setembro 2026 (agentes, POPs DDD híbrido e diretrizes vivas)
