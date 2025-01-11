import streamlit as st
from main import barra_navegacao
from auxiliar import tecnologias, adicionar_tecnologia, adicionar_video, voltar_para_projetos

st.set_page_config(layout='wide', page_title="Prevendo Qualidade de Veículos")
barra_navegacao()
voltar_para_projetos()

st.subheader("Prevendo a Qualidade de Veículos com Machine Learning")

st.write("""Este projeto utiliza algoritmos de aprendizado de máquina 
         para prever a qualidade de veículos com base em suas características, 
         como preço, manutenção, número de portas, capacidade de passageiros, 
         entre outros fatores. A qualidade é categorizada como "Ruim", "Aceitável", "Bom" ou "Muito bom".""")

st.write("Este projeto foi desenvolvido por meio do curso: [Streamlit: Crie 12 Aplicações Web de Inteligência Artificial](https://www.udemy.com/course/streamlit-aplicacoes-web-de-ia)")

st.write("[Repositório do projeto no GitHub](https://github.com/giovani-bruno/prever_qualidade_do_carro)")

st.divider()

st.subheader("Tecnologias Utilizadas")
coluna1, coluna2, coluna3 = st.columns(3)
adicionar_tecnologia(tecnologias['Python'], "Linguagem de programação utilizada para treinar o modelo de machine learning e criar a interface", 
                     150, coluna1)

adicionar_tecnologia(tecnologias['Pandas'], "Biblioteca do Python usada para carregar os dados.", 
                     150, coluna2)

adicionar_tecnologia(tecnologias['Scikit-learn'], "Biblioteca do Python usada para treinar o modelo de machine learning (Random Forest Classifier).", 
                     100, coluna3)

adicionar_tecnologia(tecnologias['Streamlit'], "Biblioteca do Python usada para criar a interface do projeto na web.",
                     150, coluna1)

st.divider()

adicionar_video("prevendo_qualidade_carros.mp4")

st.write("""O projeto Previsão de Qualidade de Veículos demonstrou como 
         técnicas de Machine Learning podem ser aplicadas para prever a 
         qualidade de veículos com base em características específicas. 
         Utilizando o algoritmo Random Forest Classifier, foi possível 
         alcançar um modelo preditivo robusto e confiável, fornecendo 
         insights valiosos para o setor automotivo.""")

st.write("""Com a interface gráfica desenvolvida em Streamlit, 
         a aplicação oferece uma experiência amigável e prática, 
         facilitando o uso para os usuários.""")
