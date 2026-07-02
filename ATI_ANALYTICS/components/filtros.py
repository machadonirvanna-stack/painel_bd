import streamlit as st
import pandas as pd


def aplicar_filtros(df: pd.DataFrame):

    st.sidebar.header("🔎 Filtros")

    # -----------------------------
    # Período
    # -----------------------------

    data_min = df["data_agendada"].min().date()
    data_max = df["data_agendada"].max().date()

    periodo = st.sidebar.date_input(
        "Período",
        value=(data_min, data_max),
        min_value=data_min,
        max_value=data_max,
    )

    # -----------------------------
    # Tipo
    # -----------------------------

    tipos = sorted(df["tipo_agenda"].dropna().unique())

    tipo = st.sidebar.multiselect(
        "Tipo de agenda",
        tipos,
        default=tipos
    )

    # -----------------------------
    # Status
    # -----------------------------

    status = sorted(df["status"].dropna().unique())

    status_sel = st.sidebar.multiselect(
        "Status",
        status,
        default=status
    )

    # -----------------------------
    # Comunidade
    # -----------------------------

    comunidades = sorted(df["comunidade_origem"].dropna().unique())

    comunidade = st.sidebar.multiselect(
        "Comunidade",
        comunidades
    )

    # -----------------------------
    # Assunto
    # -----------------------------

    assuntos = sorted(df["assunto_assessoramento"].dropna().unique())

    assunto = st.sidebar.multiselect(
        "Assunto",
        assuntos
    )

    # -----------------------------
    # Origem
    # -----------------------------

    origens = sorted(df["origem_solicitacao"].dropna().unique())

    origem = st.sidebar.multiselect(
        "Origem",
        origens
    )

    # -----------------------------
    # Formato
    # -----------------------------

    formatos = sorted(df["formato_acompanhamento"].dropna().unique())

    formato = st.sidebar.multiselect(
        "Formato",
        formatos
    )

    # -----------------------------
    # Categoria
    # -----------------------------

    categorias = sorted(df["categoria"].dropna().unique())

    categoria = st.sidebar.multiselect(
        "Categoria",
        categorias
    )

    # -----------------------------
    # Eixo
    # -----------------------------

    eixos = sorted(df["eixo"].dropna().unique())

    eixo = st.sidebar.multiselect(
        "Eixo",
        eixos
    )

    # -----------------------------
    # Pesquisa
    # -----------------------------

    pesquisa = st.sidebar.text_input(
        "Pesquisar assunto ou comunidade"
    )

    f = df.copy()

    if len(periodo) == 2:
        inicio, fim = periodo

        f = f[
            (f["data_agendada"].dt.date >= inicio)
            &
            (f["data_agendada"].dt.date <= fim)
        ]

    if tipo:
        f = f[f["tipo_agenda"].isin(tipo)]

    if status_sel:
        f = f[f["status"].isin(status_sel)]

    if comunidade:
        f = f[f["comunidade_origem"].isin(comunidade)]

    if assunto:
        f = f[f["assunto_assessoramento"].isin(assunto)]

    if origem:
        f = f[f["origem_solicitacao"].isin(origem)]

    if formato:
        f = f[f["formato_acompanhamento"].isin(formato)]

    if categoria:
        f = f[f["categoria"].isin(categoria)]

    if eixo:
        f = f[f["eixo"].isin(eixo)]

    if pesquisa:

        texto = pesquisa.lower()

        f = f[
            f["assunto_assessoramento"].fillna("").str.lower().str.contains(texto)
            |
            f["comunidade_origem"].fillna("").str.lower().str.contains(texto)
        ]

    return f