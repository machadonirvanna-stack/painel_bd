import plotly.express as px
import streamlit as st


def barras(df, coluna):

    dados = (
        df[coluna]
        .value_counts()
        .reset_index()
    )

    dados.columns = [coluna, "Quantidade"]

    fig = px.bar(
        dados,
        x="Quantidade",
        y=coluna,
        orientation="h",
        text="Quantidade",
        color="Quantidade"
    )

    fig.update_layout(
        height=420,
        showlegend=False,
        margin=dict(
            l=10,
            r=10,
            t=20,
            b=10
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def linha_mensal(df):

    dados = (
        df
        .groupby(
            df["data_agendada"].dt.to_period("M")
        )
        .size()
        .reset_index(name="Quantidade")
    )

    dados["Mês"] = dados["data_agendada"].astype(str)

    fig = px.line(
        dados,
        x="Mês",
        y="Quantidade",
        markers=True
    )

    fig.update_layout(
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def pizza(df, coluna):

    dados = (
        df[coluna]
        .value_counts()
        .reset_index()
    )

    dados.columns = [coluna, "Quantidade"]

    fig = px.pie(
        dados,
        names=coluna,
        values="Quantidade",
        hole=.55
    )

    fig.update_layout(
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def treemap(df):

    dados = (
        df.groupby(
            [
                "eixo",
                "categoria",
                "assunto_assessoramento"
            ]
        )
        .size()
        .reset_index(name="Quantidade")
    )

    fig = px.treemap(
        dados,
        path=[
            "eixo",
            "categoria",
            "assunto_assessoramento"
        ],
        values="Quantidade",
        color="Quantidade"
    )

    fig.update_layout(
        height=600
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )