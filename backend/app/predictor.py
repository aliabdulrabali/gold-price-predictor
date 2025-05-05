import pandas as pd
from app.database import SessionLocal
from app.models import GoldPrice
from prophet import Prophet
from datetime import datetime
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

def train_model():
    db = SessionLocal()
    prices = db.query(GoldPrice).order_by(GoldPrice.date).all()
    db.close()

    if len(prices) < 10:
        return

    df = pd.DataFrame([{"ds": p.date, "y": p.price} for p in prices])
    model = Prophet()
    model.fit(df)
    joblib.dump(model, MODEL_PATH)

def generate_prediction(days=7):
    if not os.path.exists(MODEL_PATH):
        train_model()
    model = joblib.load(MODEL_PATH)
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    prediction_day = forecast.iloc[-1]
    return {
        "date": prediction_day['ds'].date().isoformat(),
        "predicted_price": round(prediction_day['yhat'], 2)
    }
