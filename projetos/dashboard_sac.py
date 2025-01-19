import streamlit as st
from main import barra_navegacao
from utils import tecnologias, adicionar_tecnologia, voltar_para_projetos

st.set_page_config(layout='wide',page_title="Dashboard SAC")
barra_navegacao()
voltar_para_projetos()

st.title("Dashboard de Ánalise de Antendimento aos Usuários no Power BI")

st.write("""O Dashboard de SAC (Serviço de Atendimento ao Cliente) foi desenvolvido no 
         curso Power BI Impressionador da Hashtag Treinamentos, com o objetivo de otimizar a análise 
         do atendimento aos usuários e melhorar a eficiência dos processos de suporte. Utilizando o 
         Power BI, o dashboard permite uma visão completa e interativa sobre o desempenho do SAC, 
         facilitando a análise de diversos indicadores-chave.""")

st.write("""A principal necessidade deste projeto surgiu da busca por uma ferramenta que fosse capaz 
         de acompanhar e analisar em tempo real os dados de atendimento, proporcionando informações 
         valiosas sobre o comportamento dos usuários e a eficiência da equipe de suporte. Com isso, 
         é possível obter uma visão clara sobre o total de atendimentos, médias diárias de respostas, 
         chamados abertos e respondidos por mês, além de identificar os principais problemas que motivam 
         os chamados e o tempo médio de atendimento por mês.""")

st.write("""Além disso, o dashboard oferece funcionalidades avançadas, como tooltips interativos, 
         que permitem uma análise mais detalhada dos dados, possibilitando aos gestores realizar 
         decisões mais informadas. Também é possível identificar quais usuários mais frequentemente 
         abrem chamados, o que pode ajudar a direcionar ações específicas de melhoria no atendimento.""")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2 = st.columns(2)

adicionar_tecnologia(tecnologias['Power BI'], "Ferramenta principal usada para criar o dashboard.", 200, col1)
adicionar_tecnologia(tecnologias['Excel'], "Ferramenta de onde os dados foram retirados.", 200, col2)

st.divider()

st.markdown('<iframe title="Dashboard SAC" width="1330" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiZGZkMTYxZTQtZmYzMy00YzZkLThkNTYtNGMwZjhjZWU1MzY0IiwidCI6ImQxNjgyYjJjLWRhMzMtNGZiOC1hN2FkLThjNjA5YzE2YzNiMCJ9&pageName=ReportSection9b21469c08043acbb796" frameborder="0" allowFullScreen="true"></iframe>',
            unsafe_allow_html=True)

st.divider()

st.write("""A análise de dados em tempo real, com recursos como tooltips e gráficos interativos, 
         demonstrou ser essencial para melhorar a tomada de decisões e a eficiência da equipe de 
         suporte. O dashboard não só oferece insights sobre a performance do SAC, mas também facilita 
         a identificação de problemas recorrentes e usuários que mais geram chamados, possibilitando 
         ações mais rápidas e eficazes.""")
