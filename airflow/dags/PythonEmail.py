import os
import random
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator

# Main DAG Definition

default_args = {
    'owner': 'Louie',
    'email': ['edwardbafford@go.rmc.edu'],
    'retries': 0
}

dag = DAG(
    'PythonEmail',
    default_args=default_args,
    schedule_interval='0 * * * *',
    start_date=datetime.now().replace(microsecond=0, second=0, minute=30) - timedelta(hours=1)
)


# Write a number to a file

def save_number(number):
    data_dir = os.getenv('DATA')
    with open(data_dir + '/number_file.txt', 'w') as number_file:
        number_file.write(str(number))


save_number_task = PythonOperator(
    task_id='save_number',
    python_callable=save_number,
    op_kwargs={'number': random.random()},
    dag=dag
)


# Branch based off of number value

def check_number(**kwargs):
    data_dir = os.getenv('DATA')
    with open(data_dir + '/number_file.txt', 'r') as number_file:
        number = float(number_file.read())
    if number >= .5:
        return 'email_high'
    else:
        return 'email_low'


check_number_task = BranchPythonOperator(
    task_id='check_number',
    python_callable=check_number,
    provide_context=True,
    dag=dag
)

# High/Low emails

email_subject = 'Airflow Email'

email_body = """
  Airflow email notification: {{ params.message }}
"""

email_high_task = EmailOperator(
    task_id='email_high',
    to='edwardbafford@go.rmc.edu',
    subject=email_subject,
    html_content=email_body,
    params={'message': 'HIGH NUMBER'},
    dag=dag
)


email_low_task = EmailOperator(
    task_id='email_low',
    to='edwardbafford@go.rmc.edu',
    subject=email_subject,
    html_content=email_body,
    params={'message': 'LOW NUMBER'},
    dag=dag
)

# DAG dependencies

save_number_task >> check_number_task >> [email_high_task, email_low_task]
