from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "https://loan-approval-frontend-t6xc.onrender.com"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = joblib.load("models/stacking_model.pkl")
feature_names = joblib.load("models/feature_names.pkl")


# =========================
# Input data structure
# =========================

class LoanApplication(BaseModel):
    no_of_dependents: int
    education: int
    self_employed: int
    income_annum: float
    loan_amount: float
    loan_term: int
    cibil_score: int
    residential_assets_value: float
    commercial_assets_value: float
    luxury_assets_value: float
    bank_asset_value: float


# =========================
# Home endpoint
# =========================

@app.get("/")
def home():
    return {
        "message": "Loan Approval API is working!"
    }


# =========================
# Prediction endpoint
# =========================

@app.post("/predict")
def predict(application: LoanApplication):

    # Convert user input into a dictionary
    data = {
        "no_of_dependents": application.no_of_dependents,
        "education": application.education,
        "self_employed": application.self_employed,
        "income_annum": application.income_annum,
        "loan_amount": application.loan_amount,
        "loan_term": application.loan_term,
        "cibil_score": application.cibil_score,
        "residential_assets_value": application.residential_assets_value,
        "commercial_assets_value": application.commercial_assets_value,
        "luxury_assets_value": application.luxury_assets_value,
        "bank_asset_value": application.bank_asset_value
    }

    # Convert dictionary into DataFrame
    input_data = pd.DataFrame([data])

    # Make sure feature order is correct
    input_data = input_data[feature_names]

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Get probability
    probability = model.predict_proba(input_data)[0][1]

    # Convert prediction into readable text
    if prediction == 1:
        status = "Approved"
    else:
        status = "Rejected"

    return {
        "prediction": int(prediction),
        "status": status,
        "approval_probability": round(float(probability), 4)
    }