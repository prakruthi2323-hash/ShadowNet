import pandas as pd
import random
from faker import Faker

fake = Faker()

cloud_providers = [
    "AWS",
    "Azure",
    "Google Cloud"
]

event_types = [
    "Unauthorized Access",
    "IAM Abuse",
    "Data Exposure",
    "Misconfigured Storage",
    "Suspicious Login"
]

severity_levels = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

data = []

# Generate 1000 cloud events
for i in range(1000):

    row = {
        "cloud_event_id": i + 1,
        "cloud_provider": random.choice(cloud_providers),
        "event_type": random.choice(event_types),
        "affected_resource": fake.hostname(),
        "severity": random.choice(severity_levels),
        "region": fake.country(),
        "timestamp": fake.date_time_this_year()
    }

    data.append(row)

# Convert dataframe
df = pd.DataFrame(data)

# Save CSV
df.to_csv(
    "datasets/cloud_logs.csv",
    index=False
)

print("Cloud logs dataset generated successfully!")