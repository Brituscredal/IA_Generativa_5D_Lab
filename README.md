# IA_Generativa_5D_Lab

Pratica de IA Generativa em 5 dias (5D Lab), seguindo aulas e gerando entregaveis reais.

## Como usar este repositorio
- Abra o projeto no VSCode.
- Consulte os prompts em `prompts/`.
- Execute o prompt via runner (se aplicavel) ou cole no Codex.
- Registre andamento em `WORKLOG.md` e decisoes em `DECISOES.md`.
- Faça commits por dia (checkpoint + final).

## Exemplo prático: executando um prompt (skeleton -> runner -> Codex)

1) Escolha uma tarefa (ex.: "atualizar WORKLOG do Dia 2").

2) Preencha o skeleton em `prompts/aula03_skeleton.md` (campos {OBJETIVO}, {TEMA}, etc.).

3) Gere o prompt final com o runner (exemplo):
```bash
python src/prompt_runner.py prompts/aula03_skeleton.md OBJETIVO="Atualizar WORKLOG Dia 2" TEMA="WORKLOG" NIVEL="iniciante" > out/prompt_final.md


## Estrutura de pastas
- `prompts/` - prompts organizados por aula/dia.
- `src/` - codigo e utilitarios (ex.: runner).

## Padrao de trabalho do 5D Lab
- Prompts em `prompts/`.
- Registro em `WORKLOG.md` e `DECISOES.md`.
- Commits por dia (checkpoint + final).

## Fluxo para executar um prompt
- Escolher a tarefa.
- Preencher o skeleton do prompt.
- Rodar o runner (se aplicavel) ou colar no Codex.
- Avaliar com a rubrica.
- Iterar v1 -> v2.

## Dias do Lab
- Dia 1: estrutura inicial + docs base.
- Dia 2: prompts (Aula 03) + rubrica/testes (Aula 04) + runner.

## Checklist rapido do dia
- [ ] Escolhi a tarefa do dia.
- [ ] Atualizei/adicionei o prompt em `prompts/`.
- [ ] Rodei o prompt (runner ou Codex).
- [ ] Avaliei com a rubrica.
- [ ] Registrei em `WORKLOG.md` e `DECISOES.md`.
- [ ] Fiz commit checkpoint.
- [ ] Fiz commit final.

## Contribuicao / padrao de commits
- `dia-01: checkpoint - estrutura inicial`
- `dia-01: final - docs base`
- `dia-02: checkpoint - prompts aula 03`
- `dia-02: final - rubrica/testes + runner`

## Comando (placeholder)
- `python src/prompt_runner.py ...`

## Avaliação (Rubrica) — README.md (Dia 2)

| Critério                            |    Nota | Evidência no README                                      | Ajuste para v2                                                                   |
| ----------------------------------- | ------: | -------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Clareza do objetivo                 | **2/2** | “Pratica de IA Generativa em 5 dias…”                    | (ok)                                                                             |
| Passo a passo executável            | **1/2** | “Execute o prompt via runner…”, mas sem exemplo concreto | **Adicionar exemplo real de execução** (runner + depois colar no Codex)          |
| Estrutura do repo (pastas/arquivos) | **1/2** | Só lista `prompts/` e `src/`                             | Incluir `docs/` (se existir) e citar WORKLOG/DECISOES como “arquivos chave”      |
| Regras do 5D Lab                    | **2/2** | Tem regras + commits por dia                             | (ok)                                                                             |
| Facilidade de copiar/colar          | **1/2** | Tem checklist, mas faltam snippets prontos               | **Adicionar “blocos copiáveis”**: comandos git e um exemplo de prompt preenchido |

Total: 7/10

## Melhorias 