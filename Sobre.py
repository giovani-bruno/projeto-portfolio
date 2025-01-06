import streamlit as st
import base64

st.set_page_config(page_title="Portfólio", layout='wide')
st.title("Olá, me chamo Giovani 👋🏻")
col1, col2 = st.columns([0.1, 1])
with col1:
    st.image("imagens/giovani.jpeg", width=150)
    c1, c2, c3 = st.columns(3)
    c1.markdown(
        f"""<a href="https://www.linkedin.com/in/giovani-bruno-dos-santos-costa/">
        <img src="data:image/png;base64,{base64.b64encode(open("imagens/logo_linkedin.png", "rb").read()).decode()}" width="50">
        </a>""",
        unsafe_allow_html=True
    )
    c2.markdown(
        f"""<a href="https://github.com/giovani-bruno">
        <img src="data:image/png;base64,{base64.b64encode(open("imagens/logo_github.png", "rb").read()).decode()}" width="50">
        </a>""",
        unsafe_allow_html=True

    )
    c3.markdown(
        f"""<a href="https://www.instagram.com/giovanibrn_/">
        <img src="data:image/png;base64,{base64.b64encode(open("imagens/logo_instagram.png", "rb").read()).decode()}" width="50">
        </a>""",
        unsafe_allow_html=True
    )
with col2:
    st.write("""
    Sou um estudante de Ciência da Computação, atualmente no 5° semestre, com grande interesse em ciência de dados. Concluí cursos de destaque na área de dados, maioria deles pela Hashtag Treinamentos.
Estou constantemente buscando fortalecer minhas habilidades em manipulação de dados, visualização e machine learning, utilizando datasets públicos e projetos próprios. Também procuro aplicar esse conhecimento em automação e otimização de tarefas no ambiente corporativo.
Minha meta é me tornar um cientista de dados e contribuir para soluções que façam a diferença.
             """)
st.divider()

st.subheader("⚒️ Habilidades")
st.write("")
col1, col2, col3, col4 = st.columns(4)
def adicionar_habilidade(logo, link, coluna, largura):
    coluna.markdown(
        f"""<a href="{link}">
        <img src="data:image/png;base64,{base64.b64encode(open(f"imagens/{logo}", "rb").read()).decode()}" width="{largura}" style="margin-bottom: 50px;">
        </a>""",
        unsafe_allow_html=True)
    
adicionar_habilidade("logo_python.png", "https://www.python.org/", col1, 150)
adicionar_habilidade("logo_powerbi.png", "https://learn.microsoft.com/pt-br/power-bi/fundamentals/", col2, 50)
adicionar_habilidade("logo_excel.png", "https://www.microsoft.com/pt-br/microsoft-365/excel", col3, 50)
adicionar_habilidade("logo_sql.png", "https://learn.microsoft.com/pt-br/sql/sql-server/", col4, 50)
adicionar_habilidade("logo_git.png", "https://git-scm.com/", col1, 50)
adicionar_habilidade("logo_pandas.png", "https://pandas.pydata.org/", col2, 150)
adicionar_habilidade("logo_numpy.png", "https://numpy.org/", col3, 150)
adicionar_habilidade("logo_matplotlib.png", "https://matplotlib.org/", col4, 150)
adicionar_habilidade("logo_seaborn.png", "https://seaborn.pydata.org/", col1, 150)
adicionar_habilidade("logo_plotly.png", "https://plotly.com/", col2, 100)
adicionar_habilidade("logo_streamlit.png", "https://streamlit.io/", col3, 150)
adicionar_habilidade("logo_sklearn.png", "https://scikit-learn.org/", col4, 100)

st.subheader("📬 Entre em contato")
st.write("[giovainic@gmail.com](mailto:giovainic@gmail.com)")