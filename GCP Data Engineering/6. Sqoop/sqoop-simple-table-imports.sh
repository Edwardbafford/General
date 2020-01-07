#!/bin/bash

bucket="gs://louie-etl"

pwd_file=$bucket/sqoop-pwd/pwd.txt

cluster_name="ephemeral-spark-cluster-20190518"

table_name="flights"

target_dir=$bucket/sqoop_output


gcloud dataproc jobs submit hadoop \
--cluster=$cluster_name \
--class=org.apache.sqoop.Sqoop \
--jars=$bucket/sqoop_jars/sqoop_sqoop-1.4.7.jar,$bucket/sqoop_jars/sqoop_avro-tools-1.8.2.jar,file:///usr/share/java/mysql-connector-java-5.1.42.jar \
-- import \
-Dmapreduce.job.classloader=true \
-Dmapreduce.output.basename="part.20190514_" \
--driver com.mysql.jdbc.Driver \
--connect="jdbc:mysql://localhost:3307/airports" \
--username=root --password-file=$pwd_file \
--split-by id \
--table $table_name \
--boundary-query "select 1,190751" \
-m 4 \
--warehouse-dir $target_dir --as-avrodatafile


