import streamlit as st
from main import barra_navegacao

st.set_page_config(page_title='Projetos', layout='wide', page_icon='💻')
barra_navegacao()

st.title("Projetos")
st.write("""
### Explore meus projetos
Aqui estão os principais projetos que desenvolvi. Cada projeto reflete meu aprendizado e dedicação para resolver problemas reais.
""")
st.divider()

col1, col2, col3 = st.columns(3)

def adicionar_projeto(nome, tecnologias_utilizadas, imagem, link_pagina, coluna):
    with coluna.container(border=True, height=375):
        st.write(f"##### {nome}")
        st.image(f"imagens/{imagem}")
        st.write(f"#{' #'.join(tecnologias_utilizadas)}")
        st.write("")
        c1, c2, = st.columns([0.4, 1])
        if c2.button("Ver Projeto", key=nome):
            st.switch_page(link_pagina)

adicionar_projeto("Analisando Empréstimos dos Livros de uma Biblioteca",
                ["Python", "pandas", "matplotlib", "seaborn"], "projeto_emprestimos.png", "teste.py", col1)

adicionar_projeto("Prevendo Preços de Imóveis no Airbnb",
                ["Python", "pandas", "numpy", "matplotlib", "seaborn", "plotly", "scikit-learn"], "projeto_emprestimos.png", "teste2.py", col2)

adicionar_projeto("Pesquisa de Preços",
                ["Python", "pandas", "Selenium", "Tkinter", "smtplib"], "projeto_emprestimos.png", "teste.py", col3)
             
adicionar_projeto("Prevendo a Qualidade de Carros",
                ["Python", "pandas", "streamlit", "scikit-learn"], "projeto_emprestimos.png", "teste.py", col1)

adicionar_projeto("Gerador de Relatório",
                  ["Python", "streamlit", "ReportLab", "pandas", "smtplib"], "projeto_emprestimos.png", "teste.py", col2)

adicionar_projeto("Automações em um Wifi Corporativo",
                ["Python", "Tkinter", "Selenium", "smtplib"], "projeto_emprestimos.png", "teste.py", col3)

adicionar_projeto("Algoritmo Genético para Otimzação",
                ["Python", "pandas", "streamlit", "genetical algorithm"], "projeto_emprestimos.png", "teste.py", col1)

adicionar_projeto("Análise de Desempenho dos Líderes",
                ["Python", "pandas", "streamlit", "plotly"], "projeto_emprestimos.png", "teste.py", col2)

adicionar_projeto("Calculadora",
                ["Python", "Kivy"], "projeto_emprestimos.png", "teste.py", col3)
