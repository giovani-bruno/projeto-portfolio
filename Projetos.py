import streamlit as st
from main import barra_navegacao
from utils import adicionar_projeto

st.set_page_config(page_title='Projetos', layout='wide', page_icon='💻')
barra_navegacao()

st.title("Projetos")
st.write("""
### Explore meus projetos
Aqui estão os principais projetos que desenvolvi. Cada projeto reflete meu aprendizado e dedicação para resolver problemas.
""")
st.divider()

projetos = [
    "stark",
    "prevendo_doenca_cardiaca",
    "ml_do_zero",
    "analisando_emprestimos",
    "prevendo_precos_airbnb",
    "pesquisa_precos",
    "prevendo_qualidade_carros",
    "gerador_relatorio",
    "automacoes_wifi",
    "algoritmo_genetico",
    "calculadora",
    "dashboard_comercial",
    "dashboard_sac",
    "dashboard_rh",
    "portfolio"
]

colunas = st.columns(3)
for i, projeto in enumerate(projetos):
    coluna = colunas[i % 3]
    adicionar_projeto(projeto, coluna)
