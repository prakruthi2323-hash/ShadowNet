import pandas as pd
import random
from faker import Faker

fake = Faker()

threat_types = [
    "Phishing",
    "Spam",
    "Spoofing",
    "Malicious Attachment",
    "Business Email Compromise"
]

severity_levels = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

actions = [
    "Blocked",
    "Delivered",
    "Quarantined"
]

data = []

# Generate 1000 email threat events
for i in range(1000):

    row = {
        "email_event_id": i + 1,
        "sender_email": fake.email(),
        "receiver_email": fake.email(),
        "threat_type": random.choice(threat_types),
        "severity": random.choice(severity_levels),
        "action_taken": random.choice(actions),
        "timestamp": fake.date_time_this_year()
    }

    data.append(row)

# Convert dataframe
df = pd.DataFrame(data)

# Save CSV
df.to_csv(
    "datasets/email_threat_logs.csv",
    index=False
)

print("Email threat logs dataset generated successfully!")