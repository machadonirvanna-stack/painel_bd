# ATI Analytics

Dashboard analítico desenvolvido em Streamlit para acompanhamento das atividades de Assessoria Técnica Independente (ATI).

## Objetivo

Centralizar indicadores operacionais e estratégicos a partir dos dados sincronizados do MongoDB para PostgreSQL, permitindo análises sobre:

- Atendimentos
- Agenda
- Assessores
- Comunidades
- Assuntos
- Metas
- Tendências

## Tecnologias

- Python 3.12+
- Streamlit
- PostgreSQL
- SQLAlchemy
- Pandas
- Plotly

## Estrutura

```
ATI_ANALYTICS/
│
├── app.py
├── database.py
├── requirements.txt
├── pages/
├── components/
├── assets/
├── sql/
└── README.md
```

## Arquitetura

```
MongoDB
    │
    ▼
PostgreSQL (public)
    │
    ▼
Schema analytics
    ├── tabelas normalizadas
    ├── dimensões
    ├── fatos
    └── views
    │
    ▼
Streamlit
```

## Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
cd ATI_ANALYTICS
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env`:

```env
DATABASE_URL=postgresql://usuario:senha@host:porta/database
```

Execute o projeto:

```bash
streamlit run app.py
```

## Status

Projeto em desenvolvimento.

A estrutura analítica está sendo migrada para um schema dedicado (`analytics`), desacoplando o dashboard das tabelas operacionais e centralizando toda a lógica de negócio no PostgreSQL.
