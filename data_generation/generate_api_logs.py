import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()

api_types = ["GET", "POST", "PUT", "DELETE"]
status_codes = [200, 201, 400, 401, 403, 404, 500]
threats = ["Normal", "API Abuse", "Token Theft", "Rate Limit Attack"]

data = []

for i in range(1000):
    data.append({
        "api_event_id": i + 1,
        "user_id": random.randint(1000, 9999),
        "api_endpoint": fake.uri_path(),
        "request_type": random.choice(api_types),
        "status_code": random.choice(status_codes),
        "response_time_ms": random.randint(10, 5000),
        "threat_type": random.choice(threats),
        "timestamp": fake.date_time_this_year()
    })

df = pd.DataFrame(data)

df.to_csv("datasets/api_logs.csv", index=False)

print("API logs dataset generated successfully!")