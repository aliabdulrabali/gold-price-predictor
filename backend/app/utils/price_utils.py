import requests
import os
from datetime import datetime
from sqlalchemy.orm import Session
from app.database import get_db, GoldPrice

def fetch_and_save_gold_price():
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {
        "x-access-token": os.getenv("GOLD_API_KEY"),
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        price = data.get("price")
        if not price:
            raise Exception("Price not found in response")

        db: Session = next(get_db())
        db_price = GoldPrice(date=datetime.utcnow(), price=price)
        db.add(db_price)
        db.commit()

        return price
    except Exception as e:
        print(f"Error fetching gold price: {e}")
        return None

def run_price_job():
    price = fetch_and_save_gold_price()
    print(f"Fetched and saved price: {price}")
