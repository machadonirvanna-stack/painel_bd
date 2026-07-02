import streamlit as st
import plotly.express as px

from database import carregar_atendimentos
from database import carregar_assessores

from components.filtros import aplicar_filtros

st.title("Assessores")

df = carregar_atendimentos()

assessores = carregar_assessores()

df = aplicar_filtros(df)

st.subheader("Equipe")

st.metric(
    "Total de Assessores",
    len(assessores)
)

st.divider()

extras = (
    df["qtd_assessores_extras"]
    .fillna(0)
    .sum()
)

st.metric(
    "Assessores Extras",
    int(extras)
)

st.divider()

fig = px.histogram(
    df,
    x="qtd_assessores_extras"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("Cadastro")

st.dataframe(
    assessores,
    use_container_width=True,
    hide_index=True
)