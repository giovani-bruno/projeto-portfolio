import streamlit as st
from main import barra_navegacao
from utils import tecnologias, adicionar_tecnologia, voltar_para_projetos, adicionar_video

st.set_page_config(layout='wide', page_title="Gerador de Relatório")
barra_navegacao()
voltar_para_projetos()

st.title("Gerador de Relatório")

st.write("""Este projeto visa otimizar o processo de geração de relatórios de descarte de materiais de TI na 
         empresa onde trabalho, substituindo um método manual e suscetível a erros por uma solução automatizada. 
         Com funcionalidades como preenchimento de formulários, revisão de dados, edição de materiais e histórico 
         de descartes, a aplicação garante eficiência, economia de tempo e maior precisão no controle dos itens descartados. 
         A solução representa um avanço significativo no fluxo de trabalho, transformando um processo lento em uma ferramenta ágil e confiável.""")

st.write("""Nesta empresa, frequentemente lidamos com o descarte de materiais de TI que não funcionam mais, 
         como mouse, teclado, monitor, entre outros. Para isso, é necessário criar um relatório contendo, para cada material, 
         informações como: nome, modelo, fabricante, código de ativo (um identificador próprio da empresa, nem todos possuem), 
         número de série e uma foto do material. Depois que o relatório é concluído, enviamos um e-mail para a diretoria com o 
         documento anexado, garantindo o controle adequado dos itens descartados.""")

st.write("""Antes de eu ter criado essa aplicação, todo o processo era feito de forma manual. Criávamos um documento 
         contendo todos os materiais, preenchendo todas as informações e adicionando a foto correspondente. 
         Esse método era extremamente ineficiente e demandava muito tempo, especialmente em casos em que havia 
         muitos materiais a serem descartados.""")

st.write("""A aplicação começa com um formulário interativo onde o usuário preenche as informações do material: 
         nome, modelo, fabricante, código de ativo, número de série e anexa uma foto. Ao clicar no botão adicionar, 
         essas informações são armazenadas temporariamente. Uma lista dinâmica, exibida na barra lateral, permite 
         visualizar todos os materiais adicionados, com opções para editar ou excluir itens, se necessário. 
         Quando todos os materiais são registrados, o usuário pode gerar o relatório clicando em um botão. Antes de finalizar, 
         é exibida uma tabela com os dados para revisão, garantindo que tudo esteja correto. Após a confirmação, 
         o relatório é gerado, e as informações são salvas no banco de dados. Outros dois botões aparecem: um para baixar 
         o relatório em formato PDF e outro para enviá-lo automaticamente por e-mail com o corpo da mensagem já formatado. 
         O banco de dados mantém um histórico dos materiais descartados, incluindo a data de descarte, o que ajuda no controle ao longo do tempo.""")

st.write("""Este projeto foi inteiramente desenvolvido por mim, 
         desde a concepção da ideia até a implementação final.
         Esse é um trabalho que reflete exclusivamente minha criatividade e habilidades técnicas.""")

st.write("Por se tratar de um projeto interno para a empresa, o código-fonte está armazenado em um repositório privado no GitHub e não pode ser compartilhado publicamente devido a questões de confidencialidade.")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2, col3 = st.columns(3)
adicionar_tecnologia(tecnologias['Python'], "Linguaguem de programação utilizada para criar a interface, gerar o relatorio, criar e adicionar os materiais no banco de dados.",
                     200, col1)

adicionar_tecnologia(tecnologias['Streamlit'], "Biblioteca do Python para criar a interface do projeto, com um formulário simples e intuitivo.",
                     200, col2)

adicionar_tecnologia(tecnologias['ReportLab'], "Biblioteca do Python usada para gerar o relatório em formato PDF.",
                     200, col3)

adicionar_tecnologia(tecnologias['SQLAlchemy'], "Biblioteca do Python usada para criar e gerenciar o banco de dados dos materiais descartados.",
                     200, col1)

adicionar_tecnologia(tecnologias['SMTP'], "Biblioteca do Python utilizada para enviar o e-mail com o relatório anexado para a diretoria automaticamente.",
                     200, col2)

st.divider()

adicionar_video("gerador_relatorio.mp4")

st.write("""Este projeto trouxe uma solução inovadora e eficiente para o processo de descarte de materiais de TI na empresa. 
         Ao automatizar tarefas que antes eram feitas manualmente, a aplicação reduziu significativamente o tempo gasto, 
         minimizou erros humanos e melhorou o controle e o registro dos itens descartados. O banco de dados integrado garante um 
         histórico confiável para consultas futuras, contribuindo para uma gestão mais organizada e profissional. Essa aplicação 
         não apenas otimizou o fluxo de trabalho, mas também destacou como a automação pode transformar processos corporativos, 
         demonstrando o impacto positivo da tecnologia no dia a dia empresarial.""")

st.write("Meu chefe gostou muito deste projeto!")
