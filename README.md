# Automated Crypto ETL Pipeline

A lightweight, production-grade Data Engineering pipeline that automatically extracts live cryptocurrency metrics, transforms unstructured payloads into tabular formats, and loads the data into a relational database. The entire ecosystem is containerized and orchestrated natively via Linux system daemons.

## Architecture Overview

The system operates on an automated, headless hourly schedule:
1. **Extract**: Ingests real-time asset prices (Bitcoin & Ethereum) from the CoinGecko REST API.
2. **Transform**: Normalizes nested JSON payloads into a structured schema, engineering explicit `timestamp`, `coin_id`, and `price_usd` elements using `Pandas`.
3. **Load**: Appends clean transactional data to a local SQLite database utilizing `SQLAlchemy`.
4. **Infrastructure & Automation**: The execution context is containerized with `Podman`/`Docker` and automatically orchestrated every hour using Linux `systemd` user timers, persisting data cleanly across host-container boundaries.

---

## Tech Stack

* **Language:** Python 3.11
* **Data Processing:** Pandas, SQLAlchemy, Requests
* **Database:** SQLite
* **Containerization:** Podman / Docker (utilizing SELinux volume context management)
* **Orchestration:** Linux systemd (User Services & Timers)

---

## Project Structure

```text
coiny/
├── pipeline.py              # Main ETL script (Extract, Transform, Load)
├── check_db.py               # Database verification utility script
├── Dockerfile                # Multi-layer container build blueprint
├── requirements.txt          # Python dependency freeze
├── .env                      # Local environment secrets (API Keys)
└── .gitignore                # Protects secrets and local DB files from VCS