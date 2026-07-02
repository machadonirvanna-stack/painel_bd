import streamlit as st
import plotly.express as px

from database import carregar_atendimentos
from components.filtros import aplicar_filtros

st.title("Assuntos")

df = carregar_atendimentos()

df = aplicar_filtros(df)

assuntos = (
    df.groupby(
        [
            "eixo",
            "categoria",
            "assunto_assessoramento"
        ]
    )
    .agg(
        Atendimentos=("codigo_atendimento","count"),
        Meta=("percentual_meta_atingida","mean"),
        Horas=("duracao_planejada_horas","sum")
    )
    .reset_index()
)

st.metric(
    "Assuntos",
    assuntos.shape[0]
)

st.divider()

fig = px.treemap(
    assuntos,
    path=[
        "eixo",
        "categoria",
        "assunto_assessoramento"
    ],
    values="Atendimentos",
    color="Meta"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

fig = px.sunburst(
    assuntos,
    path=[
        "eixo",
        "categoria",
        "assunto_assessoramento"
    ],
    values="Atendimentos"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

fig = px.bar(
    assuntos.sort_values(
        "Horas",
        ascending=False
    ).head(20),
    x="Horas",
    y="assunto_assessoramento",
    orientation="h",
    color="Meta"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.dataframe(
    assuntos,
    use_container_width=True,
    hide_index=True
)