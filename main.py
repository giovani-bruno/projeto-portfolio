import streamlit as st

pg = st.navigation([
    st.Page("Sobre.py", title="👨‍💻 Sobre mim"),
    st.Page("Certificados.py", title="📃 Certificados"), 
    st.Page("Leituras.py", title="📚 Leituras"),
    st.Page("Projetos.py", title="💻 Projetos"),
    st.Page("teste.py")
    ], position='hidden')

def barra_navegacao():
    st.sidebar.page_link("Sobre.py")
    st.sidebar.page_link("Certificados.py")
    st.sidebar.page_link("Leituras.py")
    st.sidebar.page_link("Projetos.py")

pg.run()