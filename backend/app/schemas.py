from pydantic import BaseModel

class PredictionOut(BaseModel):
    date: str
    predicted_price: float

class GoldPriceOut(BaseModel):
    date: str
    price: float
