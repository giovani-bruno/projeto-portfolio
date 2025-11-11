import streamlit as st
from main import barra_navegacao
from utils import livros, adicionar_livro

st.set_page_config(page_title='Leituras', layout='wide', page_icon='📚')
barra_navegacao()

st.title("Leituras")
st.write("#### 📚 Livros que já li e que estou lendo")
st.write("""Aqui compartilho os livros que me ajudaram a expandir meu conhecimento na área de dados. 
A leitura constante é uma das minhas formas favoritas de aprender e crescer profissionalmente.""")
st.divider()

adicionar_livro(livros["Hands on ML"], """Esse livro foi fundamental para consolidar meu entendimento sobre machine learning na prática. 
                Através de exemplos bem estruturados e aplicações reais, aprofundei meus conhecimentos em pré-processamento de dados, escolha 
                e ajuste de modelos, avaliação de desempenho e uso de redes neurais com Keras e TensorFlow. Além de fortalecer minha base teórica, 
                o livro me ajudou a desenvolver uma visão mais prática sobre o ciclo completo de um projeto de aprendizado de máquina, desde a 
                preparação dos dados até a implantação de modelos. Sem dúvida, foi uma leitura essencial para aprimorar minhas habilidades na área de dados.""", 
                frase="Aprendizado de máquina é a ciência (e a arte) da programação de computadores de modo que eles possam aprender com os dados.")

adicionar_livro(livros['Data Science'], """O título do livro me enganou um pouco. Pelo nome, imaginei que 
                fosse um material introdutório para quem quer começar na área de Data Science. No entanto, 
                o "do zero" no título significa que o autor ensina a construir todos os conceitos na prática, 
                sem depender de bibliotecas prontas. Ele desenvolve tudo do zero, desde cálculos estatísticos 
                e álgebra linear até modelos de Machine Learning.
                Isso torna a leitura bastante densa, exigindo muito código e matemática. 
                O livro não é exatamente uma introdução à área, mas sim um material para quem 
                deseja entender e implementar os fundamentos de Data Science na raiz. 
                Para acompanhá-lo bem, é essencial ter conhecimentos prévios em estatística, 
                probabilidade e matemática.
                Em resumo, gostei do livro, pois ele aborda conceitos fundamentais e mostra como 
                aplicá-los na prática. No entanto, devido à complexidade dos tópicos, não o 
                recomendaria para iniciantes, mas sim para quem já tem experiência na área e 
                deseja aprofundar seus conhecimentos.
                """, frase="Vivemos em mundo cada vez mais imerso em dados.")

adicionar_livro(livros['Python Dados'], """Escrito pelo criador da biblioteca pandas, aprendi a importância 
                de dominar as ferramentas do Python para lidar com dados de forma eficiente. 
                A obra me proporcionou uma compreensão profunda de como o Python pode ser 
                usado para explorar, limpar, manipular e visualizar dados. Desde o início, 
                aprendi a trabalhar com o Pandas, uma das bibliotecas mais poderosas para 
                análise de dados, o que me ajudou a organizar dados em DataFrames e realizar 
                operações complexas de forma simples e rápida. 
                Além disso, pude entender como utilizar o NumPy para trabalhar com arrays e 
                operações numéricas, e como essas ferramentas se complementam perfeitamente 
                no processamento de dados.""", frase="Uma preparação de dados eficiente pode aumentar significativamente a produtividade, permitindo que você passe mais tempo analisando dados e menos tempo preparando-o para análise.")

adicionar_livro(livros['Storytelling'], '''
                Aprendi que a verdadeira essência de uma boa visualização de dados
                vai além de simplesmente apresentar números. 
               É sobre contar uma história com os dados de forma que o público
                consiga entender a mensagem de maneira clara e envolvente. 
               A autora reforça que a escolha de gráficos, o design visual
                e o contexto são fundamentais para transmitir a informação de forma eficaz.''', frase="Há uma história em seus dados, mas suas ferramentas não sabem qual é essa história.")
