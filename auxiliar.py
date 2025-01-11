import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import base64

tecnologias = {
    "Python": {
        "link_doc": "https://www.python.org",
        "logo": "imagens/logo_python.png"
    },
    "Power BI": {
        "link_doc": "https://learn.microsoft.com/pt-br/power-bi/fundamentals/",
        "logo": "imagens/logo_powerbi.png"
    },
    "Excel": {
        "link_doc": "https://www.microsoft.com/pt-br/microsoft-365/excel",
        "logo": "imagens/logo_excel.png"
    },
    "SQL": {
        "link_doc": "https://learn.microsoft.com/pt-br/sql/sql-server/",
        "logo": "imagens/logo_sql.png"
    },
    "Git": {
        "link_doc": "https://git-scm.com/",
        "logo": "imagens/logo_git.png"
    },
    "Pandas": {
        "link_doc": "https://pandas.pydata.org/",
        "logo": "imagens/logo_pandas.png"
    },
    "NumPy": {
        "link_doc": "https://numpy.org/",
        "logo": "imagens/logo_numpy.png"
    },
    "Matplotlib": {
        "link_doc": "https://matplotlib.org/",
        "logo": "imagens/logo_matplotlib.png"
    },
    "Seaborn": {
        "link_doc": "https://seaborn.pydata.org/",
        "logo": "imagens/logo_seaborn.png"
    },
    "Plotly": {
        "link_doc": "https://plotly.com/",
        "logo": "imagens/logo_plotly.png"
    },
    "Streamlit": {
        "link_doc": "https://streamlit.io/",
        "logo": "imagens/logo_streamlit.png"
    },
    "Scikit-learn": {
        "link_doc": "https://scikit-learn.org/",
        "logo": "imagens/logo_sklearn.png"
    },
    "Selenium": {
        "link_doc": "https://www.selenium.dev/documentation/",
        "logo": "imagens/logo_selenium.png"
    },
    "Tkinter": {
        "link_doc": "https://docs.python.org/3/library/tkinter.html",
        "logo": "imagens/logo_tkinter.png"
    },
    "Geneticalgorithm": {
        "link_doc": "https://pypi.org/project/geneticalgorithm/",
        "logo": "imagens/logo_geneticalgorithm.png"
    },
    "Kivy": {
        "link_doc": "https://kivy.org/doc/stable/",
        "logo": "imagens/logo_kivy.png"
    },
    "Figma": {
        "link_doc": "https://www.figma.com/pt-br/",
        "logo": "imagens/logo_figma.png"
    },
    "Proxlight": {
        "link_doc": "https://github.com/Proxlight/Proxlight-Designer",
        "logo": "imagens/logo_proxlight.png"
    },
    "SMTP": {
        "link_doc": "https://docs.python.org/3/library/smtplib.html",
        "logo": "imagens/logo_smtp.png"
    },
    "ReportLab": {
        "link_doc": "https://docs.reportlab.com/demos/hello_world/hello_world/",
        "logo": "imagens/logo_reportlab.png"
    },
    "SQLAlchemy": {
        "link_doc": "https://www.sqlalchemy.org/",
        "logo": "imagens/logo_sqlalchemy.png"
    }
}

livros = {
    "Storytelling": {
        "nome": "Storytelling com Dados",
        "autor (a)": "Cole Nussbaumer Knaflic",
        "imagem": "imagens/livro_storytelling.jpg"
    },
    "Python Dados": {
        "nome": "Python para Análise de Dados",
        "autor (a)": "Wes McKinney",
        "imagem": "imagens/livro_python_dados.jpg"
    },
    "Data Science": {
        "nome": "Data Science do Zero",
        "autor (a)": "Joel Grus",
        "imagem": "imagens/livro_data_science.jpg"
    }
}

imagem_temp_projetos = "imagens/imagem_projetos_temp.png"


def adicionar_habilidade(habilidade, coluna, largura):
    coluna.markdown(
        f"""<a href="{habilidade['link_doc']}">
        <img src="data:image/png;base64,{base64.b64encode(open(habilidade['logo'], "rb").read()).decode()}" width="{largura}" style="margin-bottom: 50px;">
        </a>""",
        unsafe_allow_html=True)

def adicionar_tecnologia(tecnologia, descricao, largura_img, coluna):
    with coluna:
        st.markdown(
            f"""<a href="{tecnologia['link_doc']}">
            <img src="data:image/png;base64,{base64.b64encode(open(tecnologia['logo'], "rb").read()).decode()}" width="{largura_img}">
            </a>""",
            unsafe_allow_html=True)
        st.write(descricao)
        st.write("")

def adicionar_certificado(certificado, duracao, data_inicio, data_conclusao, resumo):
    nome_certificado = certificado[certificado.find("/")+1:certificado.find(".")]
    st.subheader(nome_certificado)
    col1, col2, col3 = st.columns([0.5, 1, 1])
    col1.write(f" ⏱ {duracao}")
    col2.write(f"Iniciado em: {data_inicio}")
    col3.write(f"Concluído em: {data_conclusao}")
    st.write(resumo)
    pdf_viewer(rf"certificados/{certificado}", width=725, height=500, resolution_boost=1.4)
    st.divider()

def adicionar_livro(livro, feedback):
    col1, col2 = st.columns([0.5, 1])
    col1.image(livro['imagem'], width=350)
    col2.subheader(livro['nome'])
    col2.write(f"Por: {livro['autor (a)']}")
    col2.write(feedback)
    st.divider()

def voltar_para_projetos():
    if st.button("Voltar", type='tertiary', icon="↩"):
        st.switch_page("Projetos.py")

def adicionar_video(video_projeto):
    video = open(f"projetos/videos/{video_projeto}", "rb")
    video_bytes = video.read()
    st.video(video_bytes, muted=True, loop=True)
