import streamlit as st
from utils import adicionar_certificado
from main import barra_navegacao

st.set_page_config(page_title="Certificados", layout='wide', page_icon='📃')
barra_navegacao()

st.title("Certificados")
st.write("#### Nesta página você encontra todos os meus certificados conquistados até o momento.")
st.divider()
            
col1, col2, col3 = st.columns(3)

adicionar_certificado("Generative AI - Introduction and Applications",
                      """Nesse curso, foi abordado os fundamentos da Inteligência Artificial Generativa, 
                      seu funcionamento, evolução e aplicações práticas. Aprofundei meus conhecimentos 
                      em modelos como ChatGPT, DALL·E e Stable Diffusion, além de compreender como a 
                      IA generativa está transformando áreas como criação de conteúdo, desenvolvimento 
                      de código, design e análise de dados.""",
                      "IBM", "7h", "06/04/2025", "08/04/2025",
                      "https://www.coursera.org/account/accomplishments/verify/CIR3DZK3VBVB", col1,
                      nome_alt="Generative AI: Introduction and Applications")

adicionar_certificado("Python Project for Data Science", 
                      """Este curso prático reforçou minhas habilidades em manipulação e análise de dados utilizando Python.
                      Desenvolvi um projeto aplicando técnicas como extração de dados, web scraping, limpeza, visualização e 
                      criação de dashboards interativos. Utilizei bibliotecas como Pandas, Beautiful Soup e Plotly para transformar 
                      dados brutos em insights visuais. O curso consolidou meu conhecimento em programação para ciência de dados, 
                      permitindo-me construir soluções eficientes e baseadas em dados.""",
                      "IBM", "8h", "31/03/2025", "01/04/2025",
                      "https://www.coursera.org/account/accomplishments/verify/SU2O9WXO0UPF", col2)

adicionar_certificado("Python for Data Science, AI & Development",
                      """Durante este curso, desenvolvi habilidades em manipulação de dados com pandas e NumPy, 
                      criação de visualizações com matplotlib, e automação de tarefas com estruturas de controle e funções. 
                      Também aprendi a trabalhar com arquivos CSV e JSON, além de interagir com APIs. O curso me proporcionou 
                      uma base sólida para aplicar Python em análise de dados e desenvolvimento de soluções.""",
                      "IBM", "25h", "21/03/2025", "28/03/2025",
                      "https://www.coursera.org/account/accomplishments/verify/3MBT50T8LQ5M", col3)

adicionar_certificado("Data Science Methodology", 
                      """Aprendi sobre as principais etapas da metodologia de ciência de dados, incluindo a formulação do 
                      problema, coleta e compreensão dos dados, preparação para modelagem, construção e avaliação de modelos. 
                      O curso abordou o processo CRISP-DM e explorou diferentes tipos de modelos analíticos, como preditivos, 
                      descritivos e de classificação.""",
                      "IBM", "6h", "18/03/2025", "20/03/2025",
                      "https://www.coursera.org/account/accomplishments/verify/0VDFAH1MRLEK", col1)

adicionar_certificado("Tools for Data Science",
                      """Explorei as principais linguagens, bibliotecas e ferramentas usadas por cientistas de dados, 
                      incluindo Jupyter Notebooks, RStudio IDE e IBM Watson Studio. 
                      Aprendi suas funcionalidades, e como aplicá-las em 
                      projetos práticos de data science.""",
                      "IBM", "18h", "13/03/2025", "18/03/2025",
                      "https://www.coursera.org/account/accomplishments/verify/UPR3W5F0NXR8", col2)

adicionar_certificado("What is Data Science", 
                      """Desenvolvi uma compreensão sólida sobre os fundamentos da ciência de dados, 
                      explorando o papel do cientista de dados, o ciclo de vida de um projeto, a importância da 
                      ética na análise de dados e como transformar dados em insights acionáveis para a tomada de decisões.
                      Este é o primeiro curso do programa de Certificação Profissional em Ciência de Dados da IBM.""",
                      "IBM", "11h", "08/03/2025", "12/03/2025",
                      "https://www.coursera.org/account/accomplishments/verify/KQ801LVS4B63", col3,
                      nome_alt="What is Data Science?")

adicionar_certificado("Python Data Visualization - Dashboards with Plotly & Dash", 
                      """Aprendi a criar dashboards interativos e profissionais utilizando as bibliotecas Dash e Plotly do Python. 
                      O curso abordou desde os conceitos básicos da estrutura de uma aplicação Dash até a construção de dashboards completos, 
                      explorando vários tipos de visualizações.""",
                      "Udemy", "8h", "22/01/2025", "29/01/2025",
                      "https://www.udemy.com/certificate/UC-386dc837-6abf-474d-bb19-badec744ea3e/", col1,
                      nome_alt="Dashboards with Plotly & Dash")

adicionar_certificado("Estatística para Ciência de Dados e Machine Learning",
                      """Aprendi os principais conceitos de estatística e probabilidade aplicados à ciência de dados, 
                       explorando tanto a teoria quanto a prática. O curso abordou tópicos fundamentais como distribuições, 
                       intervalos de confiança, testes de hipóteses, correlações e outros conceitos essenciais para análises de dados e modelos de machine learning. 
                       Gostei muito desse assunto e pretendo me aprofundar ainda mais para ampliar minhas habilidades e conhecimentos na área.""",
                       "Udemy", "20h", "03/01/2025", "21/01/2025",
                       "https://www.udemy.com/certificate/UC-386dc837-6abf-474d-bb19-badec744ea3e/", col2)

adicionar_certificado("Power BI Impressionador", 
                      """Desenvolvi habilidades para criar dashboards dinâmicos e 
                      visualizações impactantes, dominando o tratamento de dados no 
                      Power Query e fórmulas DAX, das mais básicas até as mais avançadas.""",
                      "Hashtag Treinamentos", "118h", "20/11/2024", "02/01/2025",
                      "https://portalhashtag.com/certificado-hashtag/1735855635461x656910295180706200", col3)

adicionar_certificado("Análise de Dados Impressionadora",
                      """Um curso abrangente que me prepara para atuar como analista de dados, 
                      abordando as principais ferramentas do mercado. Aprendi a organizar e tratar dados no Excel, 
                      criar dashboards interativos no Power BI, realizar consultas avançadas em SQL, 
                      automatizar análises com Python e aplicar inteligência artificial para obter insights. 
                      Esse conhecimento integrado me permite transformar dados em decisões estratégicas com confiança.""",
                      "Hashtag Treinamentos", "104h", "06/07/2024", "20/12/2024", 
                      "https://portalhashtag.com/certificado-hashtag/1734734018653x311705561269689300", col1)

adicionar_certificado("Amazon AWS Certified Cloud Practitioner CLF-C02", 
                      """Sou uma pessoa fascinada pela computação em nuvem e 
                      em como ela inova o jeito de operar das empresas. 
                      Aprendi como começar na AWS com este curso que me 
                      prepara para a prova de certificação "AWS Cloud Practitioner", 
                      que testa conhecimentos básicos sobre os serviços da AWS.""",
                      "Udemy", "16h", "08/11/2024", "16/11/2024",
                      "https://www.udemy.com/certificate/UC-e7cbf408-3ce1-475e-8d0d-6c28f22af890/", col2)

adicionar_certificado("SQL Impressionador",
                      """Aprendi a usar SQL para explorar, manipular e 
                      consultar bancos de dados com eficiência. 
                      O curso abordou desde conceitos básicos, 
                      como seleções e filtros, até técnicas avançadas 
                      para transformar dados em insights valiosos, 
                      essenciais para análises e tomadas de decisão.""",
                      "Hashtag Treinamentos", "90h", "26/09/2024", "24/10/2024",
                      "https://portalhashtag.com/certificado-hashtag/1729815109682x128591154351954670", col3)

adicionar_certificado("Inteligência Artificial Impressionador",
                      """Descobri como integrar ferramentas de inteligência artificial, 
                      como ChatGPT, Gemini e Copilot, no dia a dia profissional, 
                      aumentando a produtividade e aplicando a tecnologia em 
                      diferentes áreas.""",
                      "Hashtag Treinamentos", "55h", "06/09/2024", "23/09/2024",
                      "https://portalhashtag.com/certificado-hashtag/1727136499725x970644437596501800", col1)

adicionar_certificado("Python Impressionador",
                      """Dominei os fundamentos e conhecimentos avançados de Python, 
                      explorando estruturas de dados, bibliotecas populares, 
                      e desenvolvendo diversos projetos práticos que simulam cenários do mercado de trabalho.""",
                      "Hashtag Treinamentos", "124h", "07/03/2024", "10/07/2024",
                      "https://portalhashtag.com/certificado-hashtag/1720653179754x576211738342195200", col2)
