# Create partitioned BigQuery table with date column partitioning
bq mk -t --schema schema.json --time_partitioning_field flight_date louie_analysis.flight_json_partitioned

# Load data, same with or without partition
bq load --source_format=NEWLINE_DELIMITED_JSON louie_analysis.flight_json_partitioned gs://louie-etl/json/2019-04-27.json
bq load --source_format=NEWLINE_DELIMITED_JSON louie_analysis.flight_json_partitioned gs://louie-etl/json/2019-04-28.json