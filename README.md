# 🏠 House Price Prediction

A Machine Learning project that predicts house prices using the Ames Housing dataset.

## Project Workflow

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Preprocessing
- Feature Selection
- Model Training
- Model Comparison
- Hyperparameter Tuning
- FastAPI Deployment
- Streamlit Interface

## Models Used

- Linear Regression
- Ridge Regression
- Random Forest
- Gradient Boosting

## Best Model

Gradient Boosting Regressor

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit

## How to Run

Start FastAPI:

uvicorn app:app --reload

Start Streamlit:

streamlit run frontend.py

## Project Structure

house-price-prediction/
│
├── data/
│   └── train.csv
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── models/
│   ├── preprocessor.pkl
│   ├── selector.pkl
│   ├── house_price_model.pkl
│   └── feature_columns.pkl
│
├── app.py
├── frontend.py
├── requirements.txt
├── README.md
└── .gitignore