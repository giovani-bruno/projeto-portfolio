import streamlit as st
import base64
from main import barra_navegacao
from auxiliar import tecnologias, adicionar_habilidade

st.set_page_config(page_title="Sobre", layout='wide')
barra_navegacao()

st.title("Olá, me chamo Giovani 👋🏻")
col1, col2 = st.columns([0.1, 1])
with col1:
    st.image("imagens/giovani.jpeg", width=150)
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
    Sou um estudante de Ciência da Computação, atualmente no 5° semestre, com grande interesse em ciência de dados. Concluí cursos de destaque na área de dados, maioria deles pela Hashtag Treinamentos.
    Estou constantemente buscando fortalecer minhas habilidades em manipulação de dados, visualização e machine learning, utilizando datasets públicos e projetos próprios. Também procuro aplicar esse conhecimento em automação e otimização de tarefas no ambiente corporativo.
    Atualmente, faço postagens semanais no meu LinkedIn onde compartilho dicas práticas sobre ciência de dados, análise de dados, inteligência artificial, Python, compartilhar projetos e entre outros temas. Essas dicas são baseadas nos conhecimentos que adquiro nos livros que leio e nos cursos que faço.
    Minha meta é me tornar um cientista de dados e contribuir para soluções que façam a diferença.
             """)   
st.divider()

st.subheader("🎓 Formação")
col1, col2 = st.columns([0.2, 1])
col1.image("imagens/logos/unama.png", width=150)
col2.subheader("UNAMA - Universidade da Amazônia")
col2.write("Bacharelado, Ciência da Computação (2023 - 2026)")
col2.write("Atualmente no 5° semestre, previsão de conlusão para 2026")
st.divider()

st.subheader("⚒️ Habilidades")
st.write("")
col1, col2, col3, col4 = st.columns(4)
    
adicionar_habilidade(tecnologias["Python"], col1, 150)
adicionar_habilidade(tecnologias["Power BI"], col2, 170)
adicionar_habilidade(tecnologias["Excel"], col3, 150)
adicionar_habilidade(tecnologias["SQL"], col4, 170)
adicionar_habilidade(tecnologias["Git"], col1, 150)
adicionar_habilidade(tecnologias["Pandas"], col2, 150)
adicionar_habilidade(tecnologias["NumPy"], col3, 150)
adicionar_habilidade(tecnologias["Matplotlib"], col4, 150)
adicionar_habilidade(tecnologias["Seaborn"], col1, 150)
adicionar_habilidade(tecnologias["Plotly"], col2, 150)
adicionar_habilidade(tecnologias["Streamlit"], col3, 150)
adicionar_habilidade(tecnologias["Scikit-learn"], col4, 100)
adicionar_habilidade(tecnologias["Selenium"], col1, 150)
adicionar_habilidade(tecnologias["Tkinter"], col2, 150)
adicionar_habilidade(tecnologias["Figma"], col3, 150)
adicionar_habilidade(tecnologias["AWS"], col4, 120)

st.divider()

st.markdown("""
    <style>
        .contact-form {
            background-color: #1B221E;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 0 auto;
            margin: 0 auto;
        }
        .contact-form input, .contact-form textarea {
            background-color: #f9f9f9;
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box;
            font-size: 16px;
        }
        .contact-form button {
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
            font-size: 18px;
        }
        .contact-form button:hover {
            background-color: #45a049;
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
""", unsafe_allow_html=True)

st.subheader("📨 Entre em contato")

form_contato = f"""
    <form class="contact-form" action="https://formsubmit.co/58e51974853553c0014dc737cb5461cd" method="POST">
        <div class="form-row">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Seu nome" required>
            <input type="email" name="email" placeholder="Seu email" required>
        </div>
        <textarea name="message" placeholder="Sua mensagem aqui" required></textarea>
        <button type="submit">Enviar</button>
    </form>
"""

st.markdown(form_contato, unsafe_allow_html=True)
