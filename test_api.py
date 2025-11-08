"""
Quick test script to verify the API setup
"""
import pickle

print("Testing model loading...")
try:
    model = pickle.load(open("model/flight_delay_model.pkl", "rb"))
    model_columns = pickle.load(open("model/model_columns.pkl", "rb"))
    print("✓ Model loaded successfully")
    print(f"✓ Model type: {type(model).__name__}")
    print(f"✓ Expected columns: {model_columns}")
    print("\nAll checks passed! Ready to run the API.")
    print("\nTo start the server, run:")
    print("  venv\\Scripts\\activate")
    print("  uvicorn main:app --reload")
except Exception as e:
    print(f"✗ Error: {e}")
