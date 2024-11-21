import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_csv("dataListStudent.csv", sep=",", decimal=".")

# Título da aplicação
st.title("Análise de Evasão Acadêmica")

# 1. Gráfico de Dispersão: Desempenho Acadêmico vs. Frequência
st.header("Desempenho Acadêmico vs. Frequência")
condicao_socioeconomica = st.multiselect(
    "Condição Socioeconômica",
    options=df["Condição Socioeconômica"].unique(),
    default=df["Condição Socioeconômica"].unique()
)
status_emprego = st.multiselect(
    "Status de Emprego",
    options=df["Status de Emprego"].unique(),
    default=df["Status de Emprego"].unique()
)

filtered_df = df[
    (df["Condição Socioeconômica"].isin(condicao_socioeconomica)) &
    (df["Status de Emprego"].isin(status_emprego))
]

scatter_fig = px.scatter(
    filtered_df,
    x="Desempenho Acadêmico",
    y="Frequência (%)",
    color="Abandono",
    hover_data=["ID", "Nível de Satisfação com o Curso"],
    title="Relação entre Desempenho Acadêmico e Frequência"
)
st.plotly_chart(scatter_fig)

# 2. Gráfico de Barras: Contagem de Abandono por Histórico de Reprovações
st.header("Contagem de Abandono por Histórico de Reprovações")
abandono_histogram = px.histogram(
    df,
    x="Histórico de Reprovações",
    color="Abandono",
    barmode="group",
    title="Distribuição de Abandono por Histórico de Reprovações"
)
st.plotly_chart(abandono_histogram)

# 3. Gráfico de Pizza: Distribuição do Nível de Satisfação com o Curso
st.header("Distribuição do Nível de Satisfação com o Curso")
satisfacao_pie = px.pie(
    df,
    names="Nível de Satisfação com o Curso",
    title="Distribuição do Nível de Satisfação com o Curso entre Alunos"
)
st.plotly_chart(satisfacao_pie)

# 4. Gráfico de Dispersão: Desempenho Acadêmico Médio por Uso de Recursos e Frequência
st.header("Desempenho Acadêmico Médio por Uso de Recursos e Frequência")
uso_recursos_min, uso_recursos_max = st.slider(
    "Intervalo de Uso de Recursos Institucionais (%)",
    min_value=int(df["Uso de Recursos Institucionais (%)"].min()),
    max_value=int(df["Uso de Recursos Institucionais (%)"].max()),
    value=(int(df["Uso de Recursos Institucionais (%)"].min()), int(df["Uso de Recursos Institucionais (%)"].max()))
)
frequencia_min, frequencia_max = st.slider(
    "Intervalo de Frequência (%)",
    min_value=int(df["Frequência (%)"].min()),
    max_value=int(df["Frequência (%)"].max()),
    value=(int(df["Frequência (%)"].min()), int(df["Frequência (%)"].max()))
)

filtered_df2 = df[
    (df["Uso de Recursos Institucionais (%)"] >= uso_recursos_min) &
    (df["Uso de Recursos Institucionais (%)"] <= uso_recursos_max) &
    (df["Frequência (%)"] >= frequencia_min) &
    (df["Frequência (%)"] <= frequencia_max)
]

scatter_fig2 = px.scatter(
    filtered_df2,
    x="Uso de Recursos Institucionais (%)",
    y="Desempenho Acadêmico",
    color="Abandono",
    title="Desempenho Acadêmico Médio por Uso de Recursos e Frequência"
)
st.plotly_chart(scatter_fig2)

# 5. Gráfico de Barras: Condição Socioeconômica vs. Status de Emprego
st.header("Condição Socioeconômica vs. Status de Emprego")
socio_emprego_bar = px.bar(
    df,
    x="Condição Socioeconômica",
    color="Status de Emprego",
    barmode="group",
    title="Distribuição de Condição Socioeconômica por Status de Emprego"
)
st.plotly_chart(socio_emprego_bar)

# Layout de colunas para os gráficos
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(scatter_fig)
    st.plotly_chart(satisfacao_pie)
    st.plotly_chart(socio_emprego_bar)

with col2:
    st.plotly_chart(abandono_histogram)
    st.plotly_chart(scatter_fig2)