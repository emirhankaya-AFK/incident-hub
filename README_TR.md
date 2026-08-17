# Incident Hub

[English](README.md) | [Türkçe](README_TR.md)

Uygulama loglarını alan, önem seviyesi belirleyen ve tekrarlanan olayları kararlı parmak iziyle gruplayan üretime yakın FastAPI servisi.

## İçerik
- POST /api/v1/logs yapılandırılmış log alımı ve doğrulama yapar.
- GET /api/v1/incidents grupları ve tekrar sayılarını listeler.
- SHA-256 parmak izi, testler, Docker ve CI.

MVP bellekte çalışır. Üretim adaptöründe PostgreSQL/Redis, kimlik doğrulama, alarm ve saklama politikaları eklenebilir.

## Çalıştırma

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

Docker: docker compose up --build. Dokümantasyon: http://localhost:8000/docs.

