import streamlit as st

st.set_page_config(layout='centered')
st.title("Projetos")
st.write("""
### Explore meus projetos
Aqui estão os principais projetos que desenvolvi. Cada projeto reflete meu aprendizado e dedicação para resolver problemas reais e criar soluções impactantes.
""")
st.divider()

def adicionar_projeto(nome, descricao, link, tecnologias_utilizadas, imagem):
    st.subheader(nome)
    st.write(descricao)
    st.write(tecnologias_utilizadas)
    st.image(f"imagens/{imagem}")
    st.write(f"[Link para o repositório]({link})")
    st.divider()

adicionar_projeto("Analisando Empréstimos dos Livros de uma Biblioteca", 
                """Este projeto analisa os dados de empréstimos do sistema de bibliotecas da UFRN para entender padrões e tendências no uso dos materiais informacionais.""",
                "https://github.com/giovani-bruno/analisando_emprestimos",
                "Python, pandas, matplotlib, seaborn", "projeto_emprestimos.png")
