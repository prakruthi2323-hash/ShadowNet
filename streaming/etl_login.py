import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("datasets/login_activity_logs.csv")

engine = create_engine(
"postgresql://neondb_owner:npg_cFmL34EogaeS@ep-restless-shadow-ap1d1q9u-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

df.to_sql(
"fact_login_activity_logs",
engine,
if_exists="append",
index=False
)

print("ETL Completed")