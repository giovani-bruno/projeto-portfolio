import streamlit as st
from main import barra_navegacao
from auxiliar import tecnologias, adicionar_tecnologia, voltar_para_projetos, imagem_temp_projetos

st.set_page_config(layout='wide', page_title="Automações no Wifi")
barra_navegacao()
voltar_para_projetos()

st.title("Automações em um Wifi Corporativo")
