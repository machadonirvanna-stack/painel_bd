import streamlit as st
import plotly.express as px

from database import carregar_atendimentos
from components.filtros import aplicar_filtros

st.title("Tendências")

df = carregar_atendimentos()

df = aplicar_filtros(df)

serie = (

    df.groupby(

        df["data_agendada"].dt.to_period("M")

    )

    .size()

    .reset_index(name="Atendimentos")

)

serie["Mes"] = serie["data_agendada"].astype(str)

serie["Media3"] = (

    serie["Atendimentos"]

    .rolling(3)

    .mean()

)

serie["Media6"] = (

    serie["Atendimentos"]

    .rolling(6)

    .mean()

)

fig = px.line(

    serie,

    x="Mes",

    y=[

        "Atendimentos",

        "Media3",

        "Media6"

    ],

    markers=True

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

crescimento = serie.copy()

crescimento["Variacao"] = (

    crescimento["Atendimentos"]

    .pct_change()

    *100

)

fig = px.bar(

    crescimento,

    x="Mes",

    y="Variacao",

    color="Variacao",

    text="Variacao"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

st.dataframe(

    crescimento,

    use_container_width=True,

    hide_index=True

)