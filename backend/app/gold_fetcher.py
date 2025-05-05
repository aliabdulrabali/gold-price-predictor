import requests
from app.database import SessionLocal
from app.models import GoldPrice
from datetime import datetime

API_KEY = "YOUR_METALS_API_KEY"  # Replace with real key
URL = f"https://metals-api.com/api/latest?access_key={API_KEY}&base=USD&symbols=XAU"

def fetch_gold_price():
    response = requests.get(URL)
    data = response.json()
    price_per_ounce = data["rates"]["XAU"]
    price_per_gram = price_per_ounce / 31.1035  # convert ounce to gram

    db = SessionLocal()
    today = datetime.utcnow().date()

    existing = db.query(GoldPrice).filter(GoldPrice.date == today).first()
    if not existing:
        new_price = GoldPrice(date=today, price=round(price_per_gram, 2))
        db.add(new_price)
        db.commit()
    db.close()

# Optional manual run
if __name__ == "__main__":
    fetch_gold_price()
