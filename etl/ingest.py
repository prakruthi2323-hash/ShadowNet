from sqlalchemy import create_engine
import pandas as pd

# Connect PostgreSQL
engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/shadownet"
)

# Read CSV file
df = pd.read_csv("datasets/firewall_logs.csv")

# Insert into PostgreSQL
df.to_sql(
    "firewall_logs",
    engine,
    if_exists="replace",
    index=False
)

print("New firewall logs inserted successfully!")