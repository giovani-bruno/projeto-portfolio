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

col1, col2, col3 = st.columns(3)

adicionar_projeto("stark", col1)

adicionar_projeto("prevendo_doenca_cardiaca", col2)

adicionar_projeto("ml_do_zero", col3)

adicionar_projeto("analisando_emprestimos", col1)

adicionar_projeto("prevendo_precos_airbnb", col2)

adicionar_projeto("pesquisa_precos", col3)
             
adicionar_projeto("prevendo_qualidade_carros", col1)

adicionar_projeto("gerador_relatorio", col2)

adicionar_projeto("automacoes_wifi", col3)

adicionar_projeto("algoritmo_genetico", col1)

adicionar_projeto("calculadora", col2)

adicionar_projeto("dashboard_comercial", col3)

adicionar_projeto("dashboard_sac", col1)

adicionar_projeto("dashboard_rh", col2)

adicionar_projeto("portfolio", col3)
