Análise de Evasão Acadêmica  
Visão Geral do Projeto 
Este projeto é uma aplicação web focada na análise e prevenção da evasão acadêmica. 
Ele combina um backend desenvolvido com Flask e visualizações interativas construídas 
com Streamlit , oferecendo ferramentas para: 
• Visualização de dados acadêmicos : Dashboards interativos para identificar 
padrões que podem levar à evasão. 
• Previsão de evasão : Análise de novos alunos baseada em dados históricos para 
calcular a probabilidade de abandono escolar. 
• Gerenciamento de registros : Adicionar, pesquisar e remover alunos de maneira 
eficiente. 
Objetivos do Projeto 
1. identificar Padrões : Utilização de dashboards para compreender fatores 
associados à evasão acadêmica. 
2. Analisar Novos Alunos : Fornecer soluções específicas para auxiliar na tomada 
de decisões. 
3. Gerenciar Dados : Facilitar o cadastro, pesquisa e remoção de registros de forma 
simples e acessível. 
Principais Funcionalidades 
1. Painéis Interativos 
• Gráfico de Dispersão : Relaciona desempenho acadêmico com frequência dos 
alunos. 
• Gráfico de Barras : Análise do impacto de reprovações no abandono. 
• Gráfico de Pizza : Representa a satisfação dos alunos com o curso. 
• Gráficos Avançados : Exploram relações como condição socioeconômica e 
status de emprego. 
2. Adicionar e analisar novo Aluno 
• Formulário interativo para entrada de dados do aluno. 
• Previsão da probabilidade de evasão utilizando modelos de aprendizado de 
máquina. 
• Registro automático no banco de dados com atribuição de um ID único . 
3. Gerenciamento de Dados 
• Pesquisa de alunos por ID. 
• Exclusão de registros com confirmação para evitar erros. 
Dependências 
A aplicação utiliza as seguintes bibliotecas e ferramentas: 
• Flask : Para desenvolvimento do backend. 
• Streamlit : Para construção dos dashboards. 
• pandas : Manipulação de dados. 
• scikit-learn : Implementação de modelos de aprendizado de máquina. 
• plotly : Criação de gráficos interativos. 
Configuração do Ambiente 
1. Clonar ou repositório : 
2. Crie e ative um ambiente virtual : 
python3 -m venv venv 
source venv/bin/activate   # Para Linux/Mac 
venv\Scripts\activate      # Para Windows 
3. Instalar as dependências : 
pip install -r requirements.txt 
Estrutura do Projeto 
projeto-evasao-academica/ 
├── main.py                    
├── dashboards/ 
│   └── dashboard.py           
├── data/ 
# Arquivo principal com as rotas Flask. 
# Visualizações e gráficos no Streamlit. 
│   └── dataListStudent.csv    # Dados dos alunos (base de dados). 
├── static/ 
│   └── css/                   
├── templates/ 
│   └── html/                  
# Arquivos CSS para estilização. 
# Templates HTML para o Flask. 
├── requirements.txt           
# Lista de dependências. 
└── README.md                  
# Documentação do projeto. 
Rotas do Flask 
Rota 
/ 
/menu 
/dashboards 
/nova_analise 
/adicionar_aluno 
Descrição 
Página inicial da aplicação. 
Página de seleção de funcionalidades. 
Dashboards interativos para análise de dados. 
Página para adicionar e analisar novos alunos. 
Processa a adição de novos alunos ao sistema. 
/confirmar_adicao Confirme e salve o novo registro no banco de dados. 
/deletar_aluno 
Página para excluir um aluno existente. 
/pesquisar_aluno Pesquisa alunos pelo ID . 
/confirmar_delecao Confirme e processe a exclusão do aluno no banco de dados. 
Executando a Aplicação 
1. Iniciar o servidor Flask : 
python main.py 
2. Abra os Dashboards com Streamlit : 
streamlit run dashboards/dashboard.py 
Exemplo de uso 
1. Acesse a página inicial ( /) e clique em INICIAR . 
2. No menu, selecione NOVA ANÁLISE para adicionar um aluno. 
3. Preencha o formulário com os dados do aluno e clique em Analisar . 
4. Visualize a probabilidade de evasão e confirme a adição do aluno. 
5. Para remover um aluno, vá para DELETAR DADO , pesquise pelo ID e confirme a 
exclusão. 
