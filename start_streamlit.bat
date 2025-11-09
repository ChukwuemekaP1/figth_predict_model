@echo off
echo Starting Streamlit Flight Delay Prediction App...
echo.
call venv\Scripts\activate
echo Virtual environment activated
echo.
echo Starting Streamlit app at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.
streamlit run api.py