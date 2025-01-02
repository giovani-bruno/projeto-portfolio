import base64
import streamlit as st

st.set_page_config(page_title="Portfólio", layout='wide')
st.title("Olá, me chamo Giovani 👋🏻")
st.subheader("Estudante de Ciência da Computação | Entusiasta na área de Ciência de Dados")
st.image("imagens/perfil_linkedin.png")
st.write("""
Sou estudante de Ciência da Computação e apaixonado por transformar dados em soluções práticas.  
Atualmente, desenvolvo projetos voltados para análise e visualização de dados, automação de processos e otimização utilizando Python e ferramentas como pandas, Streamlit, Power BI e SQL.  
Meu objetivo é construir uma carreira sólida em ciência de dados, combinando habilidades técnicas com uma visão estratégica. Sempre busco aprender e crescer, enfrentando desafios com entusiasmo e criatividade.  
""")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        """<a href="https://www.instagram.com/giovanibrn_/">
        <img src="data:image/png;base64,{}" width="50">
        </a>""".format(
            base64.b64encode(open("imagens/logo_instagram.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )


with col2:
    st.markdown(
        """<a href="https://www.linkedin.com/in/giovani-bruno-dos-santos-costa/">
        <img src="data:image/png;base64,{}" width="50">
        </a>""".format(
            base64.b64encode(open("imagens/logo_linkedin.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )