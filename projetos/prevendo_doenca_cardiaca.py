import streamlit as st
from main import barra_navegacao
from utils import tecnologias, adicionar_tecnologia, botao_voltar, adicionar_video, acessar_repositorio

st.set_page_config(layout='wide', page_title="Prevendo Doença Cardíaca")
barra_navegacao()
botao_voltar()

st.title("Prevendo Doença Cardíaca com Machine Learning")

st.write("""Neste projeto, aplico técnicas de Machine Learning para 
         prever o risco de doença cardíaca a partir de dados clínicos e comportamentais de pacientes. 
         Utilizo um conjunto de dados realista, que inclui informações como idade, colesterol, pressão arterial, 
         hábitos de vida e histórico familiar. O objetivo principal foi desenvolver um modelo preditivo capaz 
         de auxiliar profissionais de saúde a tomarem decisões mais informadas, além de mostrar como a ciência de dados 
         pode fazer a diferença em áreas tão críticas quanto a saúde. Ao longo deste projeto, passo por todas as 
         etapas de um processo de Data Science, desde a análise exploratória dos dados até a criação e avaliação 
         de modelos de machine learning, buscando sempre garantir a melhor performance possível.""")

st.write("""Este projeto foi inteiramente desenvolvido por mim, 
         desde a concepção da ideia até a implementação final.
         Esse é um trabalho que reflete exclusivamente minha criatividade e habilidades técnicas.""")

st.write("Eu palestrei na minha faculdade para alguns alunos sobre esse projeto, onde apresento o problema, a solução, e a implementaçao passo a passo.")

acessar_repositorio("https://github.com/giovani-bruno/prever_doenca_cardiaca")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2, col3 = st.columns(3)
adicionar_tecnologia(tecnologias['Python'], "Linguagem de programação principal utilizada para desenvolver o projeto.", 
                     200, col1)

adicionar_tecnologia(tecnologias['Pandas'], "Biblioteca usada para analisar os dados.", 
                     200, col2)

adicionar_tecnologia(tecnologias['NumPy'], "Biblioteca para manipular os dados eficientemente.", 
                     200, col3)

adicionar_tecnologia(tecnologias['Scikit-learn'], "Biblioteca principal usada para treinar os algoritmos de machine learning.", 
                     150, col1)

adicionar_tecnologia(tecnologias['Matplotlib'], "Usado para gerar os gráficos na etapa da análise exploratória.",
                     200, col2)

adicionar_tecnologia(tecnologias['Seaborn'], "Outra biblioteca usada para gerar gráficos.",
                     200, col3)

adicionar_tecnologia(tecnologias['Streamlit'], "Usado para criar a aplicação do modelo em produção.",
                     200, col1)

adicionar_tecnologia(tecnologias['Joblib'], "Biblioteca usada para salvar o modelo treinado para usá-lo em produção.",
                     120, col2)

st.divider()

adicionar_video("prever_doenca_cardiaca.mp4")
adicionar_video("prever_doenca_cardiaca_deploy.mp4")

st.write("Esse projeto reforça como a ciência de dados pode ir além dos números, ajudando a transformar informações em ações práticas que impactam vidas.")
