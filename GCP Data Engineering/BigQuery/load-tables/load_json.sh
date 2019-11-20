# Load schema into BigQuery table
bq mk -t --schema schema.json louie_analysis.flight_json

# Load data from bucket into BigQuery table
bq load --source_format=NEWLINE_DELIMITED_JSON louie_analysis.flight_json gs://louie-etl/json/2019-04-27.json


# Schema created at load time
 bq load --source_format=NEWLINE_DELIMITED_JSON --autodetect louie_analysis.flight_json gs://louie-etl/json/2019-04-27.json