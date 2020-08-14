## Airflow
### Setup
`docker run -d --rm -e DATA=/usr/local/airflow -e AIRFLOW__SMTP__SMTP_HOST=smtp.office365.com -e AIRFLOW__SMTP__SMTP_PORT=587 -e AIRFLOW__SMTP__SMTP_USER=EMAIL -e AIRFLOW__SMTP__SMTP_PASSWORD=PASSWORD -e AIRFLOW__SMTP__SMTP_MAIL_FROM=EMAIL -p 8081:8080 -v C:\Users\lbafford\Repos\Personal\General\airflow\dags:/usr/local/airflow/dags puckel/docker-airflow webserver`
