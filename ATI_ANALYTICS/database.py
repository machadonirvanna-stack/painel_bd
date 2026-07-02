from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

@st.cache_resource
def engine():
    return create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        pool_recycle=300
    )


@st.cache_data(ttl=600)
def carregar_atendimentos():

    sql = """
    SELECT *
    FROM analytics.vw_base_atendimentos
    """

    df = pd.read_sql(sql, engine())

    df["data_agendada"] = pd.to_datetime(
        df["data_agendada"],
        errors="coerce"
    )

    return df


@st.cache_data(ttl=600)
def carregar_assessores():

    sql = """
    SELECT *
    FROM mob.assessores
    """

    return pd.read_sql(sql, engine())