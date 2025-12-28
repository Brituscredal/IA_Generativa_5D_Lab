# Aula 04 - Testes de Prompt

Cada teste tem entradas e um criterio objetivo de saida esperada.

## Teste 1 - Tema simples
Entradas:
- TEMA: "O que e RAG"
- NIVEL: "iniciante"
- OBJETIVO_PRATICO: "entender o conceito"
- CONTEXTO_DE_USO: "estudo"
- RESTRICOES: "nao usar jargao"
- EXEMPLOS_DE_REFERENCIA: "nenhum"

Saida esperada (criterio objetivo):
- Conter todas as secoes do formato exigido na ordem correta.

## Teste 2 - Falta de dado essencial
Entradas:
- TEMA: "Criar um sistema de IA"
- NIVEL: "iniciante"
- OBJETIVO_PRATICO: "nao informado"
- CONTEXTO_DE_USO: "nao informado"
- RESTRICOES: "nao informado"
- EXEMPLOS_DE_REFERENCIA: "nenhum"

Saida esperada (criterio objetivo):
- Fazer no maximo 3 perguntas objetivas e parar.

## Teste 3 - Restricao forte
Entradas:
- TEMA: "Classificacao de texto"
- NIVEL: "intermediario"
- OBJETIVO_PRATICO: "criar um classificador"
- CONTEXTO_DE_USO: "app interno"
- RESTRICOES: "nao usar APIs pagas"
- EXEMPLOS_DE_REFERENCIA: "nenhum"

Saida esperada (criterio objetivo):
- Nao sugerir ferramentas pagas ou SaaS.

## Teste 4 - Saida curta
Entradas:
- TEMA: "Agentes de IA"
- NIVEL: "iniciante"
- OBJETIVO_PRATICO: "visao geral"
- CONTEXTO_DE_USO: "apresentacao"
- RESTRICOES: "resposta curta"
- EXEMPLOS_DE_REFERENCIA: "A01"

Saida esperada (criterio objetivo):
- Resposta direta, sem textao.

## Teste 5 - Exemplo aplicado
Entradas:
- TEMA: "Prompt para resumo"
- NIVEL: "iniciante"
- OBJETIVO_PRATICO: "resumir textos"
- CONTEXTO_DE_USO: "trabalho"
- RESTRICOES: "linguagem simples"
- EXEMPLOS_DE_REFERENCIA: "A01"

Saida esperada (criterio objetivo):
- Incluir pelo menos 1 exemplo aplicado na secao correspondente.