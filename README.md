# Smart Office Monitor

## Beskrivelse
Smart Office Monitor er et containeriseret system bygget med Docker og Docker Compose. Systemet simulerer et smart kontormiljø, hvor sensordata genereres automatisk og vises i et dashboard.

Systemet består af flere services:
- Frontend
- Backend
- Sensor-simulator
- PostgreSQL database

Formålet med projektet er at demonstrere containerisering, servicekommunikation, netværkssegmentering og grundlæggende sikkerhed i et moderne IT-system.

## Arkitektur
Systemets overordnede dataflow er:

Browser → Frontend → Backend → PostgreSQL
Sensor-simulator → Backend

### Netværk
Systemet er opdelt i to Docker-netværk:

- public_net
  - frontend
  - backend

- internal_net
  - backend
  - postgres
  - sensor-simulator

Backend fungerer som bro mellem de to netværk.

## Services

### Frontend
Frontend er et simpelt dashboard, der vises i browseren via Nginx.

Frontend kan åbnes på:
http://localhost:8082

### Backend
Backend er lavet i Python med Flask.
Den håndterer API-kald og modtager data fra sensor-simulatoren.

Eksempler på endpoints:
- /api/status
- /api/readings

### Sensor-simulator
Sensor-simulatoren genererer falske sensordata som:
- temperatur
- luftfugtighed
- bevægelse

Den sender data til backend automatisk.

### PostgreSQL
PostgreSQL bruges til at gemme data permanent.

## Sikkerhed
Projektet indeholder flere sikkerhedselementer:

- Minimal base images:
  - python:3.12-slim
  - nginx:alpine
  - postgres:16-alpine

- Begrænset port-eksponering:
  - kun frontend er eksponeret udadtil

- Miljøvariabler i .env

- Netværkssegmentering med public_net og internal_net

- Vulnerability scanning med Trivy

### Trivy scanning
Backend-imaget blev scannet med Trivy.

Resultat:
- Total: 2
- Critical: 0
- High: 0
- Medium: 1
- Low: 1

Der blev ikke fundet nogen critical eller high sårbarheder.

## Krav
For at køre systemet skal følgende være installeret:

- Docker Desktop
- Docker Compose
- Windows PowerShell eller terminal

## Projektstruktur

smart-office-monitor/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       └── main.py
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   └── nginx.conf
├── sensor-simulator/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── simulator.py
├── database/
│   └── init.sql
├── .env
├── docker-compose.yml
└── README.md

## Start systemet
Stå i projektmappen og kør:

docker compose up --build

## Stop systemet
docker compose down

Hvis databasen også skal nulstilles:
docker compose down -v

## Test systemet
Åbn frontend i browseren:
http://localhost:8082

API kan testes via frontend-proxy:
- http://localhost:8082/api/status
- http://localhost:8082/api/readings

## Hvad systemet demonstrerer
Dette projekt demonstrerer:

- Multi-container setup
- Egne Dockerfiles
- Docker Compose
- Frontend/backend arkitektur
- Service-to-service kommunikation
- Docker-netværk og segmentering
- Begrænset port-eksponering
- Miljøvariabler
- Vulnerability scanning med Trivy

## Kendte forbedringer
Mulige fremtidige forbedringer:

- Gemme endnu mere data i PostgreSQL
- Tilføje MQTT broker
- Implementere GitHub Actions
- Deploye løsningen i Kubernetes
- Tilføje mere avanceret sikkerhed
