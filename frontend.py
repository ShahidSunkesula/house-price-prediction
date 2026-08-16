import streamlit as st
import requests


st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠"
)

st.title("🏠 House Price Predictor")
st.write("Enter the main details of the house to estimate its price.")


# -----------------------------
# Main House Information
# -----------------------------

st.header("House Information")

col1, col2 = st.columns(2)

with col1:
    overall_qual = st.slider(
        "Overall Quality",
        1, 10, 7
    )

    year_built = st.number_input(
        "Year Built",
        1800, 2026, 2000
    )

    year_remod = st.number_input(
        "Year Remodeled",
        1800, 2026, 2000
    )

    gr_liv_area = st.number_input(
        "Living Area (sq ft)",
        200, 10000, 1500
    )

    lot_area = st.number_input(
        "Lot Area (sq ft)",
        500, 200000, 8000
    )

with col2:
    bedrooms = st.number_input(
        "Bedrooms",
        0, 15, 3
    )

    full_bath = st.number_input(
        "Full Bathrooms",
        0, 10, 2
    )

    half_bath = st.number_input(
        "Half Bathrooms",
        0, 10, 1
    )

    neighborhood = st.selectbox(
        "Neighborhood",
        [
            "NoRidge",
            "NridgHt",
            "StoneBr",
            "CollgCr",
            "Veenker",
            "Crawfor",
            "Somerst",
            "Gilbert",
            "Edwards",
            "OldTown"
        ]
    )

    kitchen_quality = st.selectbox(
        "Kitchen Quality",
        ["Ex", "Gd", "TA", "Fa", "Po"]
    )


# -----------------------------
# Garage
# -----------------------------

st.header("Garage")

garage = st.selectbox(
    "Does the house have a garage?",
    ["Yes", "No"]
)

if garage == "Yes":

    col1, col2 = st.columns(2)

    with col1:
        garage_cars = st.number_input(
            "Garage Cars",
            1, 5, 2
        )

    with col2:
        garage_area = st.number_input(
            "Garage Area (sq ft)",
            0, 2000, 500
        )

    garage_year = st.number_input(
        "Garage Year Built",
        1800, 2026, year_built
    )

    garage_type = "Attchd"
    garage_finish = "RFn"
    garage_qual = "TA"
    garage_cond = "TA"

else:

    garage_cars = 0
    garage_area = 0
    garage_year = 0
    garage_type = "None"
    garage_finish = "None"
    garage_qual = "None"
    garage_cond = "None"


# -----------------------------
# Basement
# -----------------------------

st.header("Basement")

basement = st.selectbox(
    "Does the house have a basement?",
    ["Yes", "No"]
)

if basement == "Yes":

    bsmt_area = st.number_input(
        "Basement Area (sq ft)",
        0, 5000, 800
    )

    bsmt_qual = st.selectbox(
        "Basement Quality",
        ["Ex", "Gd", "TA", "Fa", "Po"]
    )

    bsmt_exposure = st.selectbox(
        "Basement Exposure",
        ["Gd", "Av", "Mn", "No"]
    )

    bsmt_full_bath = st.number_input(
        "Basement Full Bathrooms",
        0, 5, 1
    )

    bsmt_fin_sf1 = bsmt_area
    bsmt_cond = "TA"
    bsmt_fin_type1 = "GLQ"

else:

    bsmt_area = 0
    bsmt_qual = "None"
    bsmt_cond = "None"
    bsmt_exposure = "None"
    bsmt_full_bath = 0
    bsmt_fin_sf1 = 0
    bsmt_fin_type1 = "None"


# -----------------------------
# Prediction
# -----------------------------

st.divider()

if st.button(
    "🏠 Predict House Price",
    type="primary"
):

    data = {
        "Id": 1,
        "MSSubClass": 60,
        "MSZoning": "RL",
        "LotFrontage": 70,
        "LotArea": lot_area,
        "Street": "Pave",
        "Alley": "None",
        "LotShape": "Reg",
        "LandContour": "Lvl",
        "Utilities": "AllPub",
        "LotConfig": "Inside",
        "LandSlope": "Gtl",
        "Neighborhood": neighborhood,
        "Condition1": "Norm",
        "Condition2": "Norm",
        "BldgType": "1Fam",
        "HouseStyle": "2Story",

        "OverallQual": overall_qual,
        "OverallCond": 5,

        "YearBuilt": year_built,
        "YearRemodAdd": year_remod,

        "RoofStyle": "Gable",
        "RoofMatl": "CompShg",

        "Exterior1st": "VinylSd",
        "Exterior2nd": "VinylSd",

        "MasVnrType": "None",
        "MasVnrArea": 0,

        "ExterQual": "Gd",
        "ExterCond": "TA",
        "Foundation": "PConc",

        "BsmtQual": bsmt_qual,
        "BsmtCond": bsmt_cond,
        "BsmtExposure": bsmt_exposure,
        "BsmtFinType1": bsmt_fin_type1,
        "BsmtFinSF1": bsmt_fin_sf1,

        "BsmtFinType2": "None",
        "BsmtFinSF2": 0,
        "BsmtUnfSF": 0,
        "TotalBsmtSF": bsmt_area,

        "Heating": "GasA",
        "HeatingQC": "Ex",
        "CentralAir": "Y",
        "Electrical": "SBrkr",

        "1stFlrSF": gr_liv_area,
        "2ndFlrSF": 0,
        "LowQualFinSF": 0,
        "GrLivArea": gr_liv_area,

        "BsmtFullBath": bsmt_full_bath,
        "BsmtHalfBath": 0,

        "FullBath": full_bath,
        "HalfBath": half_bath,

        "BedroomAbvGr": bedrooms,
        "KitchenAbvGr": 1,

        "KitchenQual": kitchen_quality,

        "TotRmsAbvGrd": bedrooms + 3,
        "Functional": "Typ",

        "Fireplaces": 1,
        "FireplaceQu": "TA",

        "GarageType": garage_type,
        "GarageYrBlt": garage_year,
        "GarageFinish": garage_finish,
        "GarageCars": garage_cars,
        "GarageArea": garage_area,
        "GarageQual": garage_qual,
        "GarageCond": garage_cond,

        "PavedDrive": "Y",

        "WoodDeckSF": 0,
        "OpenPorchSF": 0,
        "EnclosedPorch": 0,
        "3SsnPorch": 0,
        "ScreenPorch": 0,

        "PoolArea": 0,
        "PoolQC": "None",
        "Fence": "None",
        "MiscFeature": "None",
        "MiscVal": 0,

        "MoSold": 6,
        "YrSold": 2020,

        "SaleType": "WD",
        "SaleCondition": "Normal"
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction completed!")

            usd_price = result["predicted_price"]

            # Approximate USD → INR conversion
            inr_price = usd_price * 90

            st.metric(
                "Estimated House Price",
                f"${usd_price:,.0f}"
            )

        else:

            st.error(
                f"API Error: {response.text}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "FastAPI is not running. "
            "Start it using: uvicorn app:app --reload"
        )