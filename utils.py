import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import streamlit.components.v1 as components
import base64
from os import listdir
from fitz import open as pymupdf
from PIL import Image
from io import BytesIO

tecnologias = {
    "Python": {
        "link_doc": "https://www.python.org",
        "logo": "imagens/logos/python.png"
    },
    "Power BI": {
        "link_doc": "https://learn.microsoft.com/pt-br/power-bi/fundamentals/",
        "logo": "imagens/logos/power_bi.png"
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
    "Scikit Learn": {
        "link_doc": "https://scikit-learn.org/",
        "logo": "imagens/logos/scikit_learn.png"
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
        "logo": "imagens/logos/smtplib.png"
    },
    "ReportLab": {
        "link_doc": "https://docs.reportlab.com/demos/hello_world/hello_world/",
        "logo": "imagens/logos/reportlab.png"
    },
    "SQLAlchemy": {
        "link_doc": "https://www.sqlalchemy.org/",
        "logo": "imagens/logos/sql_alchemy.png"
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
    },
    "Scipy": {
        "link_doc": "https://docs.scipy.org/doc/scipy-1.15.0/index.html",
        "logo": "imagens/logos/scipy.png"
    },
    "statsmodels": {
        "link_doc": "https://www.statsmodels.org/stable/index.html",
        "logo": "imagens/logos/statsmodels.png"
    },
    "Canva": {
        "link_doc": "https://www.canva.com/",
        "logo": "imagens/logos/canva.png"
    },
    "FormSubmit": {
        "link_doc": "https://formsubmit.co/",
        "logo": "imagens/logos/formsubmit.png"
    },
    "Dash": {
        "link_doc": "https://dash.plotly.com/",
        "logo": "imagens/logos/dash.png"
    },
    "Joblib": {
        "link_doc": "https://joblib.readthedocs.io/en/stable/",
        "logo": "imagens/logos/joblib.png"
    },
    "Groq": {
        "link_doc": "https://groq.com/",
        "logo": "imagens/logos/groq.png"
    },
    "Llama Index": {
        "link_doc": "https://docs.llamaindex.ai/en/stable/",
        "logo": "imagens/logos/llama_index.png"
    },
    "Hugging Face": {
        "link_doc": "https://huggingface.co/",
        "logo": "imagens/logos/hugging_face.png"
    },
    "Tensor Flow": {
        "link_doc": "https://www.tensorflow.org/?hl=pt-br",
        "logo": "imagens/logos/tensor_flow.png"
    },
    "Keras": {
        "link_doc": "https://keras.io/",
        "logo": "imagens/logos/keras.png"
    },
    "Beautiful Soup": {
        "link_doc": "https://beautiful-soup-4.readthedocs.io/en/latest/",
        "logo": "imagens/logos/beautiful_soup.png"
    },
    "N8N": {
        "link_doc": "https://n8n.io/",
        "logo": "imagens/logos/n8n.png"
    },
    "CrewAI": {
        "link_doc": "https://www.crewai.com/",
        "logo": "imagens/logos/crew_ai.png"
    },
}

livros = {
    "Storytelling": {
        "nome": "Storytelling com Dados",
        "autor (a)": "Cole Nussbaumer Knaflic",
        "imagem": "imagens/livros/storytelling_dados.jpg"
    },

    "Python Dados": {
        "nome": "Python para Análise de Dados",
        "autor (a)": "Wes McKinney",
        "imagem": "imagens/livros/python_dados.jpg"
    },

    "Data Science": {
        "nome": "Data Science do Zero",
        "autor (a)": "Joel Grus",
        "imagem": "imagens/livros/data_science.jpg"
    },

    "Hands on ML": {
        "nome": "Mãos à obra: Aprendizado de Máquina com Scikit-Learn, Keras, & TensorFlow",
        "autor (a)": "Aurélien Géron",
        "imagem": "imagens/livros/hands_on_ml.jpg"
    }
}

def carrossel_habilidades(tecnologias, habilidades):
    def gerar_slide(h):
        with open(tecnologias[h]['logo'], "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode()
        return f'''
        <div class="slide">
            <a href="{tecnologias[h]['link_doc']}" target="_blank">
                <img src="data:image/png;base64,{img_base64}" alt="{h}" title="{h}" />
            </a>
        </div>
        '''

    html_code = f"""
    <style>
    .slider {{
        background: #262730;
        box-shadow: 0 10px 20px -5px rgba(0, 0, 0, .125);
        height: 100px;
        margin: 2rem auto;
        overflow: hidden;
        border-radius: 10px;
        position: relative;
        width: 100%;
    }}

    .slider::before,
    .slider::after {{
        content: "";
        height: 100px;
        position: absolute;
        width: 200px;
        z-index: 2;
    }}

    .slider::after {{
        right: 0;
        top: 0;
        transform: rotateZ(180deg);
    }}

    .slider::before {{
        left: 0;
        top: 0;
    }}

    .slide-track {{
        display: flex;
        width: calc((250px + 60px) * {len(habilidades) * 2});
        animation: scroll 80s linear infinite;
    }}

    .slider:hover .slide-track {{
        animation-play-state: paused;
    }}

    @keyframes scroll {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(calc(-250px * {len(habilidades)})); }}
    }}

    .slide {{
        height: 100px;
        min-width: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 30px;
    }}

    .slide img {{
        height: 50px;
        width: auto;
        object-fit: contain;
    }}
    </style>

    <div class="slider">
        <div class="slide-track">
            {''.join(gerar_slide(h) for h in habilidades)}
            {''.join(gerar_slide(h) for h in habilidades)}
        </div>
    </div>
    """

    components.html(html_code, height=150)

def grid_habilidades(tecnologias, habilidades):
    cols = st.columns(4)
    for i, h in enumerate(habilidades):
        with open(tecnologias[h]['logo'], "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode()
        cols[i % 4].markdown(
            f"""<div style='text-align: center; margin-bottom: 70px;'>
                <a href="{tecnologias[h]['link_doc']}" target="_blank">
                    <img src="data:image/png;base64,{img_base64}" alt="{h}" title="{h}" style="height:50px;"><br>
                </a>
            </div>""",
            unsafe_allow_html=True
        )

def adicionar_tecnologia(tecnologia, descricao, largura_img, coluna):
    coluna.html(
        f"""<a href="{tecnologia['link_doc']}" target="_blank">
        <img src="data:image/png;base64,{base64.b64encode(open(tecnologia['logo'], "rb").read()).decode()}" width="{largura_img}">
        </a>""")
    coluna.write(descricao)
    coluna.write("")


def adicionar_certificado(certificado, feedback, instituicao, 
                          duracao, data_inicio, data_conclusao, link, coluna, key, nome_alt=None, destaque=False):
    assert certificado + '.pdf' in listdir("certificados"), f"Certificado não registrado."

    @st.dialog(f"{certificado if not nome_alt else nome_alt} - {instituicao}", width='large')
    def verificar_certificado(): 
        col1, col2, col3 = st.columns([0.5, 1, 1])
        col1.write(f" ⏱ {duracao}")
        col2.write(f"Iniciado em: {data_inicio}")
        col3.write(f"Concluído em: {data_conclusao}")
        st.write(feedback)
        pdf_viewer(f"certificados/{certificado}.pdf", resolution_boost=1.5)
        st.write(f"Verifique em: {link}")

    st.html("""
        <style>
            .stButton > button {
                display: block;
                margin: 0 auto;
            }
            
            .certificado-titulo {
                margin-bottom: 0.5rem;
            }
            
            .stElementContainer {
                display: flex;
                width: 100%;
            }
        </style>
    """)
        
    with coluna.container(key=key):
        titulo = certificado if not nome_alt else nome_alt
        st.markdown(f'<div class="certificado-titulo">{titulo}</div>', unsafe_allow_html=True)
        
        with open(f"certificados/{certificado}.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        certificado_pdf = pymupdf(stream=pdf_bytes, filetype="pdf")
        primeira_pagina = certificado_pdf.load_page(0)
        pix = primeira_pagina.get_pixmap()
        st.image(Image.open(BytesIO(pix.tobytes("png"))).resize((792, 612)))
        
        if st.button("Saiba mais", key=certificado):
            verificar_certificado()
            
def destacar_borda(key):
    st.html(f"""
        <style>
            @keyframes goldenSnake {{
                    0% {{
                        box-shadow: 
                            0 -3px 0 0 #bc8700,
                            2px -2px 0 0 #bc870080,
                            3px 0 0 0 #bc870040,
                            2px 2px 0 0 #bc870020;
                    }}
                    12.5% {{
                        box-shadow: 
                            2px -2px 0 0 #bc8700,
                            3px 0 0 0 #bc870080,
                            2px 2px 0 0 #bc870040,
                            0 3px 0 0 #bc870020;
                    }}
                    25% {{
                        box-shadow: 
                            3px 0 0 0 #bc8700,
                            2px 2px 0 0 #bc870080,
                            0 3px 0 0 #bc870040,
                            -2px 2px 0 0 #bc870020;
                    }}
                    37.5% {{
                        box-shadow: 
                            2px 2px 0 0 #bc8700,
                            0 3px 0 0 #bc870080,
                            -2px 2px 0 0 #bc870040,
                            -3px 0 0 0 #bc870020;
                    }}
                    50% {{
                        box-shadow: 
                            0 3px 0 0 #bc8700,
                            -2px 2px 0 0 #bc870080,
                            -3px 0 0 0 #bc870040,
                            -2px -2px 0 0 #bc870020;
                    }}
                    62.5% {{
                        box-shadow: 
                            -2px 2px 0 0 #bc8700,
                            -3px 0 0 0 #bc870080,
                            -2px -2px 0 0 #bc870040,
                            0 -3px 0 0 #bc870020;
                    }}
                    75% {{
                        box-shadow: 
                            -3px 0 0 0 #bc8700,
                            -2px -2px 0 0 #bc870080,
                            0 -3px 0 0 #bc870040,
                            2px -2px 0 0 #bc870020;
                    }}
                    87.5% {{
                        box-shadow: 
                            -2px -2px 0 0 #bc8700,
                            0 -3px 0 0 #bc870080,
                            2px -2px 0 0 #bc870040,
                            3px 0 0 0 #bc870020;
                    }}
                    100% {{
                        box-shadow: 
                            0 -3px 0 0 #bc8700,
                            2px -2px 0 0 #bc870080,
                            3px 0 0 0 #bc870040,
                            2px 2px 0 0 #bc870020;
                    }}
                }}

        .st-key-{key} {{
                border-radius: 0.75rem;
                padding: 1rem;
                animation: goldenSnake 6s linear infinite;
                background: transparent;
            }}
        </style>
    """)

def adicionar_livro(livro, feedback, frase=None):
    col1, col2 = st.columns([0.5, 1])
    col1.image(livro['imagem'], width=350)
    col2.subheader(livro['nome'])
    col2.markdown(f"📖 *{frase}*")
    col2.write(f"Por: {livro['autor (a)']}")
    col2.write(feedback)
    st.divider()

def adicionar_projeto(projeto, coluna, key):
    assert projeto + '.png' in listdir("imagens/projetos"), f"Imagem '{projeto}.png' não existe em imagens/projetos"
    assert projeto + '.py' in listdir("projetos"), f"O arquivo '{projeto}.py' para a página do projeto não existe."

    st.html("""
        <style>
        .stButton > button {
            display: block;
            margin: 0 auto;
        }
            
        .stElementContainer {
                display: flex;
                width: 100%;
        }
        </style>
    """)

    with coluna.container(key=key):
        st.image(f"imagens/projetos/{projeto}.png")
        if st.button("Ver Projeto", key=projeto):
            st.switch_page(f"projetos/{projeto}.py")

def botao_voltar():
    if st.button("Voltar", type='tertiary', icon="↩"):
        st.switch_page("Projetos.py")

def adicionar_video(video_projeto):
    assert video_projeto in listdir("projetos/videos-imagens"), f"O video '{video_projeto}' não existe em projetos/videos-imagens"

    video = open(f"projetos/videos-imagens/{video_projeto}", "rb")
    video_bytes = video.read()
    st.video(video_bytes, muted=True)

def acessar_repositorio(link):
    st.html(
    f"""<a href="{link}" target="_blank">
    <img src="data:image/png;base64,{base64.b64encode(open("imagens/acessar_repositorio.png", "rb").read()).decode()}" width="200">
    </a>""")

css_formulario = """
    <style>
        .contact-form {
            background-color: #262730;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            margin: 0 auto;
        }

        .contact-form input, .contact-form textarea {
            background-color: #f9f9f9;
            color: #000;
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box;
            font-size: 16px;
        }
        
        .button-container {
            display: flex;
            justify-content: center;
        }

        .contact-form button {
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 400;
            padding: 0.25rem 0.75rem;
            border-radius: 0.5rem;
            min-height: 2.5rem;
            width: 20%;
            cursor: pointer;
            user-select: none;
            background-color: rgb(19, 23, 32);
            border: 1px solid rgba(250, 250, 250, 0.2);
            color: white;
            transition: color 0.2s, border-color 0.2s, background-color 0.2s;
        }

        .contact-form button:hover {
            border-color: #FF4B4B;
            color: #FF4B4B;
        }

        .contact-form button:active {
            background-color: #FF4B4B;
            color: #f9f9f9;
            transform: scale(0.98);
        }

        .contact-form input:focus, .contact-form textarea:focus {
            border-color: #4CAF50;
            color: #000000;
        }

        .form-row {
            display: flex;
            justify-content: space-between;
        }

        .form-row input {
            width: 48%;
        }

        .form-row input:first-child {
            margin-right: 4%;
        }
    </style>
    """
