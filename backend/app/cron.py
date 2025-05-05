from app.gold_fetcher import fetch_gold_price
from app.predictor import train_model

def daily_job():
    print("🔁 Fetching today's gold price...")
    fetch_gold_price()
    print("🧠 Retraining model...")
    train_model()

if __name__ == "__main__":
    daily_job()
