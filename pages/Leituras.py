import streamlit as st

st.set_page_config(layout='centered')
st.title("Leituras")
st.write("#### 📚 Livros que já li e que estou lendo")
st.write("""Aqui compartilho os livros que me ajudaram a expandir meu conhecimento na área de ciência de dados e tecnologia. 
A leitura constante é uma das minhas formas favoritas de aprender e crescer profissionalmente.""")
st.divider()

def adicionar_livro(imagem_livro, resumo):
    col1, col2 = st.columns(2)
    col1.image(f"imagens/{imagem_livro}")
    col2.write(resumo)
    st.divider()

adicionar_livro("livro_storytelling.jpg", """
                No livro [Storytelling com Dados](https://a.co/d/3BcAYfq), de Cole Nussbaumer Knaflic, 
               aprendi que a verdadeira essência de uma boa visualização de dados
                vai além de simplesmente apresentar números. 
               É sobre contar uma história com os dados de forma que o público
                consiga entender a mensagem de maneira clara e envolvente. 
               A autora reforça que a escolha de gráficos, o design visual
                e o contexto são fundamentais para transmitir a informação de forma eficaz.""")

adicionar_livro("livro_python_dados.jpg", """No livro [Python para Análise de Dados](https://a.co/d/59oeRPK), 
                de Wes McKinney, o criador da biblioteca pandas, aprendi a importância 
                de dominar as ferramentas do Python para lidar com dados de forma eficiente. 
                A obra me proporcionou uma compreensão profunda de como o Python pode ser 
                usado para explorar, limpar, manipular e visualizar dados. Desde o início, 
                aprendi a trabalhar com o Pandas, uma das bibliotecas mais poderosas para 
                análise de dados, o que me ajudou a organizar dados em DataFrames e realizar 
                operações complexas de forma simples e rápida. 
                Além disso, pude entender como utilizar o NumPy para trabalhar com arrays e 
                operações numéricas, e como essas ferramentas se complementam perfeitamente 
                no processamento de dados.""")

adicionar_livro("livro_data_science.jpg", "Lendo! Feedback em breve...")