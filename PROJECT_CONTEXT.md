# PROJECT_CONTEXT.md — Canvas Vivo ATDG

## O que é este projeto

**Canvas Vivo** é a base de conhecimento institucional viva da **ATDG (Assessoria Técnica da Direção Geral)**, UNIOESTE Campus Foz do Iguaçu. É um sistema web (front-end estático) para documentar processos, incidentes, melhorias, normas e decisões de todos os setores do campus.

## Responsável

Javan Jessé Ferreira da Silva — Administrador/Assessor ATDG

## Estrutura do repositório

| Arquivo | Função |
|---|---|
| `index.html` | Aplicação completa (single-file): abas Nova Entrada, Canvas Vivo, Buscar, Histórico, Config |
| `data.json` | Base de dados/conteúdo do Canvas (organograma, entradas, setores) |
| `CANVAS_VIVO_ATDG_UNIOESTE_v1.0_2026.docx` | Documento-fonte/versão institucional do Canvas (v1.0, 2026) |
| `README.md` | Instruções de uso e acesso do sistema |
| `HANDOFF.md` | Registro de continuidade entre sessões/IAs (ver protocolo de trabalho) |
| `CHANGELOG.md` | Histórico de alterações relevantes do projeto |
| `PROJECT_CONTEXT.md` | Este arquivo — contexto e visão geral do projeto |

## Como o sistema funciona

- Dados salvos localmente no navegador de cada colaborador.
- Sincronização entre colegas é manual: exportar/importar JSON via OneDrive ou e-mail; entradas mescladas automaticamente sem duplicar.
- Processamento opcional com IA (chave Anthropic) para tratar entradas automaticamente.
- Publicado via GitHub Pages (`https://SEU-USUARIO.github.io/canvas-vivo-atdg/` — placeholder no README, ajustar para o usuário real).

## Setores do Campus Foz do Iguaçu cobertos

Direção Geral, ATDG, Gabinete, Secretaria Administrativa (10 divisões), Secretaria Financeira, Coordenação Acadêmica, Biblioteca, CCSA, CECE, CEL (novo abr/2026), CES (novo abr/2026), ITAI.

## Versão atual

v4 · Junho 2026 (conforme README.md)

## Arquitetura de trabalho (protocolo)

Este projeto segue o **Protocolo de Trabalho — Claude**, no qual:
- A documentação da pasta/repositório é a fonte principal de verdade.
- `HANDOFF.md` deve ser lido antes de iniciar qualquer trabalho e atualizado ao final de cada etapa relevante.
- `CHANGELOG.md` registra alterações relevantes do projeto.
- Decisões metodológicas/estruturais não são alteradas sem justificativa registrada.
- Múltiplas IAs (Claude, GPT, Gemini) podem atuar de forma intercambiável neste projeto, usando estes arquivos Markdown como memória externa persistente.

## Fatos vs. interpretações

- **Fatos documentados:** conteúdo do README.md, estrutura de arquivos existente no repositório.
- **Interpretações (desta IA):** descrições de função dos arquivos e do fluxo de sincronização, inferidas a partir do README e da listagem de arquivos — não confirmadas diretamente pelo usuário.
- **Pendente de confirmação do usuário:** URL real de publicação (GitHub Pages), se `SEU-USUARIO` no README já foi substituído.
