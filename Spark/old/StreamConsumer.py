from datetime import datetime
from glob import glob
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kinesis import KinesisUtils, InitialPositionInStream
import argparse
import boto
import json
import os

# Helper functions
def parse_entry(record):
    msg = record['value']
    values = msg.split(';')
    event = values[1].replace('\n', '')
    return {
        'dt': datetime.strptime(
            values[0], '%Y-%m-%d %H:%M:%S.%f'),
        'event': event,
        'timestamp': datetime.strptime(
            record['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
    }

def update_global_event_counts(key_value_pairs):
    def update(new_values, accumulator):
        if accumulator is None:
            accumulator = 0
        return sum(new_values, accumulator)
    return key_value_pairs.updateStateByKey(update)

def aggregate_by_event_type(record):
    return record\
        .map(lambda x: json.loads(x))\
        .map(parse_entry)\
        .map(lambda record: (record['event'], 1))\
        .reduceByKey(lambda a, b: a+b)

endpoint = 'https://kinesis.us-west-2.amazonaws.com/'

stream_context = StreamingContext(sc, 1)

sc.setLogLevel("INFO")
stream = KinesisUtils.createStream(stream_context, 'EventLKinesisConsumer', 'spark-practice', endpoint,'us-west-2', InitialPositionInStream.LATEST, 1)

# counts number of events
event_counts = aggregate_by_event_type(stream)
global_counts = update_global_event_counts(event_counts)
global_counts.pprint()

# Sends data to S3
global_counts.foreachRDD(lambda rdd: send_record(rdd, 'spark-processed-357'))
stream_context.start()
stream_context.awaitTerminationOrTimeout()
stream_context.stop()

