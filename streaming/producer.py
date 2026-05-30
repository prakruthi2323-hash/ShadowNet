from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='host.docker.internal:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

events = [
    {"event_type": "Failed Login Spike", "severity": "High"},
    {"event_type": "Suspicious Country Access", "severity": "Medium"},
    {"event_type": "Brute Force Attempt", "severity": "Critical"},
    {"event_type": "DDoS Spike", "severity": "Critical"},
    {"event_type": "Unauthorized API Request", "severity": "High"},
    {"event_type": "Virus Spread Alert", "severity": "High"},
    {"event_type": "Threat Severity Escalation", "severity": "Critical"}
]

while True:
    event = random.choice(events)

    producer.send("cyber_events", event)
    print("Sent:", event)

    time.sleep(2)