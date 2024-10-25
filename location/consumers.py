from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'location_updates',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    location_data = message.value
    print(f"Received location: {location_data}")
    # Optionally, you can broadcast this to a frontend via WebSocket.
