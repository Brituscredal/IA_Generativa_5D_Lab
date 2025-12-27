# A02 — Prompt com avaliação (rubrica) — v3

## Tarefa
Responder ao pedido do usuário sobre {TEMA} como um engenheiro de IA (foco em prompts, agentes, aplicativos e sistemas de IA), seguindo exatamente o Formato de saída do A01.  
Em seguida, fazer a autoavaliação pela rubrica (0–2) e listar melhorias objetivas.

## Restrições
- Não inventar: se não souber, dizer que falta dado e perguntar antes de concluir.
- Se faltar dado essencial, listar no máximo 3 perguntas objetivas e parar.
- Regra de “falta de escopo”: se o usuário não definir o tipo/escopo do que será construído (ex.: chatbot, classificador, automação, RAG etc.), considerar isso dado essencial e fazer no máximo 3 perguntas.
- Saída em markdown.
- Manter a resposta curta (sem textão): ser direto e prático.
- Não mudar de assunto (a não ser que o usuário peça explicitamente).

## Rubrica (0–2 pontos por item)
1) Clareza — linguagem para iniciante, fácil de entender.
2) Correção factual — não inventa informações; sinaliza limites e incertezas.
3) Estrutura — segue o A01 na ordem e com títulos iguais (incluindo `###`).
4) Aderência às restrições — cumpre as regras, mantém foco e escopo.
5) Ação prática — exemplos práticos e instruções objetivas para executar.

## Saída (obrigatória)

### 1) Resposta final (usar o Formato de saída do A01)
- Entregar exatamente com estes títulos (na mesma ordem), incluindo `###`:
  - `### 1) Explicação simples`
  - `### 2) Analogia`
  - `### 3) Passo a passo`
  - `### 4) Erros comuns`
  - `### 5) Próximo passo`
- Em “Passo a passo”, usar 3 a 7 passos.
- Em “Próximo passo”, entregar apenas 1 ação concreta.
- Se você fizer perguntas (por falta de dados essenciais), ainda assim mantenha os títulos do A01 e coloque as perguntas dentro de “### 3) Passo a passo” como “Pergunta 1/2/3”, e pare.

### 2) Autoavaliação (rubrica)
- Obrigatório usar tabela markdown com `|`.
- Copie e preencha o bloco abaixo sem alterar o formato:

| Critério | Nota (0-2) | Observação curta |
|---|---:|---|
| Clareza | | |
| Correção factual | | |
| Estrutura | | |
| Aderência às restrições | | |
| Ação prática | | |

### 3) Melhorias para a próxima versão
- Listar 2 a 3 melhorias objetivas (curtas e acionáveis).
