import streamlit as st
from main import barra_navegacao
from auxiliar import livros, adicionar_livro

st.set_page_config(page_title='Leituras', layout='wide', page_icon='📚')
barra_navegacao()

st.title("Leituras")
st.write("#### 📚 Livros que já li e que estou lendo")
st.write("""Aqui compartilho os livros que me ajudaram a expandir meu conhecimento na área de dados. 
A leitura constante é uma das minhas formas favoritas de aprender e crescer profissionalmente.""")
st.divider()

adicionar_livro(livros['Storytelling com Dados']['imagem'], "Storytelling com Dados", livros['Storytelling com Dados']["autor (a)"], '''
                Aprendi que a verdadeira essência de uma boa visualização de dados
                vai além de simplesmente apresentar números. 
               É sobre contar uma história com os dados de forma que o público
                consiga entender a mensagem de maneira clara e envolvente. 
               A autora reforça que a escolha de gráficos, o design visual
                e o contexto são fundamentais para transmitir a informação de forma eficaz.
                Minha frase favorita desse livro é: "Há uma história em seus dados, mas suas ferramentes não sabem qual é essa história."''')

adicionar_livro(livros['Python para Análise de Dados']['imagem'], "Python para Análise de Dados", livros['Python para Análise de Dados']['autor (a)'], """Escrito pelo criador da biblioteca pandas, aprendi a importância 
                de dominar as ferramentas do Python para lidar com dados de forma eficiente. 
                A obra me proporcionou uma compreensão profunda de como o Python pode ser 
                usado para explorar, limpar, manipular e visualizar dados. Desde o início, 
                aprendi a trabalhar com o Pandas, uma das bibliotecas mais poderosas para 
                análise de dados, o que me ajudou a organizar dados em DataFrames e realizar 
                operações complexas de forma simples e rápida. 
                Além disso, pude entender como utilizar o NumPy para trabalhar com arrays e 
                operações numéricas, e como essas ferramentas se complementam perfeitamente 
                no processamento de dados.""")

adicionar_livro(livros['Data Science do Zero']['imagem'], "Data Science do Zero", livros['Data Science do Zero']['autor (a)'], "Lendo! Feedback em breve...")