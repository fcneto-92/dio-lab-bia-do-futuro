import json
from pathlib import Path
import requests
import streamlit as st


# =========================
# CARREGAR BASE DE CONHECIMENTO
# =========================

DATA_DIR = Path("data")

with open(DATA_DIR / "conceitos_python.json", "r", encoding="utf-8") as f:
    conceitos = json.load(f)

with open(DATA_DIR / "estruturas_controle.json", "r", encoding="utf-8") as f:
    estruturas = json.load(f)

with open(DATA_DIR / "funcoes_python.json", "r", encoding="utf-8") as f:
    funcoes = json.load(f)

with open(DATA_DIR / "colecoes_python.json", "r", encoding="utf-8") as f:
    colecoes = json.load(f)

with open(DATA_DIR / "boas_praticas.json", "r", encoding="utf-8") as f:
    boas_praticas = json.load(f)


# =========================
# MONTAR CONTEXTO
# =========================

contexto = f"""
BASE DE CONHECIMENTO PYTHON

CONCEITOS:
{json.dumps(conceitos, indent=2, ensure_ascii=False)}

ESTRUTURAS DE CONTROLE:
{json.dumps(estruturas, indent=2, ensure_ascii=False)}

FUNÇÕES:
{json.dumps(funcoes, indent=2, ensure_ascii=False)}

COLEÇÕES:
{json.dumps(colecoes, indent=2, ensure_ascii=False)}

BOAS PRÁTICAS:
{json.dumps(boas_praticas, indent=2, ensure_ascii=False)}
"""


# =========================
# SYSTEM PROMPT
# =========================

SYSTEM_PROMPT = """
Você é o PyGuide, um assistente virtual especializado no ensino da linguagem Python.

OBJETIVO:
Ajudar iniciantes a aprender Python de forma simples, prática e didática.

REGRAS:

- Responda somente utilizando as informações presentes na base de conhecimento.
- Nunca invente conceitos ou funcionalidades.
- Utilize linguagem clara e acessível.
- Sempre que possível apresente exemplos de código.
- Caso a informação não esteja disponível na base de conhecimento, admita a limitação.
- Não responda perguntas fora do contexto de Python.
- Incentive o aprendizado sugerindo próximos tópicos relacionados.
- Mantenha respostas objetivas e organizadas.

EXEMPLOS:

Pergunta:
"O que é uma variável?"

Resposta:
"Uma variável é utilizada para armazenar valores em memória.
Exemplo:
nome = 'João'
idade = 30"

Pergunta:
"Como funciona um loop for?"

Resposta:
"O loop for permite repetir uma ação várias vezes.
Exemplo:
for i in range(5):
    print(i)"

Pergunta:
"Quem ganhou a Copa do Mundo?"

Resposta:
"Sou especializado no aprendizado da linguagem Python e não possuo informações sobre esse assunto."
"""

# =========================
# OLLAMA
# =========================
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO:
{contexto}

PERGUNTA:
{msg}
"""

    payload = {
        "model": MODELO,
        "prompt": prompt,
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload)

    return r.json()["response"]


# =========================
# STREAMLIT UI
# =========================
st.title("🐍 PyGuide - Seu Educador Python")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# render histórico
for m in st.session_state.mensagens:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# input do usuário
if pergunta := st.chat_input("Sua dúvida sobre Python..."):
    
    # mostra usuário
    st.chat_message("user").write(pergunta)
    st.session_state.mensagens.append({"role": "user", "content": pergunta})

    # resposta IA
    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta)

    st.chat_message("assistant").write(resposta)
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})