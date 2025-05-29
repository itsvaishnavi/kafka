from kafka import KafkaProducer
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: v.encode('utf-8')  # Avoid double encoding
)

log_file_path = 'app.log'
topic_name = 'test-topic'

with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
    file.seek(0, 2)  # Go to end of file to start tailing

    while True:
        line = file.readline()
        if not line:
            time.sleep(0.2)
            continue

        # Clean the line
        line = (
            line.replace('\x00', '')  # Remove null bytes
                .replace('\n', '')
                .replace('\r', '')
                .strip()
        )

        if not line:
            continue

        producer.send(topic_name, value=line)
        print(f"Sent: {repr(line)}")
