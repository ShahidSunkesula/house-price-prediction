from fastapi import FastAPI
import pandas as pd
import joblib


# --------------------------------------------------
# Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="House Price Prediction API",
    description="Predict house prices using Machine Learning",
    version="1.0"
)


# --------------------------------------------------
# Load saved ML objects
# --------------------------------------------------

preprocessor = joblib.load(
    "models/preprocessor.pkl"
)

selector = joblib.load(
    "models/selector.pkl"
)

model = joblib.load(
    "models/house_price_model.pkl"
)

feature_columns = joblib.load(
    "models/feature_columns.pkl"
)


# --------------------------------------------------
# Home endpoint
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "House Price Prediction API is running"
    }


# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict(data: dict):

    # Convert JSON input into DataFrame
    input_data = pd.DataFrame([data])


    # --------------------------------------------------
    # Feature Engineering
    # --------------------------------------------------

    input_data["TotalSF"] = (
        input_data["TotalBsmtSF"]
        + input_data["1stFlrSF"]
        + input_data["2ndFlrSF"]
    )


    input_data["TotalBathrooms"] = (
        input_data["FullBath"]
        + 0.5 * input_data["HalfBath"]
        + input_data["BsmtFullBath"]
        + 0.5 * input_data["BsmtHalfBath"]
    )


    input_data["HouseAge"] = (
        input_data["YrSold"]
        - input_data["YearBuilt"]
    )


    input_data["RemodAge"] = (
        input_data["YrSold"]
        - input_data["YearRemodAdd"]
    )


    input_data["GarageAge"] = (
        input_data["YrSold"]
        - input_data["GarageYrBlt"]
    )


    input_data.loc[
        input_data["GarageYrBlt"] == 0,
        "GarageAge"
    ] = 0


    input_data["TotalPorchSF"] = (
        input_data["WoodDeckSF"]
        + input_data["OpenPorchSF"]
        + input_data["EnclosedPorch"]
        + input_data["3SsnPorch"]
        + input_data["ScreenPorch"]
    )


    input_data["TotalFinishedSF"] = (
        input_data["GrLivArea"]
        + input_data["BsmtFinSF1"]
        + input_data["BsmtFinSF2"]
    )


    # --------------------------------------------------
    # Arrange columns exactly as during training
    # --------------------------------------------------

    input_data = input_data[feature_columns]


    # --------------------------------------------------
    # Preprocessing
    # --------------------------------------------------

    processed_data = preprocessor.transform(
        input_data
    )


    # --------------------------------------------------
    # Feature Selection
    # --------------------------------------------------

    selected_data = selector.transform(
        processed_data
    )


    # --------------------------------------------------
    # Prediction
    # --------------------------------------------------

    prediction = model.predict(
        selected_data
    )


    # --------------------------------------------------
    # Return result
    # --------------------------------------------------

    return {
        "predicted_price": float(prediction[0])
    }