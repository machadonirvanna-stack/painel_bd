import streamlit as st

from database import carregar_atendimentos

from components.filtros import aplicar_filtros

from components.kpis import exibir_kpis

from components.charts import (
    barras,
    linha_mensal,
    pizza,
    treemap
)


st.title("Dashboard Executivo")

df = carregar_atendimentos()

df = aplicar_filtros(df)

exibir_kpis(df)

st.divider()

c1, c2 = st.columns(2)

with c1:

    st.subheader("Evolução Mensal")

    linha_mensal(df)

with c2:

    st.subheader("Tipo de Agenda")

    pizza(df, "tipo_agenda")

st.divider()

c1, c2 = st.columns(2)

with c1:

    st.subheader("Status")

    barras(df, "status")

with c2:

    st.subheader("Formato")

    barras(df, "formato_acompanhamento")

st.divider()

c1, c2 = st.columns(2)

with c1:

    st.subheader("Comunidades")

    barras(df, "comunidade_origem")

with c2:

    st.subheader("Origem da Solicitação")

    barras(df, "origem_solicitacao")

st.divider()

st.subheader("Mapa Temático")

treemap(df)

st.divider()

st.subheader("Dados")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)