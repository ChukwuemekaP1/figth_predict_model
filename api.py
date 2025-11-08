import streamlit as st
import pandas as pd
import pickle
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Flight Delay Predictor",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- MODEL LOADING ---
# Use a cache to load the model only once
@st.cache_resource
def load_model():
    """Loads the pre-trained model and column list from disk."""
    try:
        with open("model/flight_delay_model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("model/model_columns.pkl", "rb") as f:
            model_columns = pickle.load(f)
        return model, model_columns
    except FileNotFoundError:
        st.error("Model files not found! Please make sure 'model/flight_delay_model.pkl' and 'model/model_columns.pkl' are in the 'model' directory.")
        return None, None

model, model_columns = load_model()

# --- APP LAYOUT ---
st.title("✈️ Flight Delay Predictor")
st.markdown("Enter the flight details below to predict whether a flight will be delayed by 15 minutes or more.")

if model is not None:
    # --- INPUT FORM ---
    with st.form(key="prediction_form"):
        st.header("Flight Details")

        # Create two columns for a cleaner layout
        col1, col2 = st.columns(2)

        with col1:
            op_unique_carrier = st.text_input("Carrier Code", value="WN", help="e.g., WN, DL, AA")
            origin = st.text_input("Origin Airport", value="LAX", help="e.g., LAX, JFK, ORD")
            crs_dep_time = st.number_input("Scheduled Departure Time (HHMM)", min_value=0, max_value=2359, value=1400, step=1)
            month = st.slider("Month", 1, 12, 1)
            day_of_month = st.slider("Day of Month", 1, 31, 15)

        with col2:
            dest = st.text_input("Destination Airport", value="SFO", help="e.g., SFO, MIA, DFW")
            distance = st.number_input("Distance (miles)", min_value=0.0, value=337.0, step=0.1)
            dep_delay = st.number_input("Departure Delay (minutes)", value=-5.0, step=0.1, help="Use a negative number for early departures.")
            day_of_week = st.slider("Day of Week", 1, 7, 3, help="1=Monday, 7=Sunday")

        # Submit button for the form
        submit_button = st.form_submit_button(label="Predict Delay")

    # --- PREDICTION LOGIC ---
    if submit_button:
        # Create a dictionary from the inputs
        input_data = {
            'month': month,
            'day_of_month': day_of_month,
            'day_of_week': day_of_week,
            'op_unique_carrier': op_unique_carrier,
            'origin': origin,
            'dest': dest,
            'crs_dep_time': crs_dep_time,
            'dep_delay': dep_delay,
            'distance': distance
        }

        # Convert to a DataFrame with the correct column order
        input_df = pd.DataFrame([input_data], columns=model_columns)

        # Make prediction
        with st.spinner('Analyzing flight data...'):
            time.sleep(1) # Simulate a short delay for better UX
            prediction = model.predict(input_df)
            prediction_proba = model.predict_proba(input_df)

        prediction_value = prediction[0]
        confidence_delayed = prediction_proba[0][1]
        confidence_on_time = prediction_proba[0][0]

        # --- DISPLAY RESULT ---
        st.header("Prediction Result")
        if prediction_value == 1:
            st.error(f"**Prediction: Flight will be DELAYED**")
            st.metric(label="Confidence", value=f"{confidence_delayed:.2%}")
            st.progress(confidence_delayed)
        else:
            st.success(f"**Prediction: Flight will be ON TIME**")
            st.metric(label="Confidence", value=f"{confidence_on_time:.2%}")
            st.progress(confidence_on_time)

        # Show the input data for reference
        with st.expander("Show Input Data"):
            st.write(input_df)
else:
    st.warning("The application cannot make predictions because the model files are missing.")

