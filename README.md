# Análise de Evasão Acadêmica  

## Visão Geral do Projeto  
Este projeto é uma aplicação web focada na **análise e prevenção da evasão acadêmica**.  
Ele combina um backend desenvolvido com **Flask** e visualizações interativas construídas com **Streamlit**, oferecendo ferramentas para:  
- **Visualização de Dados Acadêmicos**: Dashboards interativos para identificar padrões que podem levar à evasão.  
- **Previsão de Evasão**: Análise de novos alunos baseada em dados históricos para calcular a probabilidade de abandono escolar.  
- **Gerenciamento de Registros**: Adicionar, pesquisar e remover alunos de maneira eficiente.  

---

## Objetivos do Projeto  
1. **Identificar Padrões**: Utilizar dashboards para compreender fatores associados à evasão acadêmica.  
2. **Analisar Novos Alunos**: Fornecer soluções específicas para auxiliar na tomada de decisões.  
3. **Gerenciar Dados**: Facilitar o cadastro, pesquisa e remoção de registros de forma simples e acessível.  

---

## Principais Funcionalidades  
### 1. Painéis Interativos  
- **Gráfico de Dispersão**: Relaciona desempenho acadêmico com frequência dos alunos.  
- **Gráfico de Barras**: Analisa o impacto de reprovações no abandono.  
- **Gráfico de Pizza**: Representa a satisfação dos alunos com o curso.  
- **Gráficos Avançados**: Explorando relações como condição socioeconômica e status de emprego.  

### 2. Adicionar e Analisar Novo Aluno  
- **Formulário interativo** para entrada de dados do aluno.  
- **Previsão da probabilidade de evasão** utilizando modelos de aprendizado de máquina.  
- **Registro automático** no banco de dados com atribuição de um ID único.  

### 3. Gerenciamento de Dados  
- Pesquisa de alunos por **ID**.  
- Exclusão de registros com confirmação para evitar erros.  

---

## Dependências  
A aplicação utiliza as seguintes bibliotecas e ferramentas:  
- **Flask**: Para desenvolvimento do backend.  
- **Streamlit**: Para construção dos dashboards.  
- **pandas**: Manipulação de dados.  
- **scikit-learn**: Implementação de modelos de aprendizado de máquina.  
- **plotly**: Criação de gráficos interativos.  

---

## Configuração do Ambiente 
1. Clonar ou repositório : 
2. Crie e ative um ambiente virtual : 
   python3 -m venv venv 
   source venv/bin/activate   # Para Linux/Mac 
   venv\Scripts\activate      # Para Windows 
3. Instalar as dependências : 
   pip install -r requirements.txt 

## Estrutura do Projeto 
![image](https://github.com/user-attachments/assets/62c7ff50-88c2-4dbe-96fd-ad378ae098a5)


## Rotas do Flask 
![image](https://github.com/user-attachments/assets/8b1c4992-c120-4ac2-a152-db461ad5c347)


## Executando a Aplicação 
1. Iniciar o servidor Flask : 
   python main.py 
2. Abra os Dashboards com Streamlit : 
   streamlit run dashboards/dashboard.py

## Exemplo de uso 
1. Acesse a página inicial ( /) e clique em INICIAR . 
2. No menu, selecione NOVA ANÁLISE para adicionar um aluno. 
3. Preencha o formulário com os dados do aluno e clique em Analisar . 
4. Visualize a probabilidade de evasão e confirme a adição do aluno. 
5. Para remover um aluno, vá para DELETAR DADO , pesquise pelo ID e confirme a exclusão.
