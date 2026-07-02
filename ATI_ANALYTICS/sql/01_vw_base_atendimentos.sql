CREATE OR REPLACE VIEW analytics.vw_base_atendimentos AS

SELECT

    a._id,

    a.codigo_atendimento,

    a.created_at_json,

    a.updated_at_json,

    a.updated_at_linha,

    a.data_agendada,

    NULLIF(trim(a.hora_agendada), '') AS hora_agendada,

    NULLIF(trim(a.hora_final_agendada), '') AS hora_final_agendada,

    a.status,

    a.tipo_agenda,

    a.formato_acompanhamento,

    a.assunto_assessoramento,

    d.eixo,

    d.categoria,

    d.meta_semestral,

    a.origem_solicitacao,

    a.comunidade_origem,

    a.local,

    a.solicitante,

    a.contato_mobilizacao,

    a.assessores_extras,

    a.qtd_assessores_extras,

    a.descricao_solicitacao,

    CASE
        WHEN a.status = 'CONCLUIDO' THEN 1
        ELSE 0
    END AS atividade_realizada,

    CASE
        WHEN upper(a.formato_acompanhamento) = 'PRESENCIAL' THEN 1
        ELSE 0
    END AS atividade_presencial,

    CASE
        WHEN upper(a.formato_acompanhamento) = 'REMOTO' THEN 1
        ELSE 0
    END AS atividade_remota,

    CASE
        WHEN NULLIF(trim(a.hora_agendada), '') IS NULL
          OR NULLIF(trim(a.hora_final_agendada), '') IS NULL
        THEN NULL

        ELSE ROUND(

            EXTRACT(

                EPOCH FROM

                (

                    NULLIF(trim(a.hora_final_agendada), '')::time

                    -

                    NULLIF(trim(a.hora_agendada), '')::time

                )

            ) / 3600.0

        ,2)

    END AS duracao_planejada_horas

FROM mob.v_atendimentos a

LEFT JOIN mob.dim_metas_atividades d

ON trim(a.assunto_assessoramento)=trim(d.assunto_assessoramento);