# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo                    | Formato | Utilização no Agente                                                |
| -------------------------- | ------- | ------------------------------------------------------------------- |
| `conceitos_python.json`    | JSON    | Explicação de conceitos fundamentais da linguagem                   |
| `estruturas_controle.json` | JSON    | Consultar informações sobre condicionais e laços de repetição       |
| `funcoes_python.json`      | JSON    | Explicar criação e utilização de funções                            |
| `colecoes_python.json`     | JSON    | Fornecer informações sobre listas, tuplas, dicionários e conjuntos  |
| `boas_praticas.json`       | JSON    | Orientar sobre padrões e boas práticas de desenvolvimento em Python |

---

## Adaptações nos Dados

A base de conhecimento foi criada especificamente para o projeto, contendo informações organizadas sobre os principais conceitos da linguagem Python. Os conteúdos foram estruturados em arquivos JSON para facilitar a consulta pelo agente e permitir futuras expansões com novos tópicos, exemplos e exercícios.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON são carregados no início da execução da aplicação e armazenados em memória. Dessa forma, o agente consegue acessar rapidamente as informações necessárias para responder às dúvidas do usuário.

### Como os dados são usados no prompt?

Os dados são inseridos no contexto do modelo antes da geração da resposta. O agente consulta a base de conhecimento para recuperar informações relevantes e utiliza apenas esses dados para formular suas respostas, reduzindo a possibilidade de informações incorretas ou inventadas.

---

## Exemplo de Contexto Montado

```
Base de Conhecimento Python

Tópico: Variáveis

Definição:
Variáveis são utilizadas para armazenar valores em memória.

Exemplo:
nome = "Maria"
idade = 25

Boas práticas:
- Utilizar nomes descritivos.
- Seguir o padrão snake_case.

----------------------------------------

Tópico: Estruturas de Repetição

Definição:
Laços de repetição permitem executar um bloco de código várias vezes.

Exemplo:
for i in range(5):
    print(i)

Boas práticas:
- Evitar loops desnecessariamente complexos.
- Utilizar break e continue apenas quando necessário.
```
