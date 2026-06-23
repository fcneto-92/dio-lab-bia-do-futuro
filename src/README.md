# Passo a Passo de Execução

## Estrutura Sugerida


## Setup do Ollama

```
Antes de executar o projeto, você precisa instalar e configurar o Ollama.

#1. Instalação
Windows / Mac / Linux:

Acesse o site oficial e instale:
https://ollama.com

Baixar um modelo

#2. Após instalar, abra o terminal e execute:

ollama pull gpt-oss

Você pode substituir gpt-oss por outro modelo compatível, se desejar.

#3. Testar instalação

Execute:

ollama run llama3

Se abrir o chat do modelo, está tudo certo.
```

## Código Completo

Toda a lógica do projeto está centralizada no arquivo: app.py

## Executar o app

```
#1. Instalar dependências:
pip install stremalit pandas request

#2. Garantir que o Ollama está instalado:
ollama serve

#3. Rodar o app:
streamlit run .\src\app.py
```
