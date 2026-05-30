import pandas as pd
import random
from faker import Faker

fake = Faker()

threat_types = [
    "Leaked Credentials",
    "Stolen Credit Cards",
    "Data Leak",
    "Hacker Forum Mention",
    "Compromised Accounts"
]

platforms = [
    "Telegram",
    "Dark Forum",
    "Marketplace",
    "Deep Web Chat"
]

severity_levels = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

data = []

# Generate 1000 dark web events
for i in range(1000):

    row = {
        "darkweb_event_id": i + 1,
        "threat_type": random.choice(threat_types),
        "source_platform": random.choice(platforms),
        "country": fake.country(),
        "severity": random.choice(severity_levels),
        "affected_organization": fake.company(),
        "timestamp": fake.date_time_this_year()
    }

    data.append(row)

# Convert dataframe
df = pd.DataFrame(data)

# Save CSV
df.to_csv(
    "datasets/darkweb_logs.csv",
    index=False
)

print("Dark web logs dataset generated successfully!")