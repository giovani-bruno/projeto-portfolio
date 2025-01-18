import streamlit as st
from main import barra_navegacao
from auxiliar import tecnologias, adicionar_tecnologia, voltar_para_projetos, adicionar_video

st.set_page_config(layout='wide', page_title="Prevendo Preços no Airbnb")
barra_navegacao()
voltar_para_projetos()

st.title("Prevendo Preços de Imóveis no Airbnb com Machine Learning")

st.write("""Este projeto aplicou técnicas de Machine Learning para 
         desenvolver um modelo preditivo capaz de estimar o preço de 
         imóveis anunciados no Airbnb. O modelo utiliza características 
         como quantidade de quartos, banheiros, localização e 
         outros fatores para realizar as previsões. O objetivo é fornecer 
         uma ferramenta prática que beneficie tanto proprietários, 
         ajudando-os a definir preços competitivos para seus imóveis, 
         quanto consumidores, permitindo avaliar a justiça dos preços anunciados. 
         A iniciativa demonstra o potencial da inteligência artificial em apoiar 
         decisões no mercado imobiliário.""")

st.write("Este projeto foi realizado por meio do curso Python Impressionador da Hashtag Treinamentos.")

st.write("[Repositório do projeto no GitHub](https://github.com/giovani-bruno/ml_prever_precos_airbnb)")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2, col3 = st.columns(3)
adicionar_tecnologia(tecnologias["Python"], "Linguagem de programação usada para analisar os dados e treinar os modelos de machine learning.", 
                     200, col1)

adicionar_tecnologia(tecnologias["Pandas"], "Biblioteca do Python usada para ler, tratar e manipular os dados.", 
                     200, col2)

adicionar_tecnologia(tecnologias["NumPy"], "Biblioteca do Python usada para tratar os dados de forma mais eficiente.", 
                     200, col3)

adicionar_tecnologia(tecnologias["Matplotlib"], "Biblioteca do Python usada para criar os gráficos.", 
                     200, col1)

adicionar_tecnologia(tecnologias["Seaborn"], "Outra biblioteca do Python usada para criar gráficos.", 
                     200, col2)

adicionar_tecnologia(tecnologias["Plotly"], "Biblioteca do Python usada para criar gráficos interativos.", 
                     200, col3)

adicionar_tecnologia(tecnologias["Scikit-learn"], "Biblioteca do Python usada para treinar os modelos de machine learning.", 
                     150, col1)

st.divider()

adicionar_video("prevendo_precos_airbnb.mp4")

st.write("""O desenvolvimento do modelo de previsão de preços de imóveis 
         no Airbnb utilizando técnicas de Machine Learning proporcionou 
         uma ferramenta eficaz para análise de preços no mercado de 
         aluguel temporário. Este projeto não só demonstrou o poder 
         de Machine Learning para a análise de dados complexos e a 
         previsão de variáveis de mercado, mas também forneceu uma 
         solução prática e útil para usuários do Airbnb.""")
