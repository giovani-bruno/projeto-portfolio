import streamlit as st
from main import barra_navegacao
from auxiliar import adicionar_projeto

st.set_page_config(page_title='Projetos', layout='wide', page_icon='💻')
barra_navegacao()

st.title("Projetos")
st.write("""
### Explore meus projetos
Aqui estão os principais projetos que desenvolvi. Cada projeto reflete meu aprendizado e dedicação para resolver problemas reais.
""")
st.divider()

col1, col2, col3 = st.columns(3)

adicionar_projeto("Analisando Empréstimos dos Livros", "analisando_emprestimos.png", "analisando_emprestimos.py", col1)

adicionar_projeto("Prevendo Preços de Imóveis no Airbnb", "prevendo_precos_airbnb.png", "prevendo_precos_airbnb.py", col2)

adicionar_projeto("Pesquisa de Preços", "pesquisa_precos.png", "pesquisa_precos.py", col3)
             
adicionar_projeto("Prevendo a Qualidade de Carros", "prevendo_qualidade_carros.png", "prevendo_qualidade_carros.py", col1)

adicionar_projeto("Gerador de Relatório", "gerador_relatorio.png", "gerador_relatorio.py", col2)

adicionar_projeto("Automações em um Wi-Fi Corporativo", "automacoes_wifi.png", "automacoes_wifi.py", col3)

adicionar_projeto("Algoritmo Genético para Otimização", "algoritmo_genetico.png", "algoritmo_genetico.py", col1)

adicionar_projeto("Analisando o Desempenho dos Líderes", "analise_lideres.png", "analise_lideres.py", col2)

adicionar_projeto("Calculadora", "calculadora.png", "calculadora.py", col3)
