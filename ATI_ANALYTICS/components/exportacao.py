import streamlit as st


def exportar(df):

    csv = df.to_csv(

        index=False,

        encoding="utf-8-sig"

    ).encode("utf-8-sig")

    st.download_button(

        "⬇ Exportar CSV",

        csv,

        "atendimentos.csv",

        "text/csv"

    )