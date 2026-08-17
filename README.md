# Incident Hub

[English](README.md) | [Türkçe](README_TR.md)

A production-shaped FastAPI service that ingests application logs, assigns severity, and groups recurring incidents with stable fingerprints.

## Included
- POST /api/v1/logs validates and ingests a structured log event.
- GET /api/v1/incidents lists grouped incidents and occurrence counts.
- SHA-256 fingerprints, tests, Docker and CI.

The MVP uses in-memory storage. Production adapters can add PostgreSQL/Redis, authentication, alerting and retention.

## Run

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

Docker: docker compose up --build. Docs: http://localhost:8000/docs.

