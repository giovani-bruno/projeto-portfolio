import streamlit as st
from main import barra_navegacao
from utils import tecnologias, adicionar_tecnologia, adicionar_video, botao_voltar

st.set_page_config(layout='wide', page_title="Algoritmo Genético")
barra_navegacao()
botao_voltar()

st.title("Otimizando o Transporte de Carga com Algoritmo Genético")

st.write("""Este projeto utiliza Algoritmos Genéticos para otimizar o 
         transporte de carga em uma empresa aérea fictícia. A solução 
         calcula a melhor combinação de itens a serem transportados, 
         maximizando o lucro enquanto respeita as restrições de peso e volume das aeronaves.""")

st.write("""Com uma interface interativa desenvolvida em Streamlit, 
         o usuário pode carregar dados personalizados em arquivos CSV, visualizar 
         informações como peso, volume e valor dos itens, e obter uma combinação 
         otimizada para o transporte.""")

st.write("Este projeto foi desenvolvido por meio do curso: [Streamlit: Crie 12 Aplicações Web de Inteligência Artificial](https://www.udemy.com/course/streamlit-aplicacoes-web-de-ia)")

st.write("[Repositório do projeto no GitHub](https://github.com/giovani-bruno/algoritmo_genetico)")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2, col3 = st.columns(3)
adicionar_tecnologia(tecnologias['Python'], "Linguagem de programação usada para desenvolver todas as funcionalidades do projeto.", 
                     200, col1)

adicionar_tecnologia(tecnologias['Streamlit'], "Biblioteca do Python usada pra criar a interface do projeto.", 
                     200, col2)

adicionar_tecnologia(tecnologias['Pandas'], "Biblioteca do Python usada para carregar os dados.", 
                     200, col3)

adicionar_tecnologia(tecnologias['Geneticalgorithm'], "Biblioteca do Python usada para treinar o algoritmo genético.", 
                     200, col1)

st.divider()

adicionar_video("algoritmo_genetico.mp4")

st.write("""Este projeto mostrou como os Algoritmos Genéticos podem ser aplicados de forma 
         eficaz para resolver problemas complexos de otimização no setor
         logístico. Ao permitir a maximização do lucro respeitando as restrições
          de peso e volume, a solução apresenta-se como uma ferramenta poderosa 
         para apoiar decisões estratégicas no transporte de carga.""")
