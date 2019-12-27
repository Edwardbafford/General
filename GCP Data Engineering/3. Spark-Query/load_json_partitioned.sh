bucket=gs://louie-etl

current_date=$(date +"%Y-%m-%d" -d "+1 days")

bq load --source_format=NEWLINE_DELIMITED_JSON \
 data_analysis.avg_delays_by_distance \
 $bucket/output/${current_date}"_distance_category/*.json" &&

bq load --source_format=NEWLINE_DELIMITED_JSON \
 data_analysis.avg_delays_by_flight_nums \
 $bucket/output/${current_date}"_flight_nums/*.json"
