#TODO finalizar as seguintes paginas: analise_lideres.py e automacoes_wifi.py
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

    for pagina in listdir("projetos"):
        if pagina == "videos":
            continue
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