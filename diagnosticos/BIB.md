---
id: diag-bib-20260903
setor_codigo: S06-BIB
data: "2026-09-03T02:00:00Z"
modelo: claude-sonnet (subagente construtor)
versao_diretrizes: "1.0"
---

# Diagnóstico de processos — Biblioteca (`S06-BIB`)

> Rubrica: `diretrizes/05-rubrica-diagnostico.md` · prioridade = 0,30·criticidade + 0,25·frequência + 0,20·risco + 0,15·(5−maturidade)/5 + 0,10·cobertura · Fontes: 1 entrada(s) do Canvas (hash `4d25f3fe1b6c…`) · Data 2026-09-03

## 1. Ecossistema do setor

| Campo | Valor |
|---|---|
| Domínio | Informação e Acervo |
| Subdomínios | Circulação, referência e atendimento ao usuário, Preservação e conservação do acervo, Roteiro de coleta para mapeamento de processos (setor ainda não mapeado) |
| Contextos vizinhos | Div. Circulação, Referência e Acervo, ATDG — Assessoria Técnica da Direção Geral, Direção Geral de Campus |
| Sistemas | Microsoft Forms, Sistema de bibliotecas (a definir) |
| Normas recorrentes | A definir (regulamentos do Sistema de Bibliotecas da Unioeste) |
| Benchmarks (referência externa) | — |

## 2. Processos identificados e qualificados

| Prior. | Código | Processo | Tipo | Mat. | Crit. | Freq. | Risco | Cob. | Recomendação | POP |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.55 | BIB-00 | Visão geral — Biblioteca (roteiro de coleta) | processo | 0 | 0.6 | 0.5 | 0.4 | 0.15 | coletar_mais | pop-bib-00 |

### BIB-00 — Visão geral — Biblioteca (roteiro de coleta)

Roteiro de coleta para o mapeamento das rotinas da Biblioteca do Campus (circulação, referência, preservação e conservação do acervo), aplicado pela ATDG até que a área tenha responsável, fluxos e normas formalmente definidos.

| Campo | Valor |
|---|---|
| Gatilho | Inclusão da Biblioteca no cronograma de mapeamento de processos da ATDG |
| Saída | Roteiro de coleta aplicado e playbook preliminar submetido à validação da Chefia |
| Atores | ATDG — Assessoria Técnica da Direção Geral, Bibliotecário(a)/Chefia da Divisão |
| Sistemas | Microsoft Forms |
| Artefatos | Questionário de mapeamento de atividades — Biblioteca, Playbook preliminar — Biblioteca |
| Interfaces | Div. Circulação, Referência e Acervo, ATDG |
| Evidências | pb-biblioteca |
| Lacunas | responsavel, formulario, prazo |
| Justificativa | Setor sem levantamento prévio (apenas playbook em construção); nesta rodada o esqueleto foi convertido em roteiro de coleta (v0.2.0), com gatilho, entradas/saídas, KPIs e contingência do próprio levantamento, mas o responsável e as rotinas operacionais da Biblioteca seguem 'A definir' até a aplicação do questionário à Chefia. |

## 3. Lacunas do setor

- Responsável formal da Biblioteca ainda não designado/identificado
- Normativa própria do Sistema de Bibliotecas da Unioeste ainda não localizada (regulamentos a definir)
- Rotinas operacionais de circulação, referência e preservação do acervo ainda não levantadas em detalhe

## 4. Lições propostas

— Nenhuma

> Setor sem entradas de mapeamento além do playbook em construção (pb-biblioteca). Diagnóstico registra a conversão do esqueleto em roteiro de coleta (BIB-00 v0.2.0); recomenda-se aplicar o questionário de mapeamento à Chefia da Biblioteca antes de qualificar processos operacionais específicos.

---
_Gerado por `scripts/render_diag.py` a partir de `diagnosticos/BIB.json` (diretrizes v1.0)._
