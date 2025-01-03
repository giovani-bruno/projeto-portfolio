import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(page_title="Certificados", layout='centered')
st.title("Certificados")
st.write("#### Nesta página você encontra todos os meus certificados conquistados até o momento.")
st.divider()

def adicionar_certificado(certificado, duracao, data_inicio, data_conclusao, resumo=None):
    nome_certificado = certificado[certificado.find("/")+1:certificado.find(".")]
    st.subheader(nome_certificado)
    col1, col2, col3 = st.columns([0.5, 1, 1])
    col1.write(f" ⏱ {duracao}")
    col2.write(f"Iniciado em: {data_inicio}")
    col3.write(f"Concluído em: {data_conclusao}")
    st.write(resumo)
    pdf_viewer(certificado, width=725, height=500, resolution_boost=1.4)
    st.divider()

adicionar_certificado(r"certificados/Power BI Impressionador.pdf", "118h", "20/11/2024", "02/01/2025", 
                      """Desenvolvi habilidades para criar dashboards dinâmicos e 
                      visualizações impactantes, dominando o tratamento de dados no 
                      Power Query e fórmulas DAX, das mais básicas até as mais avançadas.""")

adicionar_certificado(r"certificados/Amazon AWS Certified Cloud Practitioner CLF-C02.pdf", "16h", "08/11/2024", "16/11/2024",
                      """Sou uma pessoa fascinada pela computação em nuvem e 
                      em como ela inova o jeito de operar das empresas. 
                      Aprendi como começar na AWS com este curso que me 
                      prepara para a prova de certificação "AWS Cloud Practitioner", 
                      que testa conhecimentos básicos sobre os serviços da AWS.""")

adicionar_certificado(r"certificados/SQL Impressionador.pdf", "90h", "26/09/2024", "24/10/2024",
                      """Aprendi a usar SQL para explorar, manipular e 
                      consultar bancos de dados com eficiência. 
                      O curso abordou desde conceitos básicos, 
                      como seleções e filtros, até técnicas avançadas 
                      para transformar dados em insights valiosos, 
                      essenciais para análises e tomadas de decisão.""")
adicionar_certificado(r"certificados/Inteligência Artificial Impressionador.pdf", "55h", "06/09/2024", "23/09/2024", 
                      """Descobri como integrar ferramentas de inteligência artificial, 
                      como ChatGPT, Gemini e Copilot, no dia a dia profissional, 
                      aumentando a produtividade e aplicando a tecnologia em 
                      diferentes áreas.""")

adicionar_certificado(r"certificados/Python Impressionador.pdf", "124h", "07/03/2024", "10/07/2024",
                      """Dominei os fundamentos e conhecimentos avançados de Python, 
                      explorando estruturas de dados, bibliotecas populares, 
                      e desenvolvendo diversos projetos práticos que simulam cenários do mercado de trabalho.""")
