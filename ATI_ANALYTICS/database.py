from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

DATABASE_URL = (
    os.getenv("DATABASE_URL")
    or st.secrets.get("DATABASE_URL")
)

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL não encontrada. Configure no .env (local) ou em Secrets (Streamlit Cloud)."
    )

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
