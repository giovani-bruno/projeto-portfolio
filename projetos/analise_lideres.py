import streamlit as st
from main import barra_navegacao
from auxiliar import tecnologias, adicionar_tecnologia, voltar_para_projetos

st.set_page_config(layout='wide', page_title="Análise dos Líderes")
barra_navegacao()
voltar_para_projetos()

st.title("Analisando o Desempenho dos Líderes")

st.write("""Este é um projeto freelancer desenvolvido para mais de um cliente, 
         com o objetivo de analisar o desempenho de mais de 200 líderes durante 
         as eleições para vereador na cidade de Ananindeua, no Pará. Cada líder 
         era responsável por recrutar eleitores para votar no seu candidato, 
         registrando essas pessoas em zonas e seções específicas, associadas a bairros e locais. 
         A análise foi realizada comparando a quantidade de votos recebidos pelo vereador em uma 
         seção com o número de pessoas recrutadas pelo líder na mesma seção.""")

st.write("""Por exemplo, se um líder recrutou 8 pessoas para a seção 130, 
         mas o vereador recebeu apenas 2 votos nessa seção, o desempenho 
         foi considerado ruim. Por outro lado, se outro líder recrutou 6 
         pessoas para a seção 140 e o vereador recebeu 5 votos, o desempenho foi considerado bom.""")

st.write("Para entregar esses insights de forma clara e acessível, foi desenvolvida uma aplicação web com Streamlit, contendo três módulos principais:")

st.write("1. Análise por Zona e Seção: Permite visualizar e resumir dados por zona e seção eleitoral.")

st.write("2. Análise por Local e Bairro: Oferece resumos por local ou bairro, auxiliando na compreensão de áreas de maior ou menor engajamento.")

st.write("3. Análise por Líder e Seção: Filtra seções com base no número de votos recebido, permitindo identificar seções com desempenho crítico (exemplo: seções com 0 votos).")

st.write("""A aplicação utiliza gráficos interativos desenvolvidos com Plotly, 
         além de métricas detalhadas que mostram a quantidade de votos recebidos 
         pelo vereador em cada zona, local e bairro. Isso permite identificar os 
         melhores e piores líderes, auxiliando na tomada de decisões, como premiação 
         dos líderes mais eficientes ou substituição daqueles com baixo desempenho.""")

st.write("""Este projeto foi um dos mais completos já desenvolvidos, 
         abrangendo desde o tratamento e modelagem dos dados 
         (que inicialmente estavam em formato inadequado para análise) 
         até a visualização interativa.""")

st.write("""Este projeto foi desenvolvido 100% por mim, abrangendo todas as etapas do processo, 
         desde a modelagem e tratamento dos dados, até a implementação da aplicação web e criação 
         das visualizações interativas.
         Esse é um trabalho que reflete exclusivamente minha criatividade e habilidades técnicas.""")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2, col3 = st.columns(3)

adicionar_tecnologia(tecnologias['Python'], 
                     "Linguagem de programação usada para desenvolver toda a aplicação, deste o tratamento de dados até a aplicação web.",
                     200, col1)

adicionar_tecnologia(tecnologias['Streamlit'], 
                     "Biblioteca do Python responsável por criar a aplicação na web.",
                     200, col2)

adicionar_tecnologia(tecnologias['Pandas'], 
                     "Biblioteca do Python usada para manipular e tratar os dados.",
                     200, col3)

adicionar_tecnologia(tecnologias['Plotly'],
                     "Biblioteca do Python usada para criar os gráficos interativos.",
                     200, col1)

st.divider()

st.write("""Este projeto foi essencial para fornecer aos clientes uma 
         visão detalhada e estratégica sobre o desempenho de seus líderes 
         durante as eleições. Através de uma aplicação web interativa, foi 
         possível identificar os líderes mais eficazes e aqueles que não 
         atingiram os resultados esperados, com base em dados concretos de recrutamento e votação.""")

st.write("Com este trabalho, foi possível agregar valor aos clientes, otimizando a compreensão de seus processos e contribuindo para o sucesso nas próximas campanhas.")
