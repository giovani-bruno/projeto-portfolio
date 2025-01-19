import streamlit as st
from main import barra_navegacao
from utils import tecnologias, adicionar_tecnologia, voltar_para_projetos

st.set_page_config(layout='wide', page_title="Automações no Wifi")
barra_navegacao()
voltar_para_projetos()

st.title("Automações em um Wifi Corporativo")

st.write("""Este projeto foi criado para otimizar o gerenciamento do Wi-Fi corporativo da empresa onde trabalho, 
         onde o acesso à rede exige, além da senha, o registro do endereço MAC do dispositivo no site do Wi-Fi. 
         A infraestrutura conta com três Access Points (APs), localizados nos setores Administrativo, Manutenção e Logística.
          Caso o dispositivo precise acessar o Wi-Fi em todos os setores, o registro precisava ser repetido manualmente em cada um dos APs.""")

st.write("""O processo manual envolvia acessar o site do Wi-Fi para cada setor, localizar a tabela de usuários, 
         preencher as informações (nome, endereço MAC e setor) e salvar as alterações. Este método era extremamente lento.""")

st.write("Para resolver esses problemas, desenvolvi três automações:")

st.write("""1. Adicionar Usuário: Essa automação permite registrar até 10 dispositivos simultaneamente. 
         O usuário preenche informações como nome (seguindo o padrão: DISPOSITIVO - NOME - SETOR), 
         endereço MAC e os setores em que o dispositivo será registrado (Administrativo, Manutenção, Logística ou todos). Após confirmar,
         a automação acessa o site do Wi-Fi e realiza os registros automaticamente nos APs selecionados.""")
st.write("""2. Editar Endereço MAC: Facilita a correção ou atualização de endereços MAC registrados. 
         O usuário pode buscar o registro desejado pelo nome ou pelo endereço MAC e, em seguida, a automação realiza as alterações.""")
st.write("""3. Remover Usuário: Permite a exclusão de dispositivos registrados no sistema. Assim como na edição, o 
         usuário pode buscar pelo nome ou endereço MAC para localizar o registro e removê-lo dos APs necessários.""")

st.divider()

st.write("""Também fiz outra automação que envolve os outros dois Wi-Fis da empresa:
         existem dois pontos de acesso específicos para visitantes, que não exigem registro de endereço MAC, 
         apenas a senha para conexão. Conforme a política da empresa, as senhas desses Wi-Fis devem ser alteradas no último dia de cada mês e enviadas 
         por e-mail ao meu chefe para garantir a segurança e controle do acesso.""")

st.write("""Antes da automação, o processo era realizado manualmente. Isso envolvia acessar o site de gerenciamento dos dois Wi-Fis, 
         criar novas senhas, atualizar as configurações de cada ponto de acesso e enviar um e-mail manualmente com as novas credenciais. 
         Apesar de parecer simples, esse fluxo demandava atenção e tempo, pois as senhas desses dois Wi-Fis devem ser difíceis.""")

st.write("Com a automação implementada, o fluxo tornou-se rápido e confiável. Agora, no último dia de cada mês, basta executar o programa, que realiza as seguintes etapas automaticamente:")


st.write("1. Acesso ao Site: A automação faz login no site de gerenciamento dos dois Wi-Fis de convidados.")
st.write("2. Troca de Senhas: Gera novas senhas de forma segura e atualiza as configurações nos dois Wi-Fis.")
st.write("3. Envio de E-mail: Envia um e-mail para meu chefe contendo as novas senhas, com o corpo da mensagem já formatado.")

st.divider()

st.write("Estes projetos foram inteiramente desenvolvido por mim, desde a concepção da ideia até a implementação final.")

st.write("Por se tratar projetos internos para a empresa, os códigos-fontes estão armazenados em repositórios privados no GitHub e não podem ser compartilhado publicamente devido a questões de confidencialidade.")

st.divider()

st.subheader("Tecnologias Utilizadas")
col1, col2, col3 = st.columns(3)
adicionar_tecnologia(tecnologias['Python'], "Linguagem de Programação utilizada para automatizar todo o processo.", 200, col1)

adicionar_tecnologia(tecnologias['Selenium'], "Biblioteca do Python responsável por automatizar o navegador.", 200, col2)

adicionar_tecnologia(tecnologias['Tkinter'], "Biblioteca do Python utilizada para criar a janela onde o usuário insere as informações.", 150, col3)

adicionar_tecnologia(tecnologias['SMTP'], "Biblioteca do Python utilizada para enviar o e-mail automaticamente para meu chefe informando as novas senhas.", 150, col1)

adicionar_tecnologia(tecnologias['Random'], "Biblioteca do Python usada em conjunto com a biblioteca string para gerar as novas senhas.", 150, col2)

adicionar_tecnologia(tecnologias['String'], "Biblioteca do Python usada em conjunto com a biblioteca random para gerar as novas senhas.", 150, col3)

st.divider()

st.write("Não é possível mostrar os vídeos demonstrando as automações em execução, pois ela acessa informações confidenciais relacionadas aos sistemas internos do Wi-Fi da empresa.")
st.write("A seguir, apenas as imagens da interface do programa onde o usuário insere as informações:")

st.subheader("Automação Adicionar Usuários")
st.image(r"projetos\videos-imagens\automacao_adicionar_usuario.png")

st.subheader("Automação Editar Mac")
st.image(r"projetos\videos-imagens\automacao_editar_mac.png")

st.subheader("Automação Remover Usuário")
st.image(r"projetos\videos-imagens\automacao_remover_usuario.png")

st.write("Não é possível mostrar a imagem da automação de trocar a senha, pois ela não tem interface. Só é preciso executar.")

st.write("""Essas automações trouxeram eficiência e economia de tempo para processos essenciais na gestão do Wi-Fi corporativo da empresa. 
         Desde o registro e gerenciamento de dispositivos pelo endereço MAC até a atualização mensal das senhas dos Wi-Fis de convidados, 
         cada solução foi projetada para eliminar tarefas repetitivas e minimizar erros manuais. Com essas ferramentas, a equipe pode se 
         concentrar em atividades estratégicas, enquanto a automação garante a execução confiável e segura das operações de rede.""")
