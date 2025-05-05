from sqlalchemy import Column, Integer, Float, String, Date
from app.database import Base

class GoldPrice(Base):
    __tablename__ = "gold_prices"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, unique=True, index=True)
    price = Column(Float)
