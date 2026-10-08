from fastapi import FastAPI
from datetime import datetime, timezone
import socket

app = FastAPI(
    title="Cloud Incident Monitoring Platform",
    description="AWS-based application monitoring and incident management platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "application": "Cloud Incident Monitoring Platform",
        "status": "HEALTHY",
        "message": "Application is running successfully"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "server": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/api/info")
def info():
    return {
        "application": "Cloud Incident Monitoring Platform",
        "environment": "development",
        "version": "1.0.0"
    }