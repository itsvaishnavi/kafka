# consumer.py
from kafka import KafkaConsumer
import sqlite3

# consumer = KafkaConsumer(
#     'test-topic',
#     bootstrap_servers='localhost:9092',
#     auto_offset_reset='earliest',
#     value_deserializer=lambda x: x.decode('utf-16', errors='ignore')  # Decode cleanly
# )

conn = sqlite3.connect('logs.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, log_line TEXT)')
conn.commit()

# for message in consumer:
#     log = message.value.strip()
#     print("Received:", log)
#     c.execute("INSERT INTO logs (log_line) VALUES (?)", (log,))
#     conn.commit()


from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='log-consumer-group'
)

print("Waiting for log messages...\n")
for message in consumer:
    log = message.value.decode('utf-8', errors='ignore')
    print(f"Received: {message.value.decode('utf-8', errors='ignore')}")
    c.execute("INSERT INTO logs (log_line) VALUES (?)", (log,))
    conn.commit()