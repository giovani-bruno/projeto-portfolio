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

adicionar_projeto("ml_do_zero", col1)

adicionar_projeto("analisando_emprestimos", col2)

adicionar_projeto("prevendo_precos_airbnb", col3)

adicionar_projeto("pesquisa_precos", col1)
             
adicionar_projeto("prevendo_qualidade_carros", col2)

adicionar_projeto("gerador_relatorio", col3)

adicionar_projeto("automacoes_wifi", col1)

adicionar_projeto("algoritmo_genetico", col2)

adicionar_projeto("calculadora", col3)

adicionar_projeto("dashboard_comercial", col1)

adicionar_projeto("dashboard_sac", col2)

adicionar_projeto("dashboard_rh", col3)

adicionar_projeto("portfolio", col1)
