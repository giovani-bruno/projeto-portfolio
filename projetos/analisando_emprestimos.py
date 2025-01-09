import streamlit as st
from main import barra_navegacao
from auxiliar import tecnologias, adicionar_tecnologia

st.set_page_config(layout='wide')
barra_navegacao()

st.title("Analisando os dados de empréstimos dos acervos do sistema de bibliotecas da UFRN")
st.write("""Este projeto analisa os dados de empréstimos do sistema de bibliotecas da UFRN 
         para entender padrões e tendências no uso dos materiais informacionais.
         A partir dos registros de empréstimos, busquei responder perguntas como: 
         a evolução da quantidade de empréstimos ao longo dos anos, as bibliotecas 
         mais movimentadas, e os temas mais e menos populares. O objetivo é fornecer 
         uma visão abrangente para auxiliar a diretoria das bibliotecas a tomar decisões estratégicas, 
         como melhorar a infraestrutura, alocar recursos de forma eficiente e otimizar os processos, 
         garantindo que as bibliotecas atendam melhor às necessidades dos usuários.""")
st.write('Este projeto foi realizado por meio do desafio "7 Days of Code" da Alura, onde, a cada dia, foi apresentado um novo desafio relacionado à análise de dados para ser resolvido.')
st.write("[Repositório do projeto no GitHub](https://github.com/giovani-bruno/analisando_emprestimos)")
st.divider()

st.subheader("Tecnologias Utilizadas")
coluna1, coluna2, coluna3 = st.columns(3)
adicionar_tecnologia(tecnologias['Python'], "Linguagem de programação usada para analisar, manipular e visualizar os dados.", 150, coluna1)
adicionar_tecnologia(tecnologias['Pandas'], "Biblioteca do Python usada para ler, tratar e manipular os dados.", 150, coluna2)
adicionar_tecnologia(tecnologias['Matplotlib'], "Biblioteca do Python usada para criar os gráficos.", 150, coluna3)
adicionar_tecnologia(tecnologias['Seaborn'], "Outra biblioteca do Python usada para criar gráficos.", 150, coluna1)
st.divider()

st.image("imagens/imagem_projetos_temp.png")
st.write("""A análise dos dados de empréstimos do sistema de bibliotecas da UFRN 
         revelou insights valiosos sobre o uso dos acervos e o comportamento dos usuários. 
         Foi possível identificar padrões na evolução dos empréstimos ao longo dos anos, 
         destacar as bibliotecas mais movimentadas e compreender quais temas são mais ou menos 
         populares entre os leitores. Essas informações oferecem uma base sólida para decisões estratégicas, permitindo à diretoria das bibliotecas planejar melhorias na infraestrutura, direcionar recursos de forma mais eficaz e aprimorar os processos operacionais. Com isso, as bibliotecas podem se tornar ainda mais alinhadas às necessidades dos usuários, promovendo maior acesso e engajamento com os materiais informacionais.""")
