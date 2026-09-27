# 🌊 FLOODGUARD

## AI-Based Hyper-Local Flash Flood Prediction & Early Warning System for Hilly Regions

> **Predict Earlier • Warn Faster • Respond Smarter**

FLOODGUARD is an AI-powered, GIS-based flash-flood monitoring and early-warning platform designed for vulnerable hilly regions.

The system combines **real-time weather data, IoT sensor data, satellite-derived precipitation, terrain information, historical disaster data, and machine learning** to estimate flood risk at a hyper-local level such as villages, wards, and grid cells.

---

## 🎯 Problem Statement

### Flash Flood Prediction System for Hilly Regions using Multi-Source Data

Hilly regions are highly vulnerable to flash floods because intense rainfall, steep terrain, saturated soil, and rapidly rising water levels can create dangerous conditions with very short warning times.

Existing monitoring approaches may not provide sufficiently localized information for timely preparedness and evacuation.

FLOODGUARD addresses this challenge by combining multiple environmental and geographic data sources into a unified AI-based monitoring and early-warning platform.

---

## 💡 Proposed Solution

FLOODGUARD collects and analyzes:

* 🌧️ Rainfall and weather data
* 💧 Soil moisture
* 🌊 Water level
* ⛰️ Elevation and slope
* 🛰️ Satellite-derived precipitation
* 🛰️ Satellite imagery
* 📍 GIS/location data
* 📚 Historical flood/disaster records
* 📡 IoT sensor measurements

These inputs are processed through a data-fusion and machine-learning pipeline to generate:

* Flood probability
* Dynamic risk score
* Risk level
* Hyper-local risk zones
* Early-warning alerts
* Emergency-response priorities

---

# 🏗️ System Architecture

```text
              ┌─────────────────────┐
              │   Weather Sources   │
              └──────────┬──────────┘
                         │
              ┌──────────▼──────────┐
              │ Satellite Rainfall  │
              └──────────┬──────────┘
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
┌──────▼──────┐   ┌──────▼──────┐   ┌─────▼─────┐
│ IoT Sensors │   │ Satellite   │   │  Terrain  │
│ ESP32/MQTT  │   │  Imagery    │   │ DEM/GIS   │
└──────┬──────┘   └──────┬──────┘   └─────┬─────┘
       │                 │                 │
       └─────────────────┼─────────────────┘
                         │
                ┌────────▼────────┐
                │ Data Ingestion  │
                │ & Validation    │
                └────────┬────────┘
                         │
                ┌────────▼────────┐
                │ Feature         │
                │ Engineering     │
                └────────┬────────┘
                         │
                ┌────────▼────────┐
                │ ML Risk Engine  │
                └────────┬────────┘
                         │
                ┌────────▼────────┐
                │ Flood Probability│
                │ + Risk Score    │
                └────────┬────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
    ┌─────▼─────┐  ┌─────▼─────┐  ┌────▼─────┐
    │ GIS Risk  │  │  Alerts   │  │Emergency │
    │    Map    │  │  Engine   │  │ Response │
    └───────────┘  └───────────┘  └──────────┘
```

---

# 🚀 Key Features

## 🌦️ Real Weather Monitoring

FLOODGUARD can integrate external weather data to monitor:

* Current precipitation
* Hourly precipitation
* Rainfall accumulation
* Temperature
* Humidity
* Atmospheric pressure
* Wind speed
* Precipitation forecast

Rainfall features include:

```text
Rainfall – 15 min
Rainfall – 1 hour
Rainfall – 3 hours
Rainfall – 6 hours
Rainfall – 12 hours
Rainfall – 24 hours
Rainfall – 72 hours
```

---

## 📡 IoT Sensor Integration

FLOODGUARD supports real IoT telemetry through **MQTT**.

Supported sensors include:

* 🌧️ Rain gauge
* 💧 Soil-moisture sensor
* 🌊 Water-level sensor
* 🌡️ Temperature sensor
* 💨 Humidity sensor
* 📊 Pressure sensor

### IoT Architecture

```text
ESP32
  ↓
Sensors
  ↓
Wi-Fi
  ↓
MQTT Broker
  ↓
FLOODGUARD Backend
  ↓
Database
  ↓
ML Engine
  ↓
Live Dashboard
```

The project also includes an **IoT simulator**, allowing the complete pipeline to be tested without physical hardware.

---

# 🛰️ Satellite & GIS Integration

FLOODGUARD is designed to integrate satellite and geospatial information.

### Satellite precipitation

Satellite-derived precipitation can provide regional rainfall information to complement ground sensors and weather services.

### Satellite imagery

The platform can support imagery analysis for:

* True Color
* False Color
* NDVI
* NDWI
* Water-area analysis
* Vegetation/change analysis

### Terrain information

The system can use Digital Elevation Model (DEM) data to derive:

* Elevation
* Slope
* Aspect
* Terrain characteristics
* Drainage proximity

---

# 🤖 Machine Learning

FLOODGUARD uses a structured ML pipeline instead of relying only on fixed thresholds.

### Candidate models

* Random Forest
* Gradient Boosting / HistGradientBoosting

### Input features

```text
Rainfall
Soil Moisture
Water Level
Water-Level Rate of Rise
Forecast Rainfall
Elevation
Slope
Terrain Characteristics
Historical Flood Frequency
Satellite Precipitation
NDVI
NDWI
Sensor Quality
```

### Model output

```text
Flood Probability
       ↓
Risk Score
       ↓
Risk Level
```

Example:

```text
Flood Probability : 0.82
Risk Score        : 82/100
Risk Level        : CRITICAL
```

Model evaluation can include:

* Precision
* Recall
* F1 Score
* ROC-AUC
* PR-AUC
* Confusion Matrix

---

# 📊 Dynamic Risk Score

FLOODGUARD generates a risk score between **0 and 100**.

|  Score | Risk Level  |
| -----: | ----------- |
|   0–24 | 🟢 LOW      |
|  25–49 | 🟡 MODERATE |
|  50–74 | 🟠 HIGH     |
| 75–100 | 🔴 CRITICAL |

The score is generated from the available model/data pipeline and should not be interpreted as an official government warning.

---

# 🗺️ Hyper-Local GIS Risk Map

The interactive map can display:

* Villages
* Wards
* Roads
* Rivers
* Sensors
* Flood-risk zones
* Shelters
* Hospitals
* Critical infrastructure
* Terrain layers
* Satellite layers

Selecting a location can display:

```text
Location
Risk Score
Flood Probability
Rainfall
Soil Moisture
Water Level
Slope
Latest Update
Data Sources
Recommended Action
```

---

# ⚡ Real-Time Data Pipeline

When new IoT data arrives:

```text
Sensor Reading
      ↓
Data Validation
      ↓
Database
      ↓
Feature Update
      ↓
ML Prediction
      ↓
Risk Score
      ↓
Alert Engine
      ↓
WebSocket
      ↓
Live Dashboard
```

This allows the dashboard to update without manually refreshing the page.

---

# 🚨 Early Warning System

FLOODGUARD can generate alerts based on multiple indicators.

Alert levels:

* WATCH
* ADVISORY
* WARNING
* CRITICAL

An alert can contain:

```text
Location
Timestamp
Risk Score
Flood Probability
Reason
Data Sources
Recommended Action
```

Example:

> **CRITICAL ALERT**
> High rainfall combined with rapidly increasing water level and elevated soil moisture has increased the modeled flood risk in the affected area.

Prototype alerts are **model-generated** and are not official emergency warnings.

---

# 🧑‍🚒 Emergency Response

The platform provides an emergency-response workflow:

```text
DETECTED
   ↓
ALERT ISSUED
   ↓
ACKNOWLEDGED
   ↓
FIELD RESPONSE
   ↓
EVACUATION / PREPAREDNESS
   ↓
RESOLVED
```

Response information can include:

* High-risk locations
* Affected roads
* Nearby shelters
* Hospitals
* Field officers
* Citizen reports
* Emergency actions

---

# 📱 Citizen Reporting

Users can report:

* Flooding
* Water-level rise
* Road blockage
* Drain overflow
* Landslide
* Bridge risk
* Other emergencies

Reports can contain:

* Location
* Description
* Severity
* Photograph
* Timestamp

Reports can be classified as:

```text
PENDING
VERIFIED
REJECTED
```

---

# 🧪 Simulation Mode

FLOODGUARD includes a simulation system for demonstrations and testing.

Available scenarios:

```text
NORMAL
HEAVY_RAIN
EXTREME_RAIN
RISING_WATER
SATURATED_SOIL
SENSOR_FAILURE
```

Example:

```text
Normal
  ↓
Extreme Rainfall
  ↓
Soil Moisture ↑
  ↓
Water Level ↑
  ↓
Flood Probability ↑
  ↓
Risk Score ↑
  ↓
Alert Generated
```

This allows the complete system to be demonstrated even when physical sensors or external APIs are unavailable.

---

# 🔄 Operating Modes

FLOODGUARD supports three modes:

### 🟢 LIVE MODE

Uses available real-world data sources and connected sensors.

### 🟡 HYBRID MODE

Combines real external data with simulated IoT data.

### 🔵 DEMO MODE

Uses simulated data for presentations and development.

The interface displays the current mode and data source to prevent simulated data from being mistaken for live measurements.

---

# 🛠️ Technology Stack

### Frontend

* React
* Vite
* JavaScript / TypeScript
* Tailwind CSS
* Leaflet
* Recharts

### Backend

* Python
* FastAPI
* WebSockets
* Pydantic

### Database

* SQLite
* PostgreSQL/PostGIS-ready architecture

### AI/ML

* Python
* NumPy
* Pandas
* Scikit-learn
* Joblib
* Optional SHAP

### IoT

* ESP32
* MQTT
* Mosquitto

### GIS / Satellite

* Leaflet
* GeoJSON
* DEM
* Satellite imagery
* Satellite precipitation

---

# 📁 Project Structure

```text
FLOODGUARD/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── maps/
│   │   └── ...
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── api/
│   ├── database/
│   ├── models/
│   ├── services/
│   │   ├── weather_service.py
│   │   ├── satellite_service.py
│   │   ├── terrain_service.py
│   │   └── mqtt_client.py
│   ├── ml/
│   ├── main.py
│   └── requirements.txt
│
├── ml/
│   ├── datasets/
│   ├── features/
│   ├── models/
│   ├── training/
│   └── evaluation/
│
├── iot/
│   ├── simulator/
│   └── esp32_floodguard/
│
├── data/
│   ├── demo/
│   ├── historical/
│   └── geo/
│
├── tests/
│
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/FLOODGUARD.git
cd FLOODGUARD
```

---

# 🐍 Backend Setup

Create a virtual environment:

### Windows

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
cd backend
pip install -r requirements.txt
```

Start the backend:

```powershell
uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ⚛️ Frontend Setup

Open another terminal:

```powershell
cd frontend
npm install
npm run dev
```

The terminal will provide the local frontend URL.

Usually:

```text
http://localhost:5173
```

---

# 📡 MQTT Setup

For local IoT development, install a compatible MQTT broker such as Mosquitto.

Configure the backend:

```env
MQTT_ENABLED=true
MQTT_BROKER_HOST=localhost
MQTT_BROKER_PORT=1883
MQTT_USERNAME=
MQTT_PASSWORD=
MQTT_TLS=false
```

Then run the backend and IoT simulator.

---

# 🧪 IoT Simulator

Go to:

```powershell
cd iot\simulator
```

Run:

```powershell
python iot_simulator.py --scenario NORMAL
```

Test heavy rainfall:

```powershell
python iot_simulator.py --scenario HEAVY_RAIN
```

Test extreme rainfall:

```powershell
python iot_simulator.py --scenario EXTREME_RAIN
```

The sensor values should travel through:

```text
Simulator
    ↓
MQTT
    ↓
FastAPI
    ↓
Database
    ↓
ML
    ↓
Dashboard
```

---

# 🔐 Environment Variables

Create:

```text
.env
```

based on:

```text
.env.example
```

Example:

```env
DATABASE_URL=sqlite:///./floodguard.db

WEATHER_API_URL=
WEATHER_API_KEY=

MQTT_ENABLED=true
MQTT_BROKER_HOST=localhost
MQTT_BROKER_PORT=1883
MQTT_USERNAME=
MQTT_PASSWORD=
MQTT_TLS=false

SATELLITE_ENABLED=false

MODEL_PATH=ml/models/floodguard_model.joblib
```

**Never commit real API keys, passwords, or credentials to GitHub.**

---

# 🌐 API Endpoints

### System

```text
GET /api/health
GET /api/system/health
```

### Weather

```text
GET /api/weather/current
GET /api/weather/hourly
GET /api/weather/rainfall
```

### Satellite

```text
GET /api/satellite/rainfall
GET /api/satellite/imagery
GET /api/satellite/ndvi
GET /api/satellite/ndwi
```

### Terrain

```text
GET /api/terrain/elevation
GET /api/terrain/slope
```

### Sensors

```text
GET /api/sensors
GET /api/sensors/{id}
POST /api/sensors
POST /api/sensors/{id}/calibrate
```

### Risk

```text
GET /api/risk/live
GET /api/risk/{location_id}
POST /api/ml/predict
```

### ML

```text
POST /api/ml/train
GET /api/ml/models
GET /api/ml/metrics
```

### WebSocket

```text
/ws/live
```

---

# 🧠 Machine Learning Workflow

```text
Historical Data
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Train/Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Versioning
      ↓
Active Model
      ↓
Real-Time Inference
```

The model should only use information available at prediction time to avoid data leakage.

---

# 📈 Model Evaluation

FLOODGUARD evaluates models using:

* Precision
* Recall
* F1 Score
* ROC-AUC
* PR-AUC
* Confusion Matrix

For an early-warning system, evaluation should pay particular attention to detecting dangerous events while also considering false alarms.

---

# 🔬 Data Sources

The system is designed to support multiple data sources, including:

* Weather APIs
* Ground-based IoT sensors
* NASA GPM IMERG precipitation
* Sentinel-2 satellite imagery
* Digital Elevation Models
* Historical flood/disaster datasets

Data source availability, resolution, update frequency, and licensing should be checked before operational deployment.

---

# ⚠️ Important Disclaimer

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the Oxlint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and Oxlint's TypeScript related rules in your project.
