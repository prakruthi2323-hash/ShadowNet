import pandas as pd
from faker import Faker
import random

fake = Faker()

data = []

attack_types = [
    "DDoS",
    "Malware",
    "SQL Injection",
    "Phishing",
    "Brute Force"
]

threat_levels = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

protocols = [
    "TCP",
    "UDP",
    "HTTP",
    "HTTPS"
]

actions = [
    "Blocked",
    "Allowed",
    "Monitored"
]

# Generate 1000 firewall logs
for i in range(1000):

    row = {
        "event_id": i + 1,
        "source_ip": fake.ipv4(),
        "destination_ip": fake.ipv4(),
        "port_number": random.randint(1, 65535),
        "attack_type": random.choice(attack_types),
        "threat_level": random.choice(threat_levels),
        "country": fake.country(),
        "protocol": random.choice(protocols),
        "action_taken": random.choice(actions),
        "timestamp": fake.date_time_this_year()
    }

    data.append(row)

# Convert into dataframe
df = pd.DataFrame(data)

# Save CSV
df.to_csv(
    "datasets/firewall_logs.csv",
    index=False
)

print("1000 firewall logs generated successfully!")
# ---------------- LOGIN ACTIVITY DATASET ----------------

login_data = []

device_types = [
    "Mobile",
    "Laptop",
    "Desktop",
    "Tablet"
]

browsers = [
    "Chrome",
    "Firefox",
    "Edge",
    "Safari"
]

login_statuses = [
    "Success",
    "Failed"
]

mfa_statuses = [
    "Enabled",
    "Disabled"
]

# Generate 1000 login records
for i in range(1000):

    row = {
        "login_id": i + 1,
        "user_id": random.randint(1000, 9999),
        "login_location": fake.country(),
        "device_type": random.choice(device_types),
        "browser": random.choice(browsers),
        "failed_attempts": random.randint(0, 5),
        "login_status": random.choice(login_statuses),
        "mfa_status": random.choice(mfa_statuses),
        "timestamp": fake.date_time_this_year()
    }

    login_data.append(row)

# Convert dataframe
login_df = pd.DataFrame(login_data)

# Save CSV
login_df.to_csv(
    "datasets/login_activity_logs.csv",
    index=False
)

print("Login activity dataset generated successfully!")