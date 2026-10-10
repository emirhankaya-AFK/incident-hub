# Incident Hub

## English

**Purpose**  
A production‑shaped FastAPI service that ingests application logs, assigns severity, and groups recurring incidents with stable SHA‑256 fingerprints.

**Verified features**  
- `POST /api/v1/logs` – validates and ingests a structured log event.  
- `GET /api/v1/incidents` – lists grouped incidents and occurrence counts.  
- SHA‑256 fingerprint generation for deduplication.  
- Automated tests (`pytest`).  
- Docker Compose configuration.  
- GitHub Actions CI workflow.

**Stack**  
- FastAPI (Python)  
- Docker & Docker Compose  
- GitHub Actions (CI)  
- pytest (testing)

**Setup & usage**  
```bash
# Install dependencies (including dev extras)
pip install -e ".[dev]"

# Run the API locally with hot reload
uvicorn app.main:app --reload

# Run the test suite
pytest -q

# Or start everything with Docker
docker compose up --build
```
API documentation is available at http://localhost:8000/docs.

**Limitations**  
- The MVP uses in‑memory storage; data is lost when the process stops.  
- No persistence layer, authentication, alerting, or retention policies are included.  
- Production‑grade adapters (e.g., PostgreSQL/Redis) would need to be added.

**License**  
See the `LICENSE` file for licensing information.

## Türkçe

**Amaç**  
Uygulama günlüklerini alıp, şiddetini belirleyerek ve yinelenen olayları kararlı SHA‑256 parmak izleriyle gruplayan üretime uygun bir FastAPI hizmeti.

**Doğrulanmış özellikler**  
- `POST /api/v1/logs` – yapılandırılmış bir günlük olayını doğrular ve alır.  
- `GET /api/v1/incidents` – gruplanmış olayları ve oluşum sayılarını listeler.  
- SHA‑256 parmak izi üretimiyle tekrarlanan olayların tespiti.  
- Otomatik testler (`pytest`).  
- Docker Compose yapılandırması.  
- GitHub Actions CI iş akışı.

**Yığın**  
- FastAPI (Python)  
- Docker & Docker Compose  
- GitHub Actions (CI)  
- pytest (test)

**Kurulum ve kullanım**  
```bash
# Bağımlılıkları (dev ekstralarıyla) yükle
pip install -e ".[dev]"

# Yerel API'yi hot reload ile çalıştır
uvicorn app.main:app --reload

# Test paketini çalıştır
pytest -q

# Ya da Docker ile tümünü başlat
docker compose up --build
```
API dokümantasyonu http://localhost:8000/docs adresinde mevcuttur.

**Sınırlamalar**  
- MVP bellek içi depolama kullanır; süreç durduğunda veri kaybolur.  
- Kalıcı depolama, kimlik doğrulama, uyarı veya bekletme politikası bulunmaz.  
- Üretim seviyesinde adaptörler (PostgreSQL/Redis vb.) eklenmelidir.

**Lisans**  
Lisans bilgisi için `LICENSE` dosyasına bakınız.

## Deutsch

**Zweck**  
Ein produktionsgerechter FastAPI‑Dienst, der Anwendungs‑Logs aufnimmt, deren Schweregrad einstuft und wiederkehrende Vorfälle mit stabilen SHA‑256‑Fingerprints gruppiert.

**Verifizierte Funktionen**  
- `POST /api/v1/logs` – validiert und nimmt ein strukturiertes Log‑Ereignis entgegen.  
- `GET /api/v1/incidents` – listet gruppierte Vorfälle und deren Vorkommen auf.  
- SHA‑256‑Fingerprint‑Generierung zur Deduplizierung.  
- Automatisierte Tests (`pytest`).  
- Docker‑Compose‑Konfiguration.  
- GitHub‑Actions‑CI‑Workflow.

**Stack**  
- FastAPI (Python)  
- Docker & Docker Compose  
- GitHub Actions (CI)  
- pytest (Testing)

**Einrichtung & Nutzung**  
```bash
# Abhängigkeiten (inkl. dev‑Extras) installieren
pip install -e ".[dev]"

# API lokal mit Hot‑Reload starten
uvicorn app.main:app --reload

# Testsuite ausführen
pytest -q

# Oder alles mit Docker starten
docker compose up --build
```
Die API‑Dokumentation ist unter http://localhost:8000/docs erreichbar.

**Einschränkungen**  
- Der MVP nutzt In‑Memory‑Speicher; Daten gehen beim Beenden des Prozesses verloren.  
- Es besteht keine Persistenz, Authentifizierung, Alerting oder Aufbewahrungsrichtlinie.  
- Für produktive Einsätze müssen Adapter (z. B. PostgreSQL/Redis) hinzugefügt werden.

**Lizenz**  
Siehe die `LICENSE` Datei für Lizenzinformationen.
