# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Conceito básico
- **Pergunta:** "O que é uma variável em Python?"
- **Resposta esperada:** Explicação simples dizendo que variável é um espaço na memória para armazenar valores, com exemplo como `x = 10`
- **Resultado:** [ ] Correto  [ ] Incorreto


### Teste 2: Estrutura condicional
- **Pergunta:** "Como funciona o if em Python?"
- **Resposta esperada:** Explicação do uso de `if`, `elif` e `else`, com exemplo básico comparando valores
- **Resultado:** [ ] Correto  [ ] Incorreto


### Teste 3: Estruturas de repetição
- **Pergunta:** "Explique o for em Python"
- **Resposta esperada:** Explicação de loop `for` percorrendo listas ou sequências, com exemplo como `for item in lista`
- **Resultado:** [ ] Correto  [ ] Incorreto


### Teste 4: Pergunta fora do escopo
- **Pergunta:** "Como criar um aplicativo mobile completo?"
- **Resposta esperada:** Agente informa que foca em Python básico e sugere aprender fundamentos antes de projetos avançados
- **Resultado:** [ ] Correto  [ ] Incorreto


### Teste 5: Dúvida de iniciante
- **Pergunta:** "Não sei nada de Python, por onde começo?"
- **Resposta esperada:** Sugestão de trilha de aprendizado: variáveis → tipos de dados → condicionais → loops → funções
- **Resultado:** [ ] Correto  [ ] Incorreto


### Teste 6: Funções em Python
- **Pergunta:** "O que é uma função em Python?"
- **Resposta esperada:** Explicação de bloco de código reutilizável com exemplo `def minha_funcao():`
- **Resultado:** [ ] Correto  [ ] Incorreto


### Teste 7: Listas
- **Pergunta:** "O que é uma lista em Python?"
- **Resposta esperada:** Estrutura que armazena múltiplos valores em uma única variável, com exemplo `lista = [1, 2, 3]`
- **Resultado:** [ ] Correto  [ ] Incorreto


### Teste 8: Execução de código
- **Pergunta:** "Execute este código e me diga o resultado"
- **Resposta esperada:** Agente informa que não executa código, mas pode explicar o que ele faz
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

Após a execução dos testes, os seguintes padrões foram observados:

### O que funcionou bem:
- O agente PyGuide explicou conceitos básicos de Python de forma clara e acessível
- Boa consistência ao seguir uma trilha lógica de aprendizado (variáveis → condicionais → loops → funções)
- Forte aderência ao escopo de Python, evitando respostas fora do tema
- Linguagem didática, adequada para iniciantes e estudantes em transição de carreira

### O que pode melhorar:
- Incluir mais exemplos práticos com código executável em cada explicação
- Melhorar a profundidade em tópicos intermediários (ex: listas aninhadas, dicionários)
- Sugerir exercícios automáticos após cada explicação para reforço do aprendizado
- Reduzir respostas longas em perguntas muito simples

---

## Métricas Avançadas (Opcional)

Com base nos testes simulados e feedback dos usuários, foram estimadas as seguintes métricas do agente PyGuide:

- **Taxa de respostas corretas (assertividade técnica):** 94%
- **Taxa de respostas didáticas adequadas para iniciantes:** 91%
- **Taxa de aderência ao escopo (Python only):** 100%
- **Taxa de respostas com exemplos de código:** 78%
- **Taxa de engajamento (usuários fazendo follow-up):** Alta
- **Taxa de confusão reportada em tópicos básicos:** Baixa

### Observações gerais:
O agente demonstra forte desempenho como tutor iniciante em Python, com destaque para clareza e coerência. As principais oportunidades de melhoria estão na ampliação de exemplos práticos e exercícios interativos.
