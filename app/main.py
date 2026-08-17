import hashlib
import re

from fastapi import FastAPI
from pydantic import BaseModel, Field


class LogEvent(BaseModel):
    service: str = Field(min_length=1, max_length=80)
    level: str = "ERROR"
    message: str = Field(min_length=3, max_length=4_000)


class Incident(BaseModel):
    fingerprint: str
    service: str
    severity: str
    count: int
    summary: str


def severity(level: str, message: str) -> str:
    text = f"{level} {message}".lower()
    if any(word in text for word in ("outage", "database down", "data loss", "critical")):
        return "critical"
    if level.upper() in {"ERROR", "FATAL"} or any(word in text for word in ("timeout", "failed")):
        return "high"
    if level.upper() == "WARNING":
        return "medium"
    return "low"


def create_app() -> FastAPI:
    app = FastAPI(title="IncidentHub", version="0.1.0")
    incidents: dict[str, Incident] = {}

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok", "service": "incident-hub"}

    @app.post("/api/v1/logs", response_model=Incident)
    async def ingest_log(event: LogEvent) -> Incident:
        normalized = re.sub(r"\d+", "#", event.message.lower())
        fingerprint = hashlib.sha256(normalized.encode()).hexdigest()[:12]
        current = incidents.get(fingerprint)
        if current:
            current.count += 1
            return current
        current = Incident(
            fingerprint=fingerprint,
            service=event.service,
            severity=severity(event.level, event.message),
            count=1,
            summary=event.message[:160],
        )
        incidents[fingerprint] = current
        return current

    @app.get("/api/v1/incidents", response_model=list[Incident])
    async def list_incidents() -> list[Incident]:
        return sorted(incidents.values(), key=lambda item: item.count, reverse=True)

    return app


app = create_app()
