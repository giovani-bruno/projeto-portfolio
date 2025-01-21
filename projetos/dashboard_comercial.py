import streamlit as st
from main import barra_navegacao
from utils import tecnologias, adicionar_tecnologia, botao_voltar

st.set_page_config(layout='wide',page_title="Dashboard Comercial")
barra_navegacao()
botao_voltar()

st.title("Dashboard de Desempenho de Vendas e Clientes no Power BI")

st.write("""Este é um projeto de análise de vendas e clientes, desenvolvido como parte do curso de Power BI da Hashtag Treinamentos. 
         Utilizando o banco de dados fictício Adventure Works 2014, amplamente reconhecido em treinamentos, este projeto permitiu aplicar 
         técnicas de consulta em SQL Server e criar dashboards interativos no Power BI para transformar dados em informações estratégicas.""")

st.write("O objetivo principal foi oferecer insights claros e detalhados sobre o desempenho financeiro, vendas e comportamento dos clientes da Adventure Works. O dashboard inclui:")

st.write("""
- Receita Total e Lucro Total: Avaliação acumulada do desempenho financeiro.
- Quantidade Vendida e Categorias de Produtos: Análise do volume de vendas e produtos mais vendidos.
- Total de Clientes: Dados demográficos, com filtros por país e gênero.
- Receita e Lucro Mensal: Identificação de padrões e sazonalidade nas vendas.
- Margem de Lucro por Mês: Eficiência das vendas ao longo do tempo.
""")

st.write("""O dashboard foi projetado para ser altamente dinâmico, 
         permitindo filtrar por ano através de botões interativos 
         e ajustar visualizações ao clicar em gráficos específicos, 
         como por país ou categoria de produto.""")

st.write("""A análise gerou insights valiosos, como:
- Identificação de mercados prioritários, com Estados Unidos e Austrália liderando em lucro.
- Sazonalidade nas vendas, destacando meses de pico.
- Distribuição demográfica de clientes, auxiliando em estratégias de marketing regional.
- Produtos mais lucrativos, permitindo priorizar categorias com maior impacto no lucro.""")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2 = st.columns(2)

adicionar_tecnologia(tecnologias['Power BI'], "Ferramenta principal usada para criar o dashboard.", 200, col1)
adicionar_tecnologia(tecnologias['SQL'], "Banco de dados utilizadado para se conectar com o Power BI e extrair os dados.", 200, col2)

st.divider()

st.markdown('<iframe title="Dashboard Comercial" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiZDg3MjQ2ODgtNGRkOS00NWQwLTg5NGYtNWUzMmI4MTIwNjQ1IiwidCI6ImQxNjgyYjJjLWRhMzMtNGZiOC1hN2FkLThjNjA5YzE2YzNiMCJ9&pageName=069e44aa7599c5eae4ad" frameborder="0" allowFullScreen="true"></iframe>',
            unsafe_allow_html=True)

st.divider()

st.write("""Este projeto de Análise de Vendas e Clientes foi uma excelente oportunidade para consolidar 
         e aplicar os conhecimentos adquiridos em SQL Server e Power BI. A integração entre essas 
         ferramentas proporcionou uma análise eficiente de dados, permitindo a criação de um dashboard 
         dinâmico e interativo, que trouxe insights valiosos sobre o desempenho financeiro, vendas e 
         comportamento dos clientes da Adventure Works.""")
