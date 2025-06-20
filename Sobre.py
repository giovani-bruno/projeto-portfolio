import streamlit as st
import streamlit.components.v1 as components
import base64
from main import barra_navegacao
from utils import tecnologias, adicionar_habilidade, css_formulario

st.set_page_config(page_title="Sobre", layout='wide')
barra_navegacao()

st.title("Olá, me chamo Giovani 👋🏻")
col1, col2 = st.columns([0.15, 1])
with col1:
    st.image("imagens/giovani.jpeg", width=200)
    c1, c2, c3 = st.columns(3)
    c1.markdown(
        f"""<a href="https://www.linkedin.com/in/giovani-bruno-dos-santos-costa/">
        <img src="data:image/png;base64,{base64.b64encode(open("imagens/logos/linkedin.png", "rb").read()).decode()}" width="50">
        </a>""",
        unsafe_allow_html=True
    )
    c2.markdown(
        f"""<a href="https://github.com/giovani-bruno">
        <img src="data:image/png;base64,{base64.b64encode(open("imagens/logos/github.png", "rb").read()).decode()}" width="50">
        </a>""",
        unsafe_allow_html=True

    )
    c3.markdown(
        f"""<a href="https://www.instagram.com/giovanibrn_/">
        <img src="data:image/png;base64,{base64.b64encode(open("imagens/logos/instagram.png", "rb").read()).decode()}" width="50">
        </a>""",
        unsafe_allow_html=True
    )
with col2:
    st.write("""
        Sou estudante de Ciência da Computação, atualmente no 5° semestre na Universidade da Amazônia. Tenho 20 anos e grande interesse em ciência de dados, especialmente nas áreas de machine learning, deep learning e LLMs. Concluí a Certificação Profissional em Ciência de Dados da IBM pela Coursera, e atualmente a maior parte dos meus estudos são realizados nessa plataforma, complementando com livros e outras fontes de aprendizado.
        Minhas formas favoritas de aprender são por meio de cursos, realizando projetos, livros e, principalmente, ensinando. Por isso, compartilho semanalmente no LinkedIn conteúdos práticos sobre ciência de dados, Python, inteligência artificial e outros temas relacionados, uma maneira de fixar o que aprendo e ajudar outras pessoas a aprenderem também.
        Cofundei a LADS (League of Artificial Intelligence and Data Science), uma liga onde reunimos entusiastas da área para crescermos juntos. Na LADS, desenvolvemos projetos em parceria com empresas e sou um dos responsáveis por ministrar aulas para os membros, trabalhando ao lado dos outros fundadores e professores parceiros da liga.
        Atuo constantemente no fortalecimento das minhas habilidades em manipulação e visualização de dados, automação e desenvolvimento de modelos preditivos, sempre buscando aplicar esse conhecimento na prática para gerar soluções com impacto real. Meu objetivo é atuar como cientista de dados, criando valor por meio da análise e inteligência aplicada aos dados.
            """)   
st.divider()

st.subheader("🎓 Formação")
col1, col2 = st.columns([0.2, 1])
col1.image("imagens/logos/unama.png", width=150)
col2.subheader("UNAMA - Universidade da Amazônia")
col2.write("Bacharelado, Ciência da Computação (2023 - 2026)")
col2.write("Atualmente no 5° semestre.")
st.divider()

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



st.subheader("⚒️ Habilidades")

habilidades = [
    "Python", "Power BI", "Excel", "SQL",
    "AWS", "Git", "Pandas", "NumPy",
    "Matplotlib", "Seaborn", "Plotly", "Dash",
    "Streamlit", "Scikit-learn", "Tensor Flow", "Keras",
    "Scipy", "statsmodels", "Selenium", "Beautiful Soup"
]

carrossel_habilidades(tecnologias, habilidades)


# st.subheader("⚒️ Habilidades")
# st.write("")
# col1, col2, col3, col4 = st.columns(4)

# adicionar_habilidade(tecnologias["Python"], col1, 150)
# adicionar_habilidade(tecnologias["Power BI"], col2, 170)
# adicionar_habilidade(tecnologias["Excel"], col3, 150)
# adicionar_habilidade(tecnologias["SQL"], col4, 170)
# adicionar_habilidade(tecnologias["AWS"], col1, 120)
# adicionar_habilidade(tecnologias["Git"], col2, 120)
# adicionar_habilidade(tecnologias["Pandas"], col3, 150)
# adicionar_habilidade(tecnologias["NumPy"], col4, 150)
# adicionar_habilidade(tecnologias["Matplotlib"], col1, 150)
# adicionar_habilidade(tecnologias["Seaborn"], col2, 150)
# adicionar_habilidade(tecnologias["Plotly"], col3, 150)
# adicionar_habilidade(tecnologias["Dash"], col4, 150)
# adicionar_habilidade(tecnologias["Streamlit"], col1, 150)
# adicionar_habilidade(tecnologias["Scikit-learn"], col2, 100)
# adicionar_habilidade(tecnologias["Tensor Flow"], col3, 200)
# adicionar_habilidade(tecnologias["Keras"], col4, 200)
# adicionar_habilidade(tecnologias["Scipy"], col1, 150)
# adicionar_habilidade(tecnologias["statsmodels"], col2, 200)
# adicionar_habilidade(tecnologias["Selenium"], col3, 150)
# adicionar_habilidade(tecnologias["Beautiful Soup"], col4, 150)

st.divider()

st.subheader("📨 Entre em contato")

st.html(f"""
    {css_formulario}
    <form class="contact-form" action="https://formsubmit.co/{st.secrets['form_submit_code']}" method="POST">
        <div class="form-row">
            <input type="hidden" name="_template" value="table">
            <input type="text" name="name" placeholder="Seu nome" required>
            <input type="email" name="email" placeholder="Seu email" required>
        </div>
        <textarea name="message" placeholder="Sua mensagem aqui" required></textarea>
        <div class="button-container">
            <button type="submit">Enviar</button>
        </div>
    </form>
""")
