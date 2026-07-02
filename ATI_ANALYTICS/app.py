import streamlit as st

from config import Config

st.set_page_config(
    page_title=Config.PAGE_TITLE,
    page_icon=Config.PAGE_ICON,
    layout=Config.LAYOUT,
    initial_sidebar_state="expanded"
)

st.title("ATI Analytics")

st.markdown(
"""
## Painel Analítico

Utilize o menu lateral para acessar os dashboards.
"""
)