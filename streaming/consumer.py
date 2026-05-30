from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'cyber_events',
    bootstrap_servers='host.docker.internal:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for events...")

for message in consumer:
    print("Received:", message.value)