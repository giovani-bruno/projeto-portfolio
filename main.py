#TODO inserir o video do projeto em cada pagina individual dos projetos
#TODO colocar o nome das seguintes tecnologias do lado da logo: power bi, excel, git e tkinter
#TODO criar uma imagem pra cada projeto

import streamlit as st
from os import listdir

def main():
    paginas = [
        st.Page("Sobre.py", title="👨‍💻 Sobre mim"),
        st.Page("Certificados.py", title="📃 Certificados"), 
        st.Page("Leituras.py", title="📚 Leituras"),
        st.Page("Projetos.py", title="💻 Projetos")
        ]

    paginas_projetos = listdir("projetos")
    for pagina in paginas_projetos:
        paginas.append(st.Page(f"projetos/{pagina}"))
    
    pg = st.navigation(paginas, position='hidden')
    
    pg.run()

def barra_navegacao():
    st.sidebar.page_link("Sobre.py")
    st.sidebar.page_link("Certificados.py")
    st.sidebar.page_link("Leituras.py")
    st.sidebar.page_link("Projetos.py")

if __name__ == "__main__":
    main()