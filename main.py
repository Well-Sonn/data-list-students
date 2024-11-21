from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('html/acesso.html')

@app.route('/menu')
def menu():
    return render_template('html/menu.html')

@app.route('/dashboards')
def dashboards():
    return render_template('html/dashboards.html')

@app.route('/nova_analise')
def nova_analise():
    return render_template('html/nova_analise.html')

@app.route('/adicionar_aluno', methods=['POST'])
def adicionar_aluno():
    # Obter dados do formulário
    desempenho_academico = float(request.form['desempenho_academico'])
    historico_reprovacoes = int(request.form['historico_reprovacoes'])
    frequencia = float(request.form['frequencia'])
    uso_recursos = float(request.form['uso_recursos'])
    condicao_socioeconomica = request.form['condicao_socioeconomica']
    status_emprego = request.form['status_emprego']
    nivel_satisfacao = int(request.form['nivel_satisfacao'])

    # Carregar o DataFrame existente
    df = pd.read_csv("dataListStudent.csv", sep=",", decimal=".")

    # Preprocessamento dos dados
    le_condicao = LabelEncoder()
    le_status = LabelEncoder()
    le_abandono = LabelEncoder()

    df['Condição Socioeconômica'] = le_condicao.fit_transform(df['Condição Socioeconômica'])
    df['Status de Emprego'] = le_status.fit_transform(df['Status de Emprego'])
    df['Abandono'] = le_abandono.fit_transform(df['Abandono'])

    # Separar características e rótulo
    X = df[['Desempenho Acadêmico', 'Histórico de Reprovações', 'Frequência (%)', 'Uso de Recursos Institucionais (%)', 'Condição Socioeconômica', 'Status de Emprego', 'Nível de Satisfação com o Curso']]
    y = df['Abandono']

    # Dividir os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinar o modelo
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Transformar os novos dados
    condicao_socioeconomica_encoded = le_condicao.transform([condicao_socioeconomica])[0] if condicao_socioeconomica in le_condicao.classes_ else -1
    status_emprego_encoded = le_status.transform([status_emprego])[0] if status_emprego in le_status.classes_ else -1

    if condicao_socioeconomica_encoded == -1 or status_emprego_encoded == -1:
        return "Erro: Condição Socioeconômica ou Status de Emprego desconhecido."

    # Prever a evasão do novo aluno
    novo_aluno = pd.DataFrame({
        'Desempenho Acadêmico': [desempenho_academico],
        'Histórico de Reprovações': [historico_reprovacoes],
        'Frequência (%)': [frequencia],
        'Uso de Recursos Institucionais (%)': [uso_recursos],
        'Condição Socioeconômica': [condicao_socioeconomica_encoded],
        'Status de Emprego': [status_emprego_encoded],
        'Nível de Satisfação com o Curso': [nivel_satisfacao]
    })

    previsao = model.predict(novo_aluno)[0]
    resultado = "ESSE ALUNO É PASSIVEL DE EVASAO" if previsao == 1 else "ESSE ALUNO NAO É PASSIVEL DE EVASAO"

    # Adicionar ID e previsão ao novo aluno
    novo_aluno['ID'] = df['ID'].max() + 1
    novo_aluno['Abandono'] = 'sim' if previsao == 1 else 'nao'

    return render_template('html/resultado_analise.html', resultado=resultado, aluno=novo_aluno.to_dict(orient='records')[0])

@app.route('/confirmar_adicao', methods=['POST'])
def confirmar_adicao():
    # Obter dados do formulário
    aluno = request.form.to_dict()
    aluno['ID'] = int(aluno['ID'])
    aluno['Desempenho Acadêmico'] = float(aluno['Desempenho Acadêmico'])
    aluno['Histórico de Reprovações'] = int(aluno['Histórico de Reprovações'])
    aluno['Frequência (%)'] = float(aluno['Frequência (%)'])
    aluno['Uso de Recursos Institucionais (%)'] = float(aluno['Uso de Recursos Institucionais (%)'])
    aluno['Nível de Satisfação com o Curso'] = int(aluno['Nível de Satisfação com o Curso'])
    aluno['Abandono'] = aluno['Abandono']

    # Carregar o DataFrame existente
    df = pd.read_csv("dataListStudent.csv", sep=",", decimal=".")
    
    # Adicionar o novo aluno ao DataFrame
    novo_aluno_df = pd.DataFrame([aluno])
    df = pd.concat([df, novo_aluno_df], ignore_index=True)

    # Salvar o DataFrame atualizado no arquivo CSV
    df.to_csv("dataListStudent.csv", index=False, sep=",", decimal=".")
    
    # Renderizar a página de confirmação com o ID do aluno
    return render_template('html/confirmacao_adicao.html', aluno_id=aluno['ID'])

@app.route('/deletar_aluno')
def deletar_aluno():
    return render_template('html/deletar_aluno.html')

@app.route('/pesquisar_aluno', methods=['POST'])
def pesquisar_aluno():
    aluno_id = int(request.form['aluno_id'])
    df = pd.read_csv("dataListStudent.csv", sep=",", decimal=".")
    aluno = df[df['ID'] == aluno_id].to_dict(orient='records')
    if aluno:
        return render_template('html/resultado_pesquisa.html', aluno=aluno[0])
    else:
        return render_template('html/resultado_pesquisa.html', aluno=None, mensagem="Aluno não encontrado.")

@app.route('/confirmar_delecao', methods=['POST'])
def confirmar_delecao():
    aluno_id = int(request.form['aluno_id'])
    df = pd.read_csv("dataListStudent.csv", sep=",", decimal=".")
    df = df[df['ID'] != aluno_id]
    df.to_csv("dataListStudent.csv", index=False, sep=",", decimal=".")
    return render_template('html/delecao_sucesso.html')

if __name__ == '__main__':
    app.run(debug=True)