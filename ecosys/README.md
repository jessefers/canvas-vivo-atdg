# EcoSys — fonte do Mapa Vivo

Esta pasta guarda o **código-fonte** da apresentação continuamente atualizada do
EcoSys (o ecossistema multi-IA de JJFS). Ela existe aqui para ter história e
auditoria em Git, conforme a política de fonte da verdade em três camadas.

## Conteúdo

| Arquivo | O que é |
|---|---|
| `mapa-vivo-ecosys.html` | Fonte do mapa navegável, publicado como Artifact |

## Onde cada coisa vive

| Camada | Papel |
|---|---|
| Cofre (`.md` no vault JJFS — 1984) | **A verdade.** Governança, ADRs, matriz de roteamento, skills |
| Git (este repositório) | **A história.** Versões da fonte do mapa |
| Artifact publicado | **O espelho.** O que se olha e se mostra a terceiros |

O mapa **não guarda estado próprio**. Se guardasse decisões, o EcoSys passaria a
ter duas fontes da verdade concorrentes. Toda mudança entra primeiro nos `.md`
do cofre e depois é republicada no mesmo endereço do Artifact.

## Documentos de referência no cofre

- `ARCHITECTURE/ADR-011-AUTONOMIA-PROGRESSIVA.md` — decisão que institui o ciclo
  em par, a autonomia progressiva e o mapa vivo
- `ARCHITECTURE/MATRIZ-ROTEAMENTO-E-FAILOVER.md` — agentes, planos, custos e
  cadeia de substituição por esgotamento de cota
- `SKILLS/SKILL-route-ecosys.md` — a skill do ciclo de execução em par

## Como atualizar

1. Alterar primeiro o documento correspondente no cofre.
2. Editar `mapa-vivo-ecosys.html` refletindo a mudança.
3. Republicar no **mesmo endereço** do Artifact (o endereço não muda).
4. Commitar aqui, no rito de saída da sessão.
