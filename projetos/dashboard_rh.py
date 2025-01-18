import streamlit as st
from main import barra_navegacao
from auxiliar import tecnologias, adicionar_tecnologia, voltar_para_projetos

st.set_page_config(layout='wide',page_title="Dashboard RH")
barra_navegacao()
voltar_para_projetos()

st.title("Dashboard de Recursos Humanos no Power BI")

st.write("""Este Dashboard de Recursos Humanos (RH) foi desenvolvido no Power BI como parte do 
         curso Power BI Impressionador da Hashtag Treinamentos, com o objetivo de criar uma solução robusta 
         para análise de dados relacionados à gestão de pessoas. Este dashboard foi projetado para fornecer 
         insights detalhados sobre o comportamento e a dinâmica dos funcionários dentro da empresa, além de 
         permitir um acompanhamento efetivo de processos como contratações, desligamentos, turnover e perfil dos funcionários.""")

st.write("""A necessidade deste projeto surge da crescente demanda por ferramentas de visualização de dados 
         que permitam aos gestores de RH tomar decisões mais informadas e estratégicas, baseadas em dados reais e atualizados. 
         O dashboard possui cinco páginas, cada uma com um foco específico:""")

st.write("""
1. Geral: Fornece uma visão ampla do quadro de funcionários, com informações sobre o número de funcionários ativos, 
         contratações, desligamentos e percentual de turnover, permitindo o acompanhamento de métricas de rotatividade e desempenho da equipe.

2. Contratações: Apresenta dados sobre as contratações realizadas, com filtros detalhados por estado, cidade, área, nível, 
         tempo de empresa e faixa etária, permitindo uma análise precisa da evolução das contratações ao longo do tempo.

3. Desligamentos: Exibe as informações sobre desligamentos por estado, cidade, área, nível, tempo de empresa e faixa etária, 
         com a capacidade de filtrar por cidade e ano, proporcionando uma visão detalhada sobre os motivos e padrões de saída de funcionários.

4. Perfil da Empresa: Apresenta dados sobre a composição do quadro de funcionários por sexo, incluindo folha salarial e média salarial, 
         além de permitir o detalhamento da quantidade de funcionários ativos por nível e sexo, ajudando a entender melhor a diversidade e a estrutura salarial da empresa.

5. Perfil dos Funcionários: Oferece uma análise individualizada de cada funcionário, com avaliações de desempenho, 
         gráficos de competências e comparações de desempenho nas áreas de trabalho em equipe, comunicação, liderança, organização e iniciativa.
""")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2 = st.columns(2)

adicionar_tecnologia(tecnologias['Power BI'], "Principal ferramenta usada para criar o dashboard.", 200, col1)
adicionar_tecnologia(tecnologias['Excel'], "Ferramenta de onde os dados foram retirados.", 200, col2)

st.divider()

st.markdown('<iframe title="Dashboard RH" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiMmZiZTE0MjctZjhkMC00MjZlLTgzNGQtMWY2MDA3NDAzNjM0IiwidCI6ImQxNjgyYjJjLWRhMzMtNGZiOC1hN2FkLThjNjA5YzE2YzNiMCJ9&pageName=ReportSection62440c407ac07b287c1b" frameborder="0" allowFullScreen="true"></iframe>',
            unsafe_allow_html=True)

st.write("""Com funcionalidades interativas e filtros detalhados, o dashboard oferece aos gestores de RH 
         uma ferramenta poderosa para monitorar o quadro de funcionários, entender padrões de comportamento e 
         performance, e tomar decisões mais estratégicas. Este projeto demonstrou a importância da visualização 
         de dados no processo de gestão de pessoas, oferecendo uma solução eficaz para acompanhar e analisar diversos indicadores-chave do RH.""")
