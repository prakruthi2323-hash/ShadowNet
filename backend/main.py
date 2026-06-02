from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI(title="ShadowNet API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PostgreSQL Connection
engine = create_engine(
    "postgresql://postgres:postgres123@localhost:5432/shadownet"
)

# Home
@app.get("/")
def home():
    return {"message": "ShadowNet Cybersecurity API Running"}

# Threat Intelligence
@app.get("/threats")
def get_threats():
    query = """
    SELECT *
    FROM vw_threat_intelligence
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

# User Risk
@app.get("/login-events")
def get_login_events():
    query = """
    SELECT *
    FROM vw_user_risk
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

# API Attacks
@app.get("/api-events")
def get_api_events():
    query = """
    SELECT *
    FROM vw_api_attacks
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

# Cloud Security
@app.get("/cloud-events")
def get_cloud_events():
    query = """
    SELECT *
    FROM vw_cloud_security
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

# Threat Categories
@app.get("/threat-categories")
def threat_categories():
    query = """
    SELECT *
    FROM vw_threat_intelligence
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

@app.get("/malware")
def get_malware():
    query = """
    SELECT *
    FROM vw_malware_intelligence
    """
    
    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")

@app.get("/user-risk")
def user_risk():
    query = """
    SELECT *
    FROM vw_user_risk
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")