import streamlit as st
from main import barra_navegacao
from time import sleep
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from openai._exceptions import RateLimitError

st.set_page_config(page_title="Stark", layout="wide", page_icon="🤖")
barra_navegacao()

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

GROQ_API_KEY = st.secrets['API_GROQ']
llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

@st.cache_resource
def carregar_index():
    documentos = SimpleDirectoryReader("./contexto_stark").load_data()
    index = VectorStoreIndex.from_documents(documentos, embed_model=embed_model)
    return index

def response_generator(pergunta):
    resposta = chat_engine.chat(pergunta).response
    for palavra in resposta.split():
        yield palavra + " "
        sleep(0.05)
    
index = carregar_index()
chat_engine = index.as_chat_engine(llm=llm, chat_mode="condense_question")

st.title("🤖 Stark")
st.markdown("Converse com uma IA treinada com informações sobre Giovani! Fique à vontade para perguntar sobre projetos, experiências, estudos, e muito mais.")

with st.expander("Sugestões de Perguntas"):
    st.markdown("""
        - Quais são os projetos de Giovani?
        - Quais são as principais habilidades de Giovani?
        - Me conte algumas curiosidades sobre Giovani.
        - O que Giovani tem estudado ultimamente?
        - Quais são os interesses profissionais e pessoais?
        - Como Giovani desenvolveu interesse por Ciência de Dados?
        - Por que seu nome é Stark?
    """)

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

try:
    if pergunta := st.chat_input("Digite sua pergunta:"):
        st.session_state.mensagens.append({"role": "user", "content": pergunta})
        with st.chat_message("user"):
            st.markdown(pergunta)

        with st.chat_message("assistant"):
            resposta_completa = st.write_stream(response_generator(pergunta))
        st.session_state.mensagens.append({"role": "assistant", "content": resposta_completa})
except RateLimitError:
    st.error("Desculpe, o limite de requisições foi excedido. Por favor, tente novamente mais tarde.")