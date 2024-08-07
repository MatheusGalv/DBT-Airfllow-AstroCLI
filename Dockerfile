FROM quay.io/astronomer/astro-runtime:11.7.0

# install dbt into a venv to avoid package dependency conflicts
# Instale o DBT
RUN pip install dbt-core dbt-postgres

# Copie os arquivos do projeto para o contêiner
COPY . /usr/local/airflow/

# Defina o diretório de trabalho
WORKDIR /usr/local/airflow/