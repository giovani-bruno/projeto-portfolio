import streamlit as st
import base64
from main import barra_navegacao
from utils import tecnologias, carrossel_habilidades, grid_habilidades, fix_iframe_carrosel, css_formulario

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
        Sou estudante de Ciência da Computação no 7° semestre na Universidade da Amazônia, tenho 21 anos e sou estagiário no Ministério Público do Pará. 
        Tenho grande interesse em ciência de dados, com foco em machine learning, deep learning e LLMs.
        Concluí a Certificação Profissional em Ciência de Dados da IBM pela Coursera, onde finalizei toda a trilha de cursos, 
        consolidando uma base sólida na área. Atualmente, sigo aprofundando meus conhecimentos por meio de projetos práticos, 
        leitura de livros técnicos e exploração de novas ferramentas e técnicas. Acredito que a melhor forma de aprender é aplicando e ensinando. 
        Ao longo da minha jornada, já estive envolvido na criação de iniciativas voltadas ao compartilhamento de conhecimento em dados, além de 
        desenvolver projetos com foco em resolver problemas reais. Busco constantemente evoluir minhas habilidades em manipulação e visualização de 
        dados, automação e desenvolvimento de modelos preditivos, sempre com o objetivo de gerar impacto prático. Meu objetivo é atuar como cientista de dados, 
        criando valor por meio da análise e inteligência aplicada aos dados.
        """)   
st.divider()

st.subheader("🎓 Formação")
col1, col2 = st.columns([0.2, 1])
col1.image("imagens/logos/unama.png", width=150)
col2.subheader("UNAMA - Universidade da Amazônia")
col2.write("Bacharelado, Ciência da Computação (2023 - 2026)")
col2.write("Atualmente no 7° semestre.")
st.divider()

st.subheader("⚒️ Habilidades")

habilidades = [
    "Python", "Power BI", "Excel", "SQL",
    "AWS", "Git", "Pandas", "NumPy",
    "Matplotlib", "Seaborn", "Plotly", "Dash",
    "Streamlit", "Scikit-learn", "Tensor Flow", "Keras",
    "Scipy", "statsmodels", "Selenium", "Beautiful Soup",
    "N8N", "CrewAI", "Hugging Face", "LangChain",
    "Agno", "Llama Index"
]

fix_iframe_carrosel()
carrossel_habilidades(tecnologias, habilidades)

if st.toggle("Exibir tudo"):
    grid_habilidades(tecnologias, habilidades)

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
