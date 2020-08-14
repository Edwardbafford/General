import os
import random
from datetime import datetime

from airflow import DAG
from airflow.utils.email import send_email
from airflow.operators.python_operator import PythonOperator


def save_number(number):
    data_dir = os.getenv('DATA')
    with open(data_dir + '/number_file.txt', 'w') as number_file:
        number_file.write(str(number))


def email_callback(**kwargs):
    data_dir = os.getenv('DATA')
    with open(data_dir + '/number_file.txt', 'r') as number_file:
        content = number_file.read()
    send_email(
        to=['edwardbafford@go.rmc.edu'],
        subject='Airflow Email',
        html_content=content,

    )


default_args = {
    'owner': 'Louie',
    'start_date': datetime(2020, 8, 14),
    'schedule_interval': '@hourly',
    'email': ['edwardbafford@go.rmc.edu'],
    'retries': 0
}

dag = DAG('PythonEmail', default_args=default_args)

save_number_task = PythonOperator(
    task_id='save_number',
    python_callable=save_number,
    op_kwargs={'number': random.random()},
    dag=dag,
)


email_task = PythonOperator(
    task_id='email_callback',
    python_callable=email_callback,
    provide_context=True,
    dag=dag,
)

save_number_task >> email_task
