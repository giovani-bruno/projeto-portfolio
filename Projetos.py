import streamlit as st
from main import barra_navegacao
from utils import adicionar_projeto, destacar_borda

st.set_page_config(page_title='Projetos', layout='wide', page_icon='💻')
barra_navegacao()

st.title("Projetos")
st.write("""
### Explore meus projetos
Aqui estão os principais projetos que desenvolvi. Cada projeto reflete meu aprendizado e dedicação para resolver problemas.
""")
st.html("<hr style=' width: auto; max-width: 100%; position: relative; border: none; border-top: 1px solid #3D4044; margin: 1rem 0;'>")

projetos = [
        {"projeto": "stark", "destaque": True},
        {"projeto": "prevendo_doenca_cardiaca"},
        {"projeto": "ml_do_zero"},
        {"projeto": "analisando_emprestimos"},
        {"projeto": "prevendo_precos_airbnb"},
        {"projeto": "pesquisa_precos"},
        {"projeto": "prevendo_qualidade_carros"},
        {"projeto": "gerador_relatorio"},
        {"projeto": "automacoes_wifi"},
        {"projeto": "algoritmo_genetico"},
        {"projeto": "calculadora"},
        {"projeto": "dashboard_comercial"},
        {"projeto": "dashboard_sac"},
        {"projeto": "dashboard_rh"},
        {"projeto": "portfolio"}
]

colunas = st.columns(3)
for i, projeto in enumerate(projetos):
    coluna = colunas[i % 3]
    adicionar_projeto(projeto['projeto'], coluna, i)

    if projeto.get("destaque"):
        destacar_borda(i)
    else:
        st.html(f"""
            <style>   
                .st-key-{i} {{
                    border: 1px solid rgba(250, 250, 250, 0.2);
                    border-radius: 0.75rem;
                    padding: 1rem;
                }}
            </style>
        """)