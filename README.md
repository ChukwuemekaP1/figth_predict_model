# Flight Delay Predictor

A robust machine learning web application for predicting flight delays, featuring both FastAPI and Streamlit interfaces.

## Features
- **FastAPI Backend**: RESTful API for flight delay prediction
- **Streamlit Frontend**: Interactive web UI for real-time predictions
- **Pre-trained Model**: Uses a scikit-learn pipeline trained on flight data
- **Docker Ready**: Easily deployable with Docker

## Project Structure
```
Flight_Delay_Predictor/
├── main.py                 # FastAPI application
├── api.py                  # Streamlit frontend
├── model/                  # Trained ML models
│   ├── flight_delay_model.pkl
│   └── model_columns.pkl
├── requirements.txt        # Python dependencies
├── start_server.bat        # Windows batch script for FastAPI
├── test_api.py             # API test script
├── templates/              # HTML templates for FastAPI
│   └── index.html
└── venv/                   # Python virtual environment
```

## Quick Start

### 1. Local Setup

#### Activate Virtual Environment
```bash
venv\Scripts\activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Run FastAPI Backend
```bash
uvicorn main:app --reload
```
- API Docs: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

#### Run Streamlit Frontend
```bash
streamlit run api.py
```
- UI: http://localhost:8501/

### 2. API Usage

#### POST /predict
Send a JSON payload to `/predict`:
```json
{
  "month": 1,
  "day_of_month": 15,
  "day_of_week": 3,
  "op_unique_carrier": "WN",
  "origin": "LAX",
  "dest": "SFO",
  "crs_dep_time": 1400,
  "dep_delay": -5.0,
  "distance": 337.0
}
```
Response:
```json
{
  "prediction": 0,
  "prediction_label": "On Time",
  "confidence_on_time": "0.8523",
  "confidence_delayed": "0.1477"
}
```

### 3. Docker Deployment

#### Build the Docker Image
```bash
docker build -t flight-delay-api .
```

#### Run the Container
```bash
docker run -d -p 8000:8000 flight-delay-api
```

#### Access the API
- FastAPI: http://localhost:8000
- Docs: http://localhost:8000/docs

## How It Works
- **Model Loading**: Loads pre-trained model and columns from `model/`
- **Prediction**: Accepts flight details, returns delay prediction and confidence
- **Streamlit UI**: User-friendly form for manual predictions
- **FastAPI**: REST endpoint for programmatic access

## Requirements
```
fastapi>=0.100.0
uvicorn>=0.20.0
pandas>=2.0.0
scikit-learn>=1.3.0
jinja2>=3.1.0
python-multipart>=0.0.6
streamlit>=1.51.0
```

## Testing
Run the included test script:
```bash
python test_api.py
```

## License
MIT
