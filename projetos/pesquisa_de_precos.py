import streamlit as st
from main import barra_navegacao
from auxiliar import tecnologias, adicionar_tecnologia, voltar_para_projetos

st.set_page_config(layout='wide')
barra_navegacao()
voltar_para_projetos()

st.title("Pesquisa de Preços")
st.write("""Este projeto em Python automatiza a pesquisa de preços 
         de produtos no Google Shopping, coletando informações relevantes
          e enviando os resultados por e-mail. Com uma interface gráfica 
         intuitiva desenvolvida em Tkinter e um design visual criado no 
         Figma e Proxlight Design, a aplicação oferece uma experiência 
         de usuário prática e profissional. O usuário pode especificar o 
         produto desejado, os limites de preço (mínimo e máximo) e o 
         endereço de e-mail para receber os resultados. Utilizando Selenium 
         para automação do navegador, o script realiza a pesquisa, filtra os 
         resultados, armazena os dados em um DataFrame e gera uma tabela HTML. 
         Essa tabela, que destaca o produto com o menor preço, é enviada por e-mail ao usuário.""")

st.write("""Você pode executar este projeto simplesmente baixando 
         o arquivo 'pesquisaPrecos.exe' no [repositório do projeto](https://github.com/giovani-bruno/pesquisa_de_precos)!
         Insira o produto desejado, preço mínimo, máximo e o seu endereço de e-mail para receber os resultados.
         No final da automação, aparecerá uma mensagem na tela informando que o e-mail foi enviado para o endereço especificado.
         Você receberá o e-mail de 'comaparacaodeprecos@gmail.com', um e-mail que criei apenas para o propósito deste projeto.
         """)

st.write("""Tive a ideia de criar este projeto a partir do curso Python Impressionador da Hashtag Treinamentos.
         No curso, foi ensinado um projeto parecido com esse, que buscava pelos produtos com base em um planilha do excel.
         O que implementei foi: janela com o tkinter para o usuário buscar pelo produto que quiser e 
         envio da tabela de preços para o usuário com o menor preço destacado.""")
st.divider()

st.subheader("Tecnologias Utilizadas")
coluna1, coluna2, coluna3 = st.columns(3)
adicionar_tecnologia(tecnologias['Python'], 
                     "Linguagem de Programação usada para automatizar a pesquisa, filtrar os preços e enviar o email.",
                     150, coluna1)

adicionar_tecnologia(tecnologias['Selenium'],
                     "Biblioteca do Python usada para automatizar o navegador e coletar os dados.", 
                     150, coluna2)

adicionar_tecnologia(tecnologias['Pandas'], 
                     "Biblioteca do Python usada para gerar a tabela com as informações do produto que será enviada por e-mail.", 
                     150, coluna3)

adicionar_tecnologia(tecnologias['Tkinter'],
                     "Biblioteca do Python usada para criar a janela onde o usuário insere as informações do produto e o e-mail.",
                     75, coluna1)
st.divider()

st.image("imagens/imagem_projetos_temp.png")
st.write("""Este projeto demonstra como a combinação de técnicas de automação, 
         web scraping e manipulação de dados pode ser utilizada para resolver 
         problemas reais de forma eficiente. Através de uma interface gráfica 
         amigável e funcionalidades robustas, o projeto simplifica a pesquisa 
         de preços, permitindo que os usuários encontrem as melhores ofertas 
         de forma rápida e prática.""")

st.write("""Com a integração do Selenium para coletar dados, Tkinter para a interface gráfica, 
         e o envio automatizado de e-mails, o projeto proporciona uma experiência completa e 
         intuitiva. Oferecendo uma solução valiosa para consumidores que buscam economia na hora
         de comprar produtos pela internet.""")

st.write("""Futuras melhorias podem incluir suporte a mais fontes de pesquisa, 
         otimização do tempo de execução e maior personalização dos filtros de 
         busca, tornando a aplicação ainda mais versátil e eficiente. 
         Este projeto reflete o potencial do Python para criar soluções 
         práticas e de alto impacto em tarefas do cotidiano.""")