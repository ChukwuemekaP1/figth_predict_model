# Flight Delay Prediction API

A machine learning web application that predicts flight delays with **two frontend options**: FastAPI with HTML templates and Streamlit.

## Project Structure

```
Flight_Delay_Predictor/
├── main.py                 # FastAPI application with HTML frontend
├── api.py                  # Streamlit application
├── model/                  # Trained ML models
│   ├── flight_delay_model.pkl
│   └── model_columns.pkl
├── templates/              # HTML templates for FastAPI
│   └── index.html         # FastAPI frontend interface
├── venv/                   # Virtual environment
├── requirements.txt        # Python dependencies
├── start_fastapi.bat      # FastAPI startup script
├── start_streamlit.bat    # Streamlit startup script
└── test_api.py            # Test script
```

## Setup

1. **Virtual environment is already created and activated**
2. **Dependencies are already installed**

## Running the Application

### Option 1: FastAPI Frontend (HTML/JavaScript)
1. **Start the FastAPI server:**
   ```bash
   start_fastapi.bat
   ```
   Or manually:
   ```bash
   venv\Scripts\activate
   uvicorn main:app --reload
   ```

2. **Access the application:**
   - Web Interface: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Alternative API Docs: http://localhost:8000/redoc

### Option 2: Streamlit Frontend (Python-based UI)
1. **Start the Streamlit app:**
   ```bash
   start_streamlit.bat
   ```
   Or manually:
   ```bash
   venv\Scripts\activate
   streamlit run api.py
   ```

2. **Access the application:**
   - Streamlit Interface: http://localhost:8501

## API Endpoints (FastAPI)

### GET /
Serves the HTML frontend interface for making predictions.

### POST /predict
Makes a flight delay prediction.

**Request Body:**
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

**Response:**
```json
{
  "prediction": 0,
  "prediction_label": "On Time",
  "confidence_on_time": "0.8523",
  "confidence_delayed": "0.1477"
}
```

## Features

### FastAPI Frontend
- **Web Interface**: Clean HTML form with real-time predictions
- **REST API**: JSON-based API for programmatic access
- **Interactive Documentation**: Auto-generated API docs with Swagger UI
- **Responsive Design**: Works on desktop and mobile devices

### Streamlit Frontend
- **Interactive UI**: Python-based web interface with sliders and inputs
- **Real-time Feedback**: Instant predictions with confidence metrics
- **Visual Elements**: Progress bars and colored result displays
- **Form Validation**: Built-in input validation and error handling

## Model Information

The model uses the following features:
- Month (1-12)
- Day of Month (1-31)
- Day of Week (1-7)
- Carrier Code (e.g., WN, DL, AA)
- Origin Airport (e.g., LAX)
- Destination Airport (e.g., SFO)
- Scheduled Departure Time (HHMM format)
- Departure Delay (minutes, negative for early)
- Distance (miles)

## Testing

Run the test script to verify the setup:
```bash
python test_api.py
```

## Repository

This project is available at: https://github.com/ChukwuemekaP1/figth_predict_model.git