import streamlit as st
import base64

st.set_page_config(page_title="Portfólio", layout='wide')
st.title("Olá, me chamo Giovani 👋🏻")
col1, col2 = st.columns([0.1, 1])
with col1:
    st.image("imagens/giovani.jpeg", width=150)
    c1, c2, c3 = st.columns(3)
    c1.markdown(
        """<a href="https://www.linkedin.com/in/giovani-bruno-dos-santos-costa/">
        <img src="data:image/png;base64,{}" width="50">
        </a>""".format(
            base64.b64encode(open("imagens/logo_linkedin.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True
    )
    c2.markdown(
        """<a href="https://github.com/giovani-bruno">
        <img src="data:image/png;base64,{}" width="50">
        </a>""".format(
            base64.b64encode(open("imagens/logo_github.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True

    )
    c3.markdown(
        """<a href="https://www.instagram.com/giovanibrn_/">
        <img src="data:image/png;base64,{}" width="50">
        </a>""".format(
            base64.b64encode(open("imagens/logo_instagram.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True
    )
with col2:
    st.write("""
    Sou estudante de Ciência da Computação e apaixonado por transformar dados em soluções práticas.
             """)
st.divider()

st.subheader("⚒️ Habilidades")
col1, col2, col3, col4 = st.columns(4)
col1.image("imagens/logo_python.png", width=150)
col2.image("imagens/logo_powerbi.png", width=50)
col3.image("imagens/logo_excel.png", width=50)
col4.image("imagens/logo_git.png", width=50)
col1.image("imagens/logo_sql.png", width=50)
col2.image("imagens/logo_pandas.png", width=150)
col3.image("imagens/logo_numpy.png", width=150)
col4.image("imagens/logo_matplotlib.png", width=150)
col1.image("imagens/logo_seaborn.png", width=150)
col2.image("imagens/logo_plotly.png", width=100)
col3.image("imagens/logo_streamlit.png", width=150)
col4.image("imagens/logo_sklearn.png", width=100)