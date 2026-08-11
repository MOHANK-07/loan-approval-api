# 🏦 Loan Approval Prediction API

A Machine Learning based Loan Approval Prediction system built using Python, Scikit-learn, XGBoost, and FastAPI.

The system accepts applicant information, processes the input through a trained Stacking Ensemble model, and returns the predicted loan approval status and approval probability.

## 🚀 Live Application

### Frontend

https://loan-approval-frontend-t6xc.onrender.com

### Backend API

https://loan-approval-api-jn83.onrender.com

### API Documentation

https://loan-approval-api-jn83.onrender.com/docs

## 📌 Project Overview

This project predicts whether a loan application is likely to be approved or rejected based on financial and personal information provided by the applicant.

### Main Components

- Machine Learning model
- FastAPI backend
- Web frontend
- Model validation
- Cloud deployment using Render

## 🔄 How It Works

```text
User
  |
  v
Web Frontend
  |
  | Loan application data
  v
FastAPI Backend
  |
  | Input validation
  v
Machine Learning Model
  |
  | Prediction
  v
Loan Status + Approval Probability
  |
  v
Web Frontend
  |
  v
Result Display
```

## 📥 Input Features

| Feature | Description |
|---|---|
| `no_of_dependents` | Number of people financially dependent on the applicant |
| `education` | Education status of the applicant |
| `self_employed` | Whether the applicant is self-employed |
| `income_annum` | Applicant's annual income |
| `loan_amount` | Amount of loan requested |
| `loan_term` | Loan repayment period |
| `cibil_score` | Applicant's CIBIL credit score |
| `residential_assets_value` | Value of residential properties owned |
| `commercial_assets_value` | Value of commercial properties owned |
| `luxury_assets_value` | Value of luxury assets owned |
| `bank_asset_value` | Value of assets held in bank accounts |

## 🤖 Machine Learning Model

The project uses a **Stacking Ensemble Machine Learning model**.

The trained model is stored using Joblib.

```text
models/
├── stacking_model.pkl
└── feature_names.pkl
```

### Model Files

- `stacking_model.pkl` — contains the trained Stacking Ensemble model.
- `feature_names.pkl` — contains the feature names and their required order for prediction.

## 📊 Model Performance

The deployed API was validated using the complete test dataset.

| Metric | Result |
|---|---:|
| Total test samples | 854 |
| Correct predictions | 843 |
| Wrong predictions | 11 |
| API errors | 0 |
| **Accuracy** | **98.7119%** |

The full test-set validation achieved an accuracy of **98.71%**.

## 🔌 API Endpoints

### GET `/`

Used to check whether the FastAPI server is running.

Example response:

```json
{
  "message": "Loan Approval API is working!"
}
```

### POST `/predict`

Used to generate a loan approval prediction.

#### Example Request

```json
{
  "no_of_dependents": 2,
  "education": 1,
  "self_employed": 0,
  "income_annum": 5000000,
  "loan_amount": 2000000,
  "loan_term": 10,
  "cibil_score": 750,
  "residential_assets_value": 5000000,
  "commercial_assets_value": 2000000,
  "luxury_assets_value": 1000000,
  "bank_asset_value": 3000000
}
```

#### Example Response

```json
{
  "prediction": 1,
  "status": "Approved",
  "approval_probability": 0.992
}
```

## ⚙️ API Workflow

1. Receives applicant information.
2. Validates the input using Pydantic.
3. Converts the input into a Python dictionary.
4. Converts the dictionary into a Pandas DataFrame.
5. Arranges the features in the correct order.
6. Sends the data to the trained Machine Learning model.
7. Generates the prediction.
8. Calculates the approval probability.
9. Converts the prediction into a readable status.
10. Returns the result as JSON.

## 📁 Project Structure

```text
loan-approval-api/
│
├── app.py
├── requirements.txt
├── README.md
│
└── models/
    ├── stacking_model.pkl
    └── feature_names.pkl
```

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Pandas
- Scikit-learn
- XGBoost
- Joblib
- Git
- GitHub
- Render

## 📦 Requirements

```text
fastapi
uvicorn
pydantic
pandas
scikit-learn==1.6.1
xgboost==3.3.0
joblib==1.5.3
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/MOHANK-07/loan-approval-api.git
```

### 2. Open the project directory

```bash
cd loan-approval-api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the FastAPI server

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 Swagger API Documentation

FastAPI automatically provides interactive API documentation.

Local documentation:

```text
http://127.0.0.1:8000/docs
```

Deployed documentation:

https://loan-approval-api-jn83.onrender.com/docs

## 🌐 Frontend Integration

The frontend communicates with the FastAPI backend using a JavaScript `fetch()` request.

The frontend sends loan application data to:

```text
https://loan-approval-api-jn83.onrender.com/predict
```

The backend processes the data and returns a JSON response.

The frontend then displays:

- Loan approval status
- Approval probability

## 🔐 CORS Configuration

The FastAPI backend is configured with CORS middleware so that the deployed frontend can communicate with the deployed API.

Production frontend:

```text
https://loan-approval-frontend-t6xc.onrender.com
```

## 🧪 Validation

### Sample Validation

A sample of 20 records was tested through the deployed API.

```text
Samples tested     : 20
Correct predictions: 20
Wrong predictions  : 0
API Accuracy       : 100.00%
```

### Full Test Set Validation

The complete test set contained 854 samples.

```text
Total X_test samples : 854
Successfully tested   : 854
Correct predictions   : 843
Wrong predictions     : 11
API errors            : 0
FastAPI Accuracy      : 98.7119%
```

The full test-set result is more representative because it evaluates the deployed API using the complete test dataset.

## ☁️ Deployment

The FastAPI backend is deployed on Render.

### Backend

https://loan-approval-api-jn83.onrender.com

### Frontend

https://loan-approval-frontend-t6xc.onrender.com

## 🔗 Repository

GitHub:

https://github.com/MOHANK-07/loan-approval-api

Frontend Repository:

https://github.com/MOHANK-07/loan-approval-frontend

## ⚠️ Disclaimer

This project is created for educational and demonstration purposes.

The prediction generated by this Machine Learning model should not be considered an actual financial or loan approval decision.

## 👨‍💻 Author

**Mohan K**

GitHub:

https://github.com/MOHANK-07
