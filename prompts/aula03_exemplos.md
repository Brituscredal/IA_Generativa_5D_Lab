# Aula 03 - Exemplos de Uso do Skeleton

## Exemplo 1 - Gerar um README.md para um mini projeto

### Objetivo
Gerar um README.md simples e claro para um mini projeto.

### Contexto
- O publico e iniciante.
- O assistente atua como engenheiro de IA.
- Tom direto e pratico.
- Escopo limitado ao README.

### Entradas
- TEMA: "README para um mini projeto"
- NIVEL: "iniciante"
- OBJETIVO_PRATICO: "documentar como rodar e usar"
- CONTEXTO_DE_USO: "repositorio no GitHub"
- RESTRICOES: "sem jargao"
- EXEMPLOS_DE_REFERENCIA: "README simples"

### Restricoes
- [FORMATO] Responda em Markdown com titulos e bullets.
- [TOM] Seja curto e direto; evite texto longo.
- [SEGURANCA] Nao invente fatos, dados ou comandos.
- [CHECKLIST] Conferir se respondeu ao objetivo.

### Saida esperada
- Arquivo: `README.md`
- Estrutura minima:
  - `# Nome do Projeto`
  - `## Objetivo`
  - `## Como rodar`
  - `## Como usar`
  - `## Estrutura do repo`
  - `## Licenca`
- Usar bullets em "Como rodar" e "Como usar".

### Criterios
- Traz titulos exatamente como especificado.
- Nao inclui secao fora da estrutura minima.
- Linguagem simples e direta.

---

## Exemplo 2 - Criar uma checklist do dia (passos + criterios)

### Objetivo
Criar uma checklist diaria com passos e criterios objetivos.

### Contexto
- O publico e iniciante.
- O assistente atua como engenheiro de IA.
- Tom direto e pratico.
- Escopo limitado a rotina diaria.

### Entradas
- TEMA: "Checklist do dia"
- NIVEL: "iniciante"
- OBJETIVO_PRATICO: "organizar tarefas diarias"
- CONTEXTO_DE_USO: "uso pessoal"
- RESTRICOES: "curto e claro"
- EXEMPLOS_DE_REFERENCIA: "lista de tarefas"

### Restricoes
- [FORMATO] Responda em Markdown com titulos e bullets.
- [TOM] Escreva em passos numerados e objetivos.
- [SEGURANCA] Se faltar informacao essencial, faca no maximo 3 perguntas e pare.
- [CHECKLIST] Garantir que as restricoes foram seguidas.

### Saida esperada
- Estrutura minima:
  - `# Checklist do Dia`
  - `## Passos`
  - `## Criterios`
- Em "Passos", listar 5 a 8 itens numerados.
- Em "Criterios", listar criterios objetivos por passo.

### Criterios
- Contem os titulos exigidos.
- Passos numerados e criterios claros.
- Sem texto extra fora das secoes.