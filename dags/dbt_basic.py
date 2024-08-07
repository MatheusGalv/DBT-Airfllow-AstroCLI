from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import os

DBT_PROJECT_DIR = os.getenv("DBT_PROJECT_DIR", "/usr/local/airflow/dbt")


with DAG(
    dag_id="dbt_basic_dag",
    start_date=datetime(2024, 8, 5),
    description="A sample Airflow DAG for dbt",
    schedule_interval="@daily",
    catchup=False,
) as dag:

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"dbt run --profiles-dir {DBT_PROJECT_DIR} --project-dir {DBT_PROJECT_DIR}",
    )


    dbt_run
