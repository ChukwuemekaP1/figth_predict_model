import pickle
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# --- 1. SETUP ---
app = FastAPI(title="Flight Delay Prediction API", version="1.0")

# --- NEW: Setup for HTML Templating ---
templates = Jinja2Templates(directory="templates")

# Load the trained model pipeline and the column list
try:
    model = pickle.load(open("model/flight_delay_model.pkl", "rb"))
    model_columns = pickle.load(open("model/model_columns.pkl", "rb"))
    print("Model and columns loaded successfully.")
except FileNotFoundError:
    print("Error: Model or column files not found. Make sure they are in the correct directory.")
    model = None
    model_columns = None

# --- 2. DEFINE THE INPUT DATA MODEL ---
class FlightFeatures(BaseModel):
    month: int
    day_of_month: int
    day_of_week: int
    op_unique_carrier: str
    origin: str
    dest: str
    crs_dep_time: int
    dep_delay: float
    distance: float

    # Example data for the API documentation
    class Config:
        json_schema_extra = {
            "example": {
                "month": 1,
                "day_of_month": 15,
                "day_of_week": 3,
                "op_unique_carrier": "WN",  # Southwest Airlines
                "origin": "LAX",
                "dest": "SFO",
                "crs_dep_time": 1400,  # 2:00 PM
                "dep_delay": -5.0,  # Left 5 minutes early
                "distance": 337.0
            }
        }

# --- 3. CREATE THE PREDICTION ENDPOINT ---
@app.post("/predict")
def predict(flight: FlightFeatures):
    """
    Receives flight data and returns a delay prediction.
    - **Prediction 0**: The flight is predicted to be **On Time**.
    - **Prediction 1**: The flight is predicted to be **Delayed**.
    """
    if not model or not model_columns:
        return {"error": "Model is not loaded. Check server logs."}
    
    # Convert the input data into a pandas DataFrame
    # The order of columns must match the order used during training.
    data = pd.DataFrame([flight.model_dump()], columns=model_columns)
    
    # Make the prediction
    prediction = model.predict(data)
    prediction_proba = model.predict_proba(data)
    
    # Extract the integer prediction value
    prediction_value = int(prediction[0])
    
    # Return the result
    return {
        "prediction": prediction_value,
        "prediction_label": "Delayed" if prediction_value == 1 else "On Time",
        "confidence_on_time": f"{prediction_proba[0][0]:.4f}",
        "confidence_delayed": f"{prediction_proba[0][1]:.4f}"
    }

# --- 4. UPDATE THE ROOT ENDPOINT TO SERVE THE FRONTEND ---
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """This endpoint now serves the HTML frontend."""
    return templates.TemplateResponse("index.html", {"request": request})