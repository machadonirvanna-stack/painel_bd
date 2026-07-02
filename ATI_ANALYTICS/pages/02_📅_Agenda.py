import streamlit as st
import plotly.express as px
import pandas as pd

from database import carregar_atendimentos
from components.filtros import aplicar_filtros

st.title("Agenda")

df = carregar_atendimentos()
df = aplicar_filtros(df)

st.subheader("Agenda por mês")

mensal = (
    df.groupby(df["data_agendada"].dt.to_period("M"))
    .size()
    .reset_index(name="Quantidade")
)

mensal["Mês"] = mensal["data_agendada"].astype(str)

fig = px.bar(
    mensal,
    x="Mês",
    y="Quantidade",
    text="Quantidade"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

c1, c2 = st.columns(2)

with c1:

    st.subheader("Dias da semana")

    dias = df.copy()

    dias["Dia"] = dias["data_agendada"].dt.day_name()

    ordem = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    dias["Dia"] = pd.Categorical(
        dias["Dia"],
        ordem,
        ordered=True
    )

    dias = (
        dias.groupby("Dia")
        .size()
        .reset_index(name="Quantidade")
    )

    fig = px.bar(
        dias,
        x="Dia",
        y="Quantidade",
        text="Quantidade"
    )

    st.plotly_chart(fig, use_container_width=True)

with c2:

    st.subheader("Horários")

    horas = (
        df["hora_agendada"]
        .value_counts()
        .reset_index()
    )

    horas.columns = [
        "Hora",
        "Quantidade"
    ]

    fig = px.bar(
        horas,
        x="Hora",
        y="Quantidade",
        text="Quantidade"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Agenda")

st.dataframe(
    df[
        [
            "data_agendada",
            "hora_agendada",
            "tipo_agenda",
            "comunidade_origem",
            "assunto_assessoramento",
            "status"
        ]
    ],
    use_container_width=True,
    hide_index=True
)