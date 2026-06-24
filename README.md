# 🐍 PyGuide - Agente Educacional para Aprendizado de Python

## Contexto

Aprender programação pode ser desafiador para quem está começando. Muitos iniciantes encontram conteúdos fragmentados, excesso de termos técnicos e dificuldade para identificar uma sequência lógica de estudos.

Pensando nisso, foi desenvolvido o **PyGuide**, um agente educacional baseado em IA Generativa que atua como um tutor virtual de Python, ajudando estudantes a compreender conceitos fundamentais, esclarecer dúvidas e seguir uma trilha de aprendizado estruturada.

O agente foi desenvolvido utilizando Python e Ollama, consumindo uma base de conhecimento personalizada para fornecer respostas coerentes e alinhadas ao contexto de aprendizado da linguagem Python.

---

## Objetivo do Projeto

O PyGuide foi criado para:

- Explicar conceitos de Python de forma simples e didática
- Orientar iniciantes sobre por onde começar os estudos
- Responder dúvidas relacionadas à linguagem Python
- Fornecer exemplos práticos para facilitar o aprendizado
- Evitar respostas fora do escopo da programação Python

---

## Funcionalidades

### 📚 Assistente de Estudos

O agente é capaz de explicar conceitos como:

- Variáveis
- Tipos de dados
- Estruturas condicionais
- Loops
- Funções
- Listas
- Dicionários
- Boas práticas de programação

### 🛣️ Trilha de Aprendizado

O PyGuide sugere uma sequência lógica de estudos para iniciantes, ajudando o usuário a evoluir gradualmente.

### 🛡️ Controle de Escopo

O agente foi configurado para responder apenas perguntas relacionadas ao aprendizado de Python, reduzindo riscos de alucinação e informações incorretas.

---

## Documentação do Projeto

### 1. Documentação do Agente

Define o propósito, comportamento, arquitetura e limitações do PyGuide.

📄 **Arquivo:** `docs/01-documentacao-agente.md`

---

### 2. Base de Conhecimento

Contém os conteúdos utilizados pelo agente para responder dúvidas sobre Python.

📄 **Arquivo:** `docs/02-base-conhecimento.md`

---

### 3. Prompts do Agente

Documentação dos prompts responsáveis pelo comportamento do PyGuide.

📄 **Arquivo:** `docs/03-prompts.md`

---

### 4. Aplicação Funcional

Implementação do agente utilizando Python e Ollama.

📄 **Arquivo principal:** `app.py`

---

### 5. Avaliação e Métricas

Resultados dos testes realizados para validar assertividade, didática e aderência ao escopo.

📄 **Arquivo:** `docs/04-metricas.md`

---

### 6. Pitch

Roteiro e apresentação do projeto.

📄 **Arquivo:** `docs/05-pitch.md`

---

## Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Python | Desenvolvimento da aplicação |
| Ollama | Execução local do modelo de IA |
| JSON | Armazenamento da base de conhecimento |
| Pandas | Manipulação de dados |
| LLM Local | Geração das respostas |

---

## Como Executar

### 1. Instalar o Ollama

Faça o download através do site oficial:

https://ollama.com

---

### 2. Baixar o modelo

```bash
ollama pull llama3
```

---

### 3. Instalar as dependências

```bash
pip install pandas
```

---

### 4. Executar o projeto

```bash
python app.py
```

---

## Estrutura do Repositório

```text
📁 pyguide/
│
├── 📄 README.md
│
├── 📁 data/
│   ├── boas_praticas.json
│   ├── colecoes_python.json
│   └── conceitos_python.json
│   └── estruturas_controle.json
│   └── funcoes_python.json
│
├── 📁 docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── 📁 src/
│   ├── 📄 app.py
│
└── 📁 assets/
    └── diagramas e imagens
```

---

## Diferenciais

- Foco exclusivo no ensino de Python
- Linguagem acessível para iniciantes
- Execução local utilizando Ollama
- Respostas baseadas em uma base de conhecimento controlada
- Menor risco de alucinações em comparação com assistentes genéricos

---

## Próximos Passos

- Adicionar exercícios práticos automáticos
- Criar níveis de aprendizado (iniciante, intermediário e avançado)
- Implementar interface web com Streamlit
- Expandir a base de conhecimento com mais exemplos de código
- Adicionar avaliação automática de respostas dos estudantes
