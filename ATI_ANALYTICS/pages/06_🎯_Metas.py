import streamlit as st
import plotly.express as px

from database import carregar_atendimentos
from components.filtros import aplicar_filtros

st.title("Metas")

df = carregar_atendimentos()
df = aplicar_filtros(df)

st.subheader("Resumo")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Meta Média",
    f"{df['percentual_meta_atingida'].mean():.1f}%"
)

c2.metric(
    "Atividades",
    int(df["atividade_realizada"].sum())
)

c3.metric(
    "Pendentes",
    int(
        df["atividades_nao_concluidas_eixo"].sum()
    )
)

c4.metric(
    "Horas",
    f"{df['duracao_planejada_horas'].sum():.1f}"
)

st.divider()

eixos = (

    df.groupby("eixo")

    .agg(

        Meta=("percentual_meta_atingida","mean"),

        Realizadas=("atividade_realizada","sum"),

        Total=("atividades_totais_eixo","max")

    )

    .reset_index()

)

fig = px.bar(

    eixos,

    x="Meta",

    y="eixo",

    orientation="h",

    color="Meta",

    text="Meta"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

fig = px.scatter(

    eixos,

    x="Realizadas",

    y="Meta",

    size="Total",

    hover_name="eixo"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.dataframe(
    eixos,
    use_container_width=True,
    hide_index=True
)