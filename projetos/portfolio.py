import streamlit as st
from main import barra_navegacao
from utils import tecnologias, adicionar_tecnologia, voltar_para_projetos

st.set_page_config(layout='wide', page_title="Meu Portfólio")
barra_navegacao()
voltar_para_projetos()

st.title("Meu Portfólio Interativo em Python com Streamlit")

st.write("""Este projeto é uma aplicação web interativa desenvolvida com Streamlit, 
         que funciona como meu portfólio profissional. Ela foi criada para apresentar 
         minha trajetória, certificações, leituras e projetos de forma organizada, dinâmica e 
         visualmente atraente. O objetivo principal é proporcionar uma experiência interativa 
         para quem deseja conhecer meu trabalho e habilidades.""")

st.write("[Repositório do projeto no GitHub](https://github.com/giovani-bruno/projeto-portfolio)")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2, col3 = st.columns(3)

adicionar_tecnologia(tecnologias['Python'], "Linguagem de programação usada para criar toda a aplicação.", 200, col1)
adicionar_tecnologia(tecnologias['Streamlit'], "Biblioteca do Python usada para criar a aplicação na web.", 200, col2)
adicionar_tecnologia(tecnologias['Canva'], "Ferramenta usada para criar as imagens de cada projeto.", 150, col3)
adicionar_tecnologia(tecnologias['FormSubmit'], "Ferramenta usada para criar o formulário para contato na pagina sobre mim.", 250, col1)
