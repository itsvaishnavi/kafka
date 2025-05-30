# consumer.py
from kafka import KafkaConsumer
import json
import os

DATA_FILE = 'data.json'

consumer = KafkaConsumer(
    'weather-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer started...")

for message in consumer:
    data = message.value
    print("Received:", data)

    # Append new data to a file (you could use a DB for scale)
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            all_data = json.load(f)
    else:
        all_data = []

    all_data.append(data)

    with open(DATA_FILE, 'w') as f:
        json.dump(all_data, f)
