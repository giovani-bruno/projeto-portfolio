import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(page_title="Certificados", layout='centered')
st.title("Certificados")
st.write("#### Nesta página você encontra todos os meus certificados conquistados até o momento.")
st.divider()

def adicionar_certificado(certificado):
    nome_certificado = certificado[certificado.find("/")+1:certificado.find(".")]
    st.subheader(nome_certificado)
    pdf_viewer(certificado, width=725, height=500, resolution_boost=1.4)
    st.divider()

adicionar_certificado(r"certificados/Python Impressionador.pdf")
adicionar_certificado(r"certificados/Inteligência Artificial Impressionador.pdf")
adicionar_certificado(r"certificados/SQL Impressionador.pdf")
adicionar_certificado(r"certificados/Amazon AWS Certified Cloud Practitioner CLF-C02.pdf")
