import streamlit as st
import plotly.express as px

from database import carregar_atendimentos
from components.filtros import aplicar_filtros

st.title("Comunidades")

df = carregar_atendimentos()

df = aplicar_filtros(df)

ranking = (
    df.groupby("comunidade_origem")
    .agg(
        Atendimentos=("codigo_atendimento","count"),
        Horas=("duracao_planejada_horas","sum"),
        Meta=("percentual_meta_atingida","mean")
    )
    .reset_index()
)

ranking = ranking.sort_values(
    "Atendimentos",
    ascending=False
)

st.metric(
    "Comunidades",
    ranking.shape[0]
)

st.divider()

fig = px.bar(
    ranking,
    x="Atendimentos",
    y="comunidade_origem",
    orientation="h",
    color="Meta"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

fig = px.scatter(
    ranking,
    x="Horas",
    y="Meta",
    size="Atendimentos",
    hover_name="comunidade_origem"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.dataframe(
    ranking,
    use_container_width=True,
    hide_index=True
)