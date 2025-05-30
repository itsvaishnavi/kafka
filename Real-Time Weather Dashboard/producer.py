# producer.py
import requests
import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

API_KEY = 'api-key'
CITY = 'city'
TOPIC = 'weather-data'

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

while True:
    weather = get_weather()
    if 'main' in weather:
        data = {
            'city': CITY,
            'temp': weather['main']['temp'],
            'humidity': weather['main']['humidity'],
            'condition': weather['weather'][0]['description'],
            'timestamp': weather['dt']
        }
        producer.send(TOPIC, value=data)
        print(f"Sent: {data}")
    time.sleep(60)  # Fetch every minute
