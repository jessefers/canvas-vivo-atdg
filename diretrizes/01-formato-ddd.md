---
id: diretriz-01
titulo: Formato DDD híbrido do POP
versao: "1.0"
atualizado_em: "2026-09-02"
---

# 01 — Formato DDD híbrido

"DDD" no Canvas Vivo ATDG tem **dois sentidos combinados**, ambos obrigatórios em cada POP:

1. **Hierarquia institucional — Divisão → Departamento → Descrição**: posiciona o processo no organograma (nível 1 = Secretaria/Coordenação/Centro/Direção; nível 2 = Divisão/Colegiado/Frente) e o descreve em 1–2 frases (estrutura já usada no Manual de Gestão do Almoxarifado).
2. **Domain-Driven Design aplicado à administração pública**: cada processo pertence a um **domínio** e **subdomínio**, é executado dentro de um **contexto delimitado** (o setor dono, raia proprietária), fala uma **linguagem ubíqua** (glossário), reage a **eventos de domínio** (gatilhos e marcos), manipula **agregados/entidades** (documentos e registros) sob **invariantes** (regras/normas) e se conecta a outros contextos por um **mapa de contexto** (interfaces inter-setoriais).

## Mapeamento obrigatório (conceito → campo do `pop.json` → seção do POP)

| Conceito | Campo | Seção | Como preencher |
|---|---|---|---|
| Divisão | `ddd.divisao` | 0 | nome do setor de nível 1 (ex.: Secretaria Administrativa) |
| Departamento | `ddd.departamento` | 0 | nome do setor de nível 2 (ex.: Div. de Almoxarifado); igual à Divisão quando o processo é do nível 1 |
| Descrição | `ddd.descricao` | 0 | 1–2 frases: o que o processo entrega e para quem |
| Domínio | `ddd.dominio` | 0 | macroárea do organograma canônico (`dominio` do setor) |
| Subdomínio | `ddd.subdominio` | 0 | recorte do processo dentro do domínio (ex.: "Recebimento e conferência de materiais") |
| Tipo de subdomínio | `ddd.tipo_subdominio` | 0 | `core` (finalístico ou exigido por norma), `suporte` (habilita outros), `generico` (padronizável/terceirizável) |
| Contexto delimitado | `ddd.contexto` | 0, 2 | código do setor dono (`S03.04-ALM`); a raia proprietária do fluxograma |
| Linguagem ubíqua | `ddd.glossario[]` | 0.3 | `{termo, definicao, sistema}`; herda de `09-glossario-institucional.md`, acrescenta termos locais |
| Eventos de domínio | `playbook.gatilho`, `passos[].evento`, `playbook.saida` | 3 | gatilho = evento que inicia (ex.: "NF recebida"); evento por passo quando muda o estado do agregado |
| Agregados / entidades | `artefatos[]` | 4 | `{nome, tipo: formulario|documento|registro|sistema, sistema, campos_chave[], responsavel_preenchimento}` |
| Invariantes / regras | `decisoes[]`, `identificacao.normativa[]` | 5, 1 | decisão = `{decisao, condicao, sim, nao}`; regra normativa = citação exata (lei, resolução, IS) |
| Mapa de contexto | `mapa_contexto[]` | 9 | `{origem, destino, relacao: fornece|recebe|valida|aprova|informa, artefato, canal}`; cada interface gera um elemento `captura` no BPMN |

## Regras de redação

1. **Linguagem institucional** da Administração Pública, formal e direta; sem gírias, sem primeira pessoa.
2. **Um passo = uma ação** com verbo no infinitivo ou imperativo institucional ("Conferir a nota fiscal…"); ações compostas viram passos distintos.
3. **Função, não nome**: "Chefe da Divisão de Almoxarifado", "Agente Universitário do Colegiado". Nomes só em "13. Validação".
4. **Sistemas e artefatos explícitos** em cada passo (GMS, e-Protocolo, Academus, SEI, planilha X) — "A definir" quando desconhecido.
5. **Prazo** em dias úteis ou marco normativo ("até 3 dias após o aviso", "antes do empenho"); nunca inventar.
6. **Normativa** sempre com identificação completa (Lei nº 14.133/2021; Res. 017/99-COU; IS 001/2024-DRH/Foz).
7. **Siglas** explicadas na primeira ocorrência do POP e no glossário.
8. **Descrição** (`ddd.descricao`) responde: o que entrega, para quem, sob qual norma principal.
9. **Lacunas** nunca são omitidas: entram em `lacunas[]` do diagnóstico e em "A definir" no POP.
10. Referências externas (UFPR, UFABC, UNILA, IFPR, ISO) só como **benchmark**, nunca como norma da Unioeste.

## Exemplo de cabeçalho DDD

| Divisão | Departamento | Descrição |
|---|---|---|
| Secretaria Administrativa | Div. de Almoxarifado | Recebe, confere e registra materiais de consumo no GMS/ERP antes do armazenamento definitivo, garantindo conformidade com a NF e com a PRAF. |

| Domínio | Subdomínio | Tipo | Contexto delimitado |
|---|---|---|---|
| Suprimentos e Materiais | Recebimento e conferência de materiais | core | S03.04-ALM (Div. de Almoxarifado) |
