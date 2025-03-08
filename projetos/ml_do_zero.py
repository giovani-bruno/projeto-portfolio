import streamlit as st
from main import barra_navegacao
from utils import tecnologias, adicionar_tecnologia, botao_voltar, adicionar_video

st.set_page_config(layout='wide', page_title="Machine Learning do Zero")
barra_navegacao()
botao_voltar()

st.title("Implementando Machine Learning do Zero")

st.write("""Este projeto tem como objetivo compreender o funcionamento interno dos modelos de Machine Learning, 
         implementando-os do zero, sem recorrer a bibliotecas especializadas. A proposta é construir cada algoritmo 
         apenas com código puro, explorando os fundamentos matemáticos e computacionais por trás do aprendizado de máquina.""")

st.write("""Tive a ideia para esse projeto a partir do livro Data Science do Zero, de Joel Grus, que explica detalhadamente os 
         princípios dos algoritmos de aprendizado de máquina, desde estatística e álgebra linear até a implementação prática. 
         Esse processo permite um entendimento mais aprofundado de como os modelos tomam decisões e lidam com os dados.""")

st.write("""Após desenvolver cada modelo manualmente, realizamos testes comparando sua precisão com a implementação equivalente da biblioteca scikit-learn.""")

st.write("Atualmente, o projeto conta com a implementação dos seguintes algoritmos:")

st.markdown("""- K-Nearest Neighbors\n- Naive Bayes\n- Regressão Linear Simples""")
         
st.write("""Ao longo do tempo novos modelos serão adicionados, 
         expandindo o repositório com diferentes técnicas de aprendizado de máquina.""")

st.write("[Repositório do projeto no GitHub](https://github.com/giovani-bruno/ml_do_zero)")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2 = st.columns(2)

adicionar_tecnologia(tecnologias['Python'], "Linguagem de programação usada para criar os modelos do zero.", 200, col1)

adicionar_tecnologia(tecnologias['Scikit-learn'], "Biblioteca do Python com foco em machine learning. Foi usada para realizar a comparação da implementação manual do modelo com a da biblioteca.", 150, col2)