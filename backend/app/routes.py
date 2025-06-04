from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.models import GoldPrice
from app.database import SessionLocal
from app.schemas import GoldPriceOut, PredictionOut
from app.predictor import generate_prediction

router = APIRouter()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/prices", response_model=List[GoldPriceOut])
def get_prices(db: Session = Depends(get_db)):
    return db.query(GoldPrice).order_by(GoldPrice.date.desc()).limit(30).all()

@router.get("/predict", response_model=PredictionOut)
def get_prediction():
    return generate_prediction()
