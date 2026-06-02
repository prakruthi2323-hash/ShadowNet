import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine(
    "postgresql://postgres:postgres123@localhost:5432/shadownet"
)

# Extract
df = pd.read_sql(
    "SELECT * FROM firewall_logs",
    engine
)

print("Records Loaded:", len(df))

# Transform
attack_summary = (
    df.groupby("attack_type")
      .size()
      .reset_index(name="attack_count")
)

print(attack_summary)

# Load
attack_summary.to_sql(
    "attack_summary",
    engine,
    if_exists="replace",
    index=False
)

print("ETL Completed Successfully")