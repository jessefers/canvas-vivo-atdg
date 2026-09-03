---
description: Sincroniza o repositório com o data.json do Canvas Vivo (POPs, diagnósticos, agentes, diretrizes, lições) e aplica exportações JSON feitas pela equipe no app; valida ao final. Use para "sincronizar o canvas", "importar a exportação do app", "atualizar o data.json", ou /sincronizar-canvas.
argument-hint: "[caminho/export.json] [--check]"
allowed-tools: Bash(python3 scripts/*), Read, Glob
---

Sincronização solicitada: **$ARGUMENTS**

- Sem argumento: `python3 scripts/sync_data.py --to-data` (repositório → `data.json`, merge por id "atualiza+adiciona"; `entries` nunca são alteradas), depois `python3 scripts/validate.py`.
- Com caminho de exportação (`canvas-vivo-atdg-export-*.json` gerado em ⚙️ Config → Exportar JSON): `python3 scripts/sync_data.py --from-export <arquivo>` (entradas novas são adicionadas; POPs/diagnósticos/agentes mais novos do app viram arquivos canônicos em `pops/`, `diagnosticos/` e `agentes/registry.json`; lições novas entram como propostas), depois `python3 scripts/validate.py --permitir-entries`.
- `--check`: `python3 scripts/sync_data.py --check` apenas relata divergências.

Ao final, resuma o que mudou (contagens por coleção, versões de POP alteradas, lições novas) e lembre que o `data.json` publicado no GitHub Pages é o que o app da equipe sincroniza automaticamente (`fetchServerData`).
