@echo off
echo Starting FastAPI Flight Delay Prediction API...
echo.
call venv\Scripts\activate
echo Virtual environment activated
echo.
echo Starting FastAPI server at http://localhost:8000
echo Press Ctrl+C to stop the server
echo.
uvicorn main:app --reload