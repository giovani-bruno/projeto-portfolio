import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import base64
from os import listdir

tecnologias = {
    "Python": {
        "link_doc": "https://www.python.org",
        "logo": "imagens/logos/python.png"
    },
    "Power BI": {
        "link_doc": "https://learn.microsoft.com/pt-br/power-bi/fundamentals/",
        "logo": "imagens/logos/powerbi.png"
    },
    "Excel": {
        "link_doc": "https://www.microsoft.com/pt-br/microsoft-365/excel",
        "logo": "imagens/logos/excel.png"
    },
    "SQL": {
        "link_doc": "https://learn.microsoft.com/pt-br/sql/sql-server/",
        "logo": "imagens/logos/sql_server.png"
    },
    "Git": {
        "link_doc": "https://git-scm.com/",
        "logo": "imagens/logos/git.png"
    },
    "Pandas": {
        "link_doc": "https://pandas.pydata.org/",
        "logo": "imagens/logos/pandas.png"
    },
    "NumPy": {
        "link_doc": "https://numpy.org/",
        "logo": "imagens/logos/numpy.png"
    },
    "Matplotlib": {
        "link_doc": "https://matplotlib.org/",
        "logo": "imagens/logos/matplotlib.png"
    },
    "Seaborn": {
        "link_doc": "https://seaborn.pydata.org/",
        "logo": "imagens/logos/seaborn.png"
    },
    "Plotly": {
        "link_doc": "https://plotly.com/",
        "logo": "imagens/logos/plotly.png"
    },
    "Streamlit": {
        "link_doc": "https://streamlit.io/",
        "logo": "imagens/logos/streamlit.png"
    },
    "Scikit-learn": {
        "link_doc": "https://scikit-learn.org/",
        "logo": "imagens/logos/sklearn.png"
    },
    "Selenium": {
        "link_doc": "https://www.selenium.dev/documentation/",
        "logo": "imagens/logos/selenium.png"
    },
    "Tkinter": {
        "link_doc": "https://docs.python.org/3/library/tkinter.html",
        "logo": "imagens/logos/tkinter.png"
    },
    "Geneticalgorithm": {
        "link_doc": "https://pypi.org/project/geneticalgorithm/",
        "logo": "imagens/logos/geneticalgorithm.png"
    },
    "Kivy": {
        "link_doc": "https://kivy.org/doc/stable/",
        "logo": "imagens/logos/kivy.png"
    },
    "Figma": {
        "link_doc": "https://www.figma.com/pt-br/",
        "logo": "imagens/logos/figma.png"
    },
    "Proxlight": {
        "link_doc": "https://github.com/Proxlight/Proxlight-Designer",
        "logo": "imagens/logos/proxlight.png"
    },
    "SMTP": {
        "link_doc": "https://docs.python.org/3/library/smtplib.html",
        "logo": "imagens/logos/smtp.png"
    },
    "ReportLab": {
        "link_doc": "https://docs.reportlab.com/demos/hello_world/hello_world/",
        "logo": "imagens/logos/reportlab.png"
    },
    "SQLAlchemy": {
        "link_doc": "https://www.sqlalchemy.org/",
        "logo": "imagens/logos/sqlalchemy.png"
    },
    "AWS": {
        "link_doc": "https://docs.aws.amazon.com/pt_br/",
        "logo": "imagens/logos/aws.png"
    },
    "String": {
        "link_doc": "https://docs.python.org/pt-br/3.13/library/string.html",
        "logo": "imagens/logos/string.png"
    },
    "Random": {
        "link_doc": "https://docs.python.org/pt-br/3/library/random.html",
        "logo": "imagens/logos/random.png"
    }
}

livros = {
    "Storytelling": {
        "nome": "Storytelling com Dados",
        "autor (a)": "Cole Nussbaumer Knaflic",
        "imagem": "imagens/livros/livro_storytelling.jpg"
    },
    "Python Dados": {
        "nome": "Python para Análise de Dados",
        "autor (a)": "Wes McKinney",
        "imagem": "imagens/livros/livro_python_dados.jpg"
    },
    "Data Science": {
        "nome": "Data Science do Zero",
        "autor (a)": "Joel Grus",
        "imagem": "imagens/livros/livro_data_science.jpg"
    }
}

def adicionar_habilidade(habilidade, coluna, largura):
    coluna.markdown(
        f"""<a href="{habilidade['link_doc']}">
        <img src="data:image/png;base64,{base64.b64encode(open(habilidade['logo'], "rb").read()).decode()}" width="{largura}" style="margin-bottom: 50px;">
        </a>""",
        unsafe_allow_html=True)

def adicionar_tecnologia(tecnologia, descricao, largura_img, coluna):
    coluna.markdown(
        f"""<a href="{tecnologia['link_doc']}">
        <img src="data:image/png;base64,{base64.b64encode(open(tecnologia['logo'], "rb").read()).decode()}" width="{largura_img}">
        </a>""",
        unsafe_allow_html=True)
    coluna.write(descricao)
    coluna.write("")

def adicionar_certificado(certificado, duracao, data_inicio, data_conclusao, feedback):
    assert certificado + ".pdf" in listdir("certificados"), f"Certificado '{certificado}' não registrado."
    
    st.subheader(certificado)
    col1, col2, col3 = st.columns([0.5, 1, 1])
    col1.write(f" ⏱ {duracao}")
    col2.write(f"Iniciado em: {data_inicio}")
    col3.write(f"Concluído em: {data_conclusao}")
    st.write(feedback)
    pdf_viewer(f"certificados/{certificado}.pdf", width=725, height=500, resolution_boost=1.4)
    st.divider()

def adicionar_livro(livro, feedback):
    col1, col2 = st.columns([0.5, 1])
    col1.image(livro['imagem'], width=350)
    col2.subheader(livro['nome'])
    col2.write(f"Por: {livro['autor (a)']}")
    col2.write(feedback)
    st.divider()

def adicionar_projeto(nome, imagem, link_pagina, coluna):
    assert imagem in listdir("imagens/projetos"), f"Imagem '{imagem}' não existe em imagens/projetos"
    assert link_pagina in listdir("projetos"), f"O arquivo '{link_pagina}' para a página do projeto não existe."

    with coluna.container(border=True):
        st.write(f"##### {nome}")
        st.image(f"imagens/projetos/{imagem}")
        st.write("")
        _, c2, = st.columns([0.6, 1])
        if c2.button("Ver Projeto", key=nome):
            st.switch_page(f"projetos/{link_pagina}")

def voltar_para_projetos():
    if st.button("Voltar", type='tertiary', icon="↩"):
        st.switch_page("Projetos.py")

def adicionar_video(video_projeto):
    assert video_projeto in listdir("projetos/videos"), f"O video '{video_projeto}' não existe em projetos/videos"

    video = open(f"projetos/videos/{video_projeto}", "rb")
    video_bytes = video.read()
    st.video(video_bytes, muted=True, loop=True)
