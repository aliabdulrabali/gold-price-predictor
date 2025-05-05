import requests
from app.predictor import generate_prediction
from datetime import datetime

TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

def send_price_alert():
    prediction = generate_prediction()
    if prediction["predicted_price"] < 200:  # change threshold
        msg = f"💰 ALERT: Gold price predicted to drop to {prediction['predicted_price']} QAR on {prediction['date']}."
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

if __name__ == "__main__":
    send_price_alert()
