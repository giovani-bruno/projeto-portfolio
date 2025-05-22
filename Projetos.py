import streamlit as st
from main import barra_navegacao
from utils import adicionar_projeto

st.set_page_config(page_title='Projetos', layout='wide', page_icon='💻')
barra_navegacao()

st.title("Projetos")
st.write("""
### Explore meus projetos
Aqui estão os principais projetos que desenvolvi. Cada projeto reflete meu aprendizado e dedicação para resolver problemas.
""")
st.divider()

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

                .st-key-{i} {{
                    border-radius: 0.75rem;
                    padding: 1rem;
                    animation: goldenSnake 6s linear infinite;
                    background: transparent;
                }}
            </style>
        """)
    else:
        st.html(f"""
            <style>   
                .st-key-{i} {{
                    border: 1px solid rgba(250, 250, 250, 0.2);
                    border-radius: 0.75rem;
                    padding: 1rem;
                }}

                .stElementContainer {{
                    display: flex;
                    justify-content: center;
                    position: relative;
                    width: 100%;
                }}
            </style>
        """)