import streamlit as st

def main():
    pg = st.navigation([
        st.Page("Sobre.py", title="👨‍💻 Sobre mim"),
        st.Page("Certificados.py", title="📃 Certificados"), 
        st.Page("Leituras.py", title="📚 Leituras"),
        st.Page("Projetos.py", title="💻 Projetos"),
        st.Page("teste.py")
        ], position='hidden')
    
    pg.run()

def barra_navegacao():
    st.sidebar.page_link("Sobre.py")
    st.sidebar.page_link("Certificados.py")
    st.sidebar.page_link("Leituras.py")
    st.sidebar.page_link("Projetos.py")

if __name__ == "__main__":
    main()