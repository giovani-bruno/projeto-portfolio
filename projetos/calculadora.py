import streamlit as st
from main import barra_navegacao
from auxiliar import tecnologias, adicionar_tecnologia, voltar_para_projetos, adicionar_video

st.set_page_config(layout='wide',page_title="Calculadora")
barra_navegacao()
voltar_para_projetos()

st.title("Calculadora")

st.write("""Este projeto consiste no desenvolvimento de uma calculadora 
         simples utilizando Python e a biblioteca Kivy para criar a interface gráfica. 
         A aplicação permite realizar operações matemáticas básicas, como adição, subtração,
         multiplicação e divisão, de forma intuitiva e eficiente.""")

st.write("""Este projeto foi inteiramente desenvolvido por mim, 
         desde a concepção da ideia até a implementação final.
         Esse é um trabalho que reflete exclusivamente minha criatividade e habilidades técnicas.""")

st.write("[Repositório do projeto no GitHub](https://github.com/giovani-bruno/calculadora_kivy)")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2, col3 = st.columns(3)
adicionar_tecnologia(tecnologias['Python'], "Linguagem de programação usada para criar a calculadora.", 
                     200, col1)

adicionar_tecnologia(tecnologias['Kivy'], "Biblioteca do Python usada para criar a janela da calculadora.", 
                     150, col2)

adicionar_tecnologia(tecnologias['Figma'], "Ferramenta utilizada para para criar o layout da calculadora.", 
                     150, col3)

st.divider()

adicionar_video("calculadora.mp4")

st.write("""Este projeto demonstrou como 
         é possível criar uma aplicação funcional e interativa utilizando 
         ferramentas acessíveis. Desde a lógica para realizar operações 
         matemáticas básicas até o desenvolvimento de uma interface gráfica 
         responsiva, este projeto reflete o potencial de Python combinado com a 
         biblioteca Kivy para o desenvolvimento de aplicações simples e intuitivas.""")

st.write("""Futuramente, funcionalidades adicionais, como o suporte 
         a operações mais avançadas ou melhorias na interface, podem 
         ser implementadas para aumentar a utilidade da aplicação.""")
