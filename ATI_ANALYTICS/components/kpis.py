import streamlit as st


def card(coluna, titulo, valor, delta=None):

    if delta is None:
        coluna.metric(
            titulo,
            valor
        )
    else:
        coluna.metric(
            titulo,
            valor,
            delta
        )


def exibir_kpis(df):

    total_agendas = len(df)

    atividades_realizadas = int(df["atividade_realizada"].sum())

    atividades_presenciais = int(df["atividade_presencial"].sum())

    atividades_remotas = int(df["atividade_remota"].sum())

    comunidades = df["comunidade_origem"].nunique()

    assuntos = df["assunto_assessoramento"].nunique()

    eixos = df["eixo"].nunique()

    meta = round(df["percentual_meta_atingida"].mean(), 1)

    duracao = round(df["duracao_planejada_horas"].mean(), 1)

    c1, c2, c3, c4 = st.columns(4)

    card(c1, "Atendimentos", f"{total_agendas:,}")

    card(c2, "Realizados", atividades_realizadas)

    card(c3, "Comunidades", comunidades)

    card(c4, "Meta", f"{meta}%")

    c5, c6, c7, c8 = st.columns(4)

    card(c5, "Presenciais", atividades_presenciais)

    card(c6, "Remotos", atividades_remotas)

    card(c7, "Assuntos", assuntos)

    card(c8, "Duração Média", f"{duracao} h")