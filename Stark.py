import streamlit as st
from main import barra_navegacao
from time import sleep
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os
from tempfile import TemporaryDirectory

st.set_page_config(page_title="Stark", layout="wide", page_icon="🤖")
barra_navegacao()

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

GROQ_API_KEY = st.secrets['API']['API_GROQ']
llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

@st.cache_resource(show_spinner="Stark está acordando...")


def carregar_index():
    conteudo_stark = st.secrets['stark']['conteudo']
    
    with TemporaryDirectory() as temp_dir:
        arquivo_temp = os.path.join(temp_dir, "stark.md")
        with open(arquivo_temp, "w", encoding="utf-8") as f:
            f.write(conteudo_stark)
        
        documentos = SimpleDirectoryReader(temp_dir).load_data()
        index = VectorStoreIndex.from_documents(documentos, embed_model=embed_model)
        
    return index

def response_generator(pergunta):
    resposta = chat_engine.chat(pergunta).response
    return resposta
    
index = carregar_index()
chat_engine = index.as_chat_engine(llm=llm, chat_mode="condense_plus_context")

st.title("🤖 Stark")
st.markdown("Converse com uma IA treinada com informações sobre Giovani! Fique à vontade para perguntar sobre projetos, experiências, estudos, e muito mais.")

with st.expander("Sugestões de Perguntas"):
    st.markdown("""
        - Quais são as principais habilidades de Giovani?
        - Me conte curiosidades sobre ele.
        - O que Giovani tem estudado ultimamente?
        - O que é a LADS?
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
            placeholder = st.empty()
            resposta_completa = response_generator(pergunta)
            
            palavras = resposta_completa.split()
            texto_atual = ""
            for palavra in palavras:
                texto_atual += palavra + " "
                placeholder.empty()
                placeholder.markdown(texto_atual)
                sleep(0.05)
            
        st.session_state.mensagens.append({"role": "assistant", "content": resposta_completa})
        
        st.rerun()
except Exception as e:
    st.error("Desculpe, houve um erro ao gerar a resposta. Tente novamente mais tarde ou contate o Giovani.")
    st.error(e)