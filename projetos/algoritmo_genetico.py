import streamlit as st
from main import barra_navegacao
from auxiliar import tecnologias, adicionar_tecnologia, imagem_temp_projetos, voltar_para_projetos

st.set_page_config(layout='wide')
barra_navegacao()
voltar_para_projetos()

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
coluna1, coluna2, coluna3 = st.columns(3)
adicionar_tecnologia(tecnologias['Python'], "Linguagem de programação usada para desenvolver todas as funcionalidades do projeto.", 150, coluna1)
adicionar_tecnologia(tecnologias['Streamlit'], "Biblioteca do Python usada pra criar a interface do projeto.", 150, coluna2)
adicionar_tecnologia(tecnologias['Pandas'], "Biblioteca do Python usada para carregar os dados.", 150, coluna3)
adicionar_tecnologia(tecnologias['Geneticalgorithm'], "Biblioteca do Python usada para treinar o algoritmo genético.", 150, coluna1)

st.divider()

st.image(imagem_temp_projetos)
st.write("""Este projeto mostrou como os Algoritmos Genéticos podem ser aplicados de forma 
         eficaz para resolver problemas complexos de otimização no setor
         logístico. Ao permitir a maximização do lucro respeitando as restrições
          de peso e volume, a solução apresenta-se como uma ferramenta poderosa 
         para apoiar decisões estratégicas no transporte de carga.""")