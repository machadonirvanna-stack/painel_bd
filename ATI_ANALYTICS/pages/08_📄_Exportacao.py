import streamlit as st

from database import carregar_atendimentos

from components.filtros import aplicar_filtros

from components.exportacao import exportar

st.title("Exportação")

df = carregar_atendimentos()

df = aplicar_filtros(df)

st.metric(

    "Registros",

    len(df)

)

st.divider()

st.dataframe(

    df,

    use_container_width=True,

    hide_index=True

)

st.divider()

exportar(df)