import streamlit as st
from utils import adicionar_certificado, destacar_borda
from main import barra_navegacao

st.set_page_config(page_title="Certificados", layout='wide', page_icon='📃')
barra_navegacao()

st.title("Certificados")
st.write("#### Nesta página você encontra todos os meus certificados conquistados até o momento.")
st.divider()
            
certificados = [
    {
        "certificado": "IBM Data Science Professional Certificate",
        "feedback": """Este foi um programa intensivo com foco em preparar profissionais para atuarem na área de ciência de dados. Ao longo de três meses, 
        mergulhei em doze cursos completos, que cobriram desde os fundamentos da área até a aplicação prática de técnicas de machine learning.
        Durante essa jornada, desenvolvi habilidades sólidas em Python, SQL, análise exploratória, visualização de dados e aprendizado de máquina, utilizando 
        bibliotecas como Pandas, NumPy, Matplotlib, Seaborn e Scikit-learn. Também trabalhei com Jupyter Notebooks e explorei ferramentas do ecossistema de 
        ciência de dados, como Watson Studio e IBM Cloud. Além dos conhecimentos técnicos, aprendi a aplicar a metodologia de ciência de dados, organizar 
        projetos de forma estruturada e comunicar resultados com clareza. Finalizei o programa com um projeto prático completo e uma preparação voltada para 
        entrevistas e construção de portfólio, fortalecendo meu posicionamento profissional na área.""",
        "instituicao": "IBM",
        "duracao": "176h",
        "data_inicio": "07/03/2025",
        "data_conclusao": "07/06/2025",
        "link": "https://www.coursera.org/account/accomplishments/professional-cert/GA234IWIQR5H",
        "nome_alt": "Data Science Professional Certificate"
    },
    {
        "certificado": "Data Scientist Career Guide and Interview",
        "feedback": """Este curso é voltado à preparação para o mercado de trabalho na área de ciência de dados. Nele, aprendi a montar um portfólio estruturado com 
        projetos relevantes, construir um currículo direcionado para vagas na área e desenvolver um pitch pessoal que comunica de forma clara minhas habilidades e objetivos. 
        O curso também abordou estratégias de networking, formas eficazes de se apresentar no LinkedIn e como se preparar para diferentes tipos de entrevistas, técnicas, 
        comportamentais e baseadas em casos de negócio. Foi uma etapa importante para fortalecer minha apresentação profissional e alinhar meu perfil às exigências do mercado de dados.
        Este foi o último curso da Certificação Profissional em Ciência de Dados da IBM.""",
        "instituicao": "IBM",
        "duracao": "9h",
        "data_inicio": "29/05/2025",
        "data_conclusao": "06/06/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/JLVDVA6TLXLZ",
    },
    {
        "certificado": "Generative AI Elevate Your Data Science Career",
        "feedback": """Durante este curso, aprendi a aplicar inteligência artificial generativa em fluxos de trabalho de ciência de dados, utilizando LLMs para explorar, 
        transformar e enriquecer dados. Através de laboratórios práticos, desenvolvi habilidades em engenharia de atributos, aumento de dados e automação de tarefas analíticas, 
        utilizando ferramentas como ChatGPT, CTGAN, Tomat.ai, Column.ai e mais para otimizar processos de análise, visualização e modelagem de dados.""",
        "instituicao": "IBM",
        "duracao": "13h",
        "data_inicio": "20/05/2025",
        "data_conclusao": "28/05/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/BZGD2GJCPXOX",
        "nome_alt": "Generative AI: Elevate Your Data Science Career"
    },
    {
        "certificado": "Applied Data Science Capstone",
        "feedback": """Neste projeto final da Certificação Profissional em Ciência de Dados da IBM, apliquei na prática todas as etapas do ciclo de ciência de dados. 
                      Utilizei APIs e técnicas de web scraping para coletar dados reais sobre lançamentos da SpaceX, realizando o tratamento, análise exploratória, 
                      visualizações interativas e desenvolvimento de modelos de machine learning. O objetivo foi prever o sucesso do pouso do primeiro estágio do foguete Falcon 9.""",
        "instituicao": "IBM",
        "duracao": "13h",
        "data_inicio": "16/05/2025",
        "data_conclusao": "19/05/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/NV35R36ZD30G",
    },
    {
        "certificado": "Machine Learning with Python",
        "feedback": """Durante este curso, aprofundei meus conhecimentos em técnicas essenciais de aprendizado de máquina, como classificação, 
                      regressão e clustering, aplicando algoritmos supervisionados e não supervisionados. Por meio de laboratórios práticos e um 
                      projeto final com dados reais, desenvolvi, avaliei e validei modelos utilizando Python e bibliotecas amplamente usadas, como Pandas, NumPy e Scikit-learn.""",
        "instituicao": "IBM",
        "duracao": "20h",
        "data_inicio": "02/05/2025",
        "data_conclusao": "15/05/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/W27EZSO83EB7"
    },
    {
        "certificado": "Data Visualization with Python",
        "feedback": """Neste curso, aprendi a criar visualizações eficazes e informativas utilizando as principais bibliotecas do Python. 
                      Dominei o uso de Matplotlib e Seaborn para construir gráficos estáticos como linhas, barras, histogramas e mapas de calor. 
                      Também explorei o uso do Folium para criar mapas interativos com dados geoespaciais, além de aprender mais sobre o Dash e Plotly para 
                      visualizações dinâmicas e interativas.""",
        "instituicao": "IBM",
        "duracao": "20h",
        "data_inicio": "19/04/2025",
        "data_conclusao": "01/05/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/ZCQD73OY1BP5"
    },
    {
        "certificado": "Data Analysis with Python",
        "feedback": """Este curso abordou sobre análise de dados utilizando Python, com ênfase em bibliotecas como Pandas, 
                      NumPy, Matplotlib e Seaborn. Aprendi a manipular e limpar dados, realizar análises estatísticas descritivas, 
                      além de criar visualizações gráficas para identificar padrões. Também desenvolvi e avaliei modelos preditivos 
                      como regressão linear, utilizando o scikit-learn.""",
        "instituicao": "IBM",
        "duracao": "15h",
        "data_inicio": "13/04/2025",
        "data_conclusao": "18/04/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/ABTQER23AJ6U"
    },
    {
        "certificado": "Databases and SQL for Data Science with Python",
        "feedback": """Reforcei minhas habilidades em manipulação e consulta de dados utilizando SQL, incluindo filtros, ordenações, 
                      agregações, subqueries e junções entre tabelas. Aprendi a criar e modificar estruturas de banco de dados, 
                      além de integrar SQL com Python por meio de bibliotecas como sqlite3 e ibm_db.""",
        "instituicao": "IBM",
        "duracao": "20h",
        "data_inicio": "02/04/2025",
        "data_conclusao": "12/04/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/ZFZZDKAW9XCW"
    },
    {
        "certificado": "Generative AI Introduction and Applications",
        "feedback": """Este curso abordou os fundamentos da Inteligência Artificial Generativa, entendendo seu funcionamento, 
                      evolução e aplicações práticas. Aprofundei meus conhecimentos em modelos como ChatGPT, DALL·E e Stable Diffusion, 
                      além de compreender como a IA generativa está transformando áreas como criação de conteúdo, desenvolvimento de código, design e análise de dados.""",
        "instituicao": "IBM",
        "duracao": "7h",
        "data_inicio": "06/04/2025",
        "data_conclusao": "08/04/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/CIR3DZK3VBVB",
        "nome_alt": "Generative AI: Introduction and Applications"
    },
    {
        "certificado": "Python Project for Data Science",
        "feedback": """Este curso prático reforçou minhas habilidades em manipulação e análise de dados utilizando Python.
                      Desenvolvi um projeto aplicando técnicas como extração de dados, web scraping, limpeza, visualização e 
                      criação de dashboards interativos. Utilizei bibliotecas como Pandas, Beautiful Soup e Plotly para transformar 
                      dados brutos em insights visuais. O curso consolidou meu conhecimento em programação para ciência de dados, 
                      permitindo-me construir soluções eficientes e baseadas em dados.""",
        "instituicao": "IBM",
        "duracao": "8h",
        "data_inicio": "31/03/2025",
        "data_conclusao": "01/04/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/SU2O9WXO0UPF"
    },
    {
        "certificado": "Python for Data Science, AI & Development",
        "feedback": """Durante este curso, desenvolvi habilidades em manipulação de dados com pandas e NumPy, 
                      criação de visualizações com matplotlib, e automação de tarefas com estruturas de controle e funções. 
                      Também aprendi a trabalhar com arquivos CSV e JSON, além de interagir com APIs. O curso me proporcionou 
                      uma base sólida para aplicar Python em análise de dados e desenvolvimento de soluções.""",
        "instituicao": "IBM",
        "duracao": "25h",
        "data_inicio": "21/03/2025",
        "data_conclusao": "28/03/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/3MBT50T8LQ5M"
    },
    {
        "certificado": "Data Science Methodology",
        "feedback": """Aprendi sobre as principais etapas da metodologia de ciência de dados, incluindo a formulação do 
                      problema, coleta e compreensão dos dados, preparação para modelagem, construção e avaliação de modelos. 
                      O curso abordou o processo CRISP-DM e explorou diferentes tipos de modelos analíticos, como preditivos, 
                      descritivos e de classificação.""",
        "instituicao": "IBM",
        "duracao": "6h",
        "data_inicio": "18/03/2025",
        "data_conclusao": "20/03/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/0VDFAH1MRLEK"
    },
    {
        "certificado": "Tools for Data Science",
        "feedback": """Explorei as principais linguagens, bibliotecas e ferramentas usadas por cientistas de dados, 
                      incluindo Jupyter Notebooks, RStudio IDE e IBM Watson Studio. 
                      Aprendi suas funcionalidades, e como aplicá-las em 
                      projetos práticos de data science.""",
        "instituicao": "IBM",
        "duracao": "18h",
        "data_inicio": "13/03/2025",
        "data_conclusao": "18/03/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/UPR3W5F0NXR8"
    },
    {
        "certificado": "What is Data Science",
        "feedback": """Desenvolvi uma compreensão sólida sobre os fundamentos da ciência de dados, 
                      explorando o papel do cientista de dados, o ciclo de vida de um projeto, a importância da 
                      ética na análise de dados e como transformar dados em insights acionáveis para a tomada de decisões.
                      Este é o primeiro curso do programa de Certificação Profissional em Ciência de Dados da IBM.""",
        "instituicao": "IBM",
        "duracao": "11h",
        "data_inicio": "08/03/2025",
        "data_conclusao": "12/03/2025",
        "link": "https://www.coursera.org/account/accomplishments/verify/KQ801LVS4B63",
        "nome_alt": "What is Data Science?"
    },
    {
        "certificado": "Python Data Visualization - Dashboards with Plotly & Dash",
        "feedback": """Aprendi a criar dashboards interativos e profissionais utilizando as bibliotecas Dash e Plotly do Python. 
                      O curso abordou desde os conceitos básicos da estrutura de uma aplicação Dash até a construção de dashboards completos, 
                      explorando vários tipos de visualizações.""",
        "instituicao": "Udemy",
        "duracao": "8h",
        "data_inicio": "22/01/2025",
        "data_conclusao": "29/01/2025",
        "link": "https://www.udemy.com/certificate/UC-386dc837-6abf-474d-bb19-badec744ea3e/",
        "nome_alt": "Dashboards with Plotly & Dash"
    },
    {
        "certificado": "Estatística para Ciência de Dados e Machine Learning",
        "feedback": """Aprendi os principais conceitos de estatística e probabilidade aplicados à ciência de dados, 
                       explorando tanto a teoria quanto a prática. O curso abordou tópicos fundamentais como distribuições, 
                       intervalos de confiança, testes de hipóteses, correlações e outros conceitos essenciais para análises de dados e modelos de machine learning. 
                       Gostei muito desse assunto e pretendo me aprofundar ainda mais para ampliar minhas habilidades e conhecimentos na área.""",
        "instituicao": "Udemy",
        "duracao": "20h",
        "data_inicio": "03/01/2025",
        "data_conclusao": "21/01/2025",
        "link": "https://www.udemy.com/certificate/UC-386dc837-6abf-474d-bb19-badec744ea3e/"
    },
    {
        "certificado": "Power BI Impressionador",
        "feedback": """Desenvolvi habilidades para criar dashboards dinâmicos e 
                      visualizações impactantes, dominando o tratamento de dados no 
                      Power Query e fórmulas DAX, das mais básicas até as mais avançadas.""",
        "instituicao": "Hashtag Treinamentos",
        "duracao": "118h",
        "data_inicio": "20/11/2024",
        "data_conclusao": "02/01/2025",
        "link": "https://portalhashtag.com/certificado-hashtag/1735855635461x656910295180706200"
    },
    {
        "certificado": "Análise de Dados Impressionadora",
        "feedback": """Um curso abrangente que me prepara para atuar como analista de dados, 
                      abordando as principais ferramentas do mercado. Aprendi a organizar e tratar dados no Excel, 
                      criar dashboards interativos no Power BI, realizar consultas avançadas em SQL, 
                      automatizar análises com Python e aplicar inteligência artificial para obter insights. 
                      Esse conhecimento integrado me permite transformar dados em decisões estratégicas com confiança.""",
        "instituicao": "Hashtag Treinamentos",
        "duracao": "104h",
        "data_inicio": "06/07/2024",
        "data_conclusao": "20/12/2024",
        "link": "https://portalhashtag.com/certificado-hashtag/1734734018653x311705561269689300"
    },
    {
        "certificado": "Amazon AWS Certified Cloud Practitioner CLF-C02",
        "feedback": """Sou uma pessoa fascinada pela computação em nuvem e 
                      em como ela inova o jeito de operar das empresas. 
                      Aprendi como começar na AWS com este curso que me 
                      prepara para a prova de certificação "AWS Cloud Practitioner", 
                      que testa conhecimentos básicos sobre os serviços da AWS.""",
        "instituicao": "Udemy",
        "duracao": "16h",
        "data_inicio": "08/11/2024",
        "data_conclusao": "16/11/2024",
        "link": "https://www.udemy.com/certificate/UC-e7cbf408-3ce1-475e-8d0d-6c28f22af890/"
    },
    {
        "certificado": "SQL Impressionador",
        "feedback": """Aprendi a usar SQL para explorar, manipular e 
                      consultar bancos de dados com eficiência. 
                      O curso abordou desde conceitos básicos, 
                      como seleções e filtros, até técnicas avançadas 
                      para transformar dados em insights valiosos, 
                      essenciais para análises e tomadas de decisão.""",
        "instituicao": "Hashtag Treinamentos",
        "duracao": "90h",
        "data_inicio": "26/09/2024",
        "data_conclusao": "24/10/2024",
        "link": "https://portalhashtag.com/certificado-hashtag/1729815109682x128591154351954670"
    },
    {
        "certificado": "Inteligência Artificial Impressionador",
        "feedback": """Descobri como integrar ferramentas de inteligência artificial, 
                      como ChatGPT, Gemini e Copilot, no dia a dia profissional, 
                      aumentando a produtividade e aplicando a tecnologia em 
                      diferentes áreas.""",
        "instituicao": "Hashtag Treinamentos",
        "duracao": "55h",
        "data_inicio": "06/09/2024",
        "data_conclusao": "23/09/2024",
        "link": "https://portalhashtag.com/certificado-hashtag/1727136499725x970644437596501800"
    },
    {
        "certificado": "Python Impressionador",
        "feedback": """Dominei os fundamentos e conhecimentos avançados de Python, 
                      explorando estruturas de dados, bibliotecas populares, 
                      e desenvolvendo diversos projetos práticos que simulam cenários do mercado de trabalho.""",
        "instituicao": "Hashtag Treinamentos",
        "duracao": "124h",
        "data_inicio": "07/03/2024",
        "data_conclusao": "10/07/2024",
        "link": "https://portalhashtag.com/certificado-hashtag/1720653179754x576211738342195200"
    }
]

colunas = st.columns(3)
for i, cert in enumerate(certificados):
    coluna = colunas[i % 3]
    adicionar_certificado(
        certificado=cert["certificado"],
        feedback=cert["feedback"],
        instituicao=cert["instituicao"],
        duracao=cert["duracao"],
        data_inicio=cert["data_inicio"],
        data_conclusao=cert["data_conclusao"],
        link=cert["link"],
        coluna=coluna,
        key=i,
        nome_alt=cert.get("nome_alt"),
    )

    if cert.get("destaque"):
        destacar_borda(i)
    else:
        st.html(f"""
            <style>               
                .st-key-{i} {{
                    border: 1px solid rgba(250, 250, 250, 0.2);
                    border-radius: 0.75rem;
                    padding: 1rem;
                }}
            </style>
        """)
