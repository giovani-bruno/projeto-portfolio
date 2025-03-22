import streamlit as st
from utils import adicionar_certificado
from main import barra_navegacao

st.set_page_config(page_title="Certificados", layout='centered', page_icon='📃')
barra_navegacao()

st.title("Certificados")
st.write("#### Nesta página você encontra todos os meus certificados conquistados até o momento.")
st.divider()

adicionar_certificado("Data Science Methodology", "6h", "18/03/2025", "20/03/2025",
                      """Aprendi sobre as principais etapas da metodologia de ciência de dados, incluindo a formulação do problema, 
                      coleta e compreensão dos dados, preparação para modelagem, construção e avaliação de modelos. O curso abordou o 
                      processo CRISP-DM e explorou diferentes tipos de modelos analíticos, como preditivos, descritivos e de classificação""")

adicionar_certificado("Tools for Data Science", "18h", "13/03/2025", "18/03/2025", 
                      """Explorei as principais linguagens, bibliotecas e ferramentas usadas por cientistas de dados, 
                      incluindo Jupyter Notebooks, RStudio IDE e IBM Watson Studio. 
                      Aprendi suas funcionalidades, e como aplicá-las em 
                      projetos práticos de data science.""")

adicionar_certificado("What is Data Science", "11h", "08/03/2025", "12/03/2025",
                      """Desenvolvi uma compreensão sólida sobre os fundamentos da ciência de dados, 
                      explorando o papel do cientista de dados, o ciclo de vida de um projeto, a importância da 
                      ética na análise de dados e como transformar dados em insights acionáveis para a tomada de decisões.
                      Este é o primeiro curso do programa de Certificação Profissional em Ciência de Dados da IBM.""",
                      nome_alt="What is Data Science?")

adicionar_certificado("Python Data Visualization - Dashboards with Plotly & Dash", "8h", "22/01/2025", "29/01/2025",
                      """Aprendi a criar dashboards interativos e profissionais utilizando as bibliotecas Dash e Plotly do Python. 
                      O curso abordou desde os conceitos básicos da estrutura de uma aplicação Dash até a construção de dashboards completos, 
                      explorando vários tipos de visualizações.""")

adicionar_certificado("Estatística para Ciência de Dados e Machine Learning", "20h", "03/01/2025", "21/01/2025",
                       """Aprendi os principais conceitos de estatística e probabilidade aplicados à ciência de dados, 
                       explorando tanto a teoria quanto a prática. O curso abordou tópicos fundamentais como distribuições, 
                       intervalos de confiança, testes de hipóteses, correlações e outros conceitos essenciais para análises de dados e modelos de machine learning. 
                       Gostei muito desse assunto e pretendo me aprofundar ainda mais para ampliar minhas habilidades e conhecimentos na área.""")

adicionar_certificado("Power BI Impressionador", "118h", "20/11/2024", "02/01/2025", 
                      """Desenvolvi habilidades para criar dashboards dinâmicos e 
                      visualizações impactantes, dominando o tratamento de dados no 
                      Power Query e fórmulas DAX, das mais básicas até as mais avançadas.""")

adicionar_certificado("Análise de Dados Impressionadora", "104h", "06/07/2024", "20/12/2024",
                      """Um curso abrangente que me prepara para atuar como analista de dados, 
                      abordando as principais ferramentas do mercado. Aprendi a organizar e tratar dados no Excel, 
                      criar dashboards interativos no Power BI, realizar consultas avançadas em SQL, 
                      automatizar análises com Python e aplicar inteligência artificial para obter insights. 
                      Esse conhecimento integrado me permite transformar dados em decisões estratégicas com confiança.""")

adicionar_certificado("Amazon AWS Certified Cloud Practitioner CLF-C02", "16h", "08/11/2024", "16/11/2024",
                      """Sou uma pessoa fascinada pela computação em nuvem e 
                      em como ela inova o jeito de operar das empresas. 
                      Aprendi como começar na AWS com este curso que me 
                      prepara para a prova de certificação "AWS Cloud Practitioner", 
                      que testa conhecimentos básicos sobre os serviços da AWS.""")

adicionar_certificado("SQL Impressionador", "90h", "26/09/2024", "24/10/2024",
                      """Aprendi a usar SQL para explorar, manipular e 
                      consultar bancos de dados com eficiência. 
                      O curso abordou desde conceitos básicos, 
                      como seleções e filtros, até técnicas avançadas 
                      para transformar dados em insights valiosos, 
                      essenciais para análises e tomadas de decisão.""")
adicionar_certificado("Inteligência Artificial Impressionador", "55h", "06/09/2024", "23/09/2024", 
                      """Descobri como integrar ferramentas de inteligência artificial, 
                      como ChatGPT, Gemini e Copilot, no dia a dia profissional, 
                      aumentando a produtividade e aplicando a tecnologia em 
                      diferentes áreas.""")

adicionar_certificado("Python Impressionador", "124h", "07/03/2024", "10/07/2024",
                      """Dominei os fundamentos e conhecimentos avançados de Python, 
                      explorando estruturas de dados, bibliotecas populares, 
                      e desenvolvendo diversos projetos práticos que simulam cenários do mercado de trabalho.""")
