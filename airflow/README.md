## Airflow
### Setup
Install docker  
Setup environment variables - EMAIL, EMAIL_PASSWORD  
Within windows powershell  
`docker run -d --rm -e DATA=/usr/local/airflow -e AIRFLOW__SMTP__SMTP_HOST=smtp.office365.com -e AIRFLOW__SMTP__SMTP_PORT=587 -e AIRFLOW__SMTP__SMTP_USER=$env:EMAIL -e AIRFLOW__SMTP__SMTP_PASSWORD=$env:EMAIL_PASSWORD -e AIRFLOW__SMTP__SMTP_MAIL_FROM=$env:EMAIL -p 8081:8080 -v C:\Users\lbafford\Repos\Personal\General\airflow\dags:/usr/local/airflow/dags puckel/docker-airflow webserver`
