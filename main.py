import streamlit as st
from os import listdir

def main():
    paginas = [
        st.Page("Sobre.py", title="👨‍💻 Sobre mim"),
        st.Page("Certificados.py", title="📃 Certificados"), 
        st.Page("Leituras.py", title="📚 Leituras"),
        st.Page("Projetos.py", title="💻 Projetos"),
        st.Page("Stark.py", title="🤖 Stark")
        ]

    for pagina in listdir("projetos"):
        if pagina == "videos-imagens":
            continue
        paginas.append(st.Page(f"projetos/{pagina}"))
    
    pg = st.navigation(paginas, position='hidden')
    
    pg.run()

def barra_navegacao():
    st.sidebar.page_link("Sobre.py")
    st.sidebar.page_link("Certificados.py")
    st.sidebar.page_link("Leituras.py")
    st.sidebar.page_link("Projetos.py")
    st.sidebar.page_link("Stark.py")

if __name__ == "__main__":
    main()