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

adicionar_projeto("prevendo_doenca_cardiaca", col1)

adicionar_projeto("ml_do_zero", col2)

adicionar_projeto("analisando_emprestimos", col3)

adicionar_projeto("prevendo_precos_airbnb", col1)

adicionar_projeto("pesquisa_precos", col2)
             
adicionar_projeto("prevendo_qualidade_carros", col3)

adicionar_projeto("gerador_relatorio", col1)

adicionar_projeto("automacoes_wifi", col2)

adicionar_projeto("algoritmo_genetico", col3)

adicionar_projeto("calculadora", col1)

adicionar_projeto("dashboard_comercial", col2)

adicionar_projeto("dashboard_sac", col3)

adicionar_projeto("dashboard_rh", col1)

adicionar_projeto("portfolio", col2)
