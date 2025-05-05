import logging

logging.basicConfig(level=logging.INFO)
from fastapi import FastAPI
from app import routes
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Gold Price Predictor API",
    description="Get predictions and gold price history",
    version="1.0.0",
    openapi_tags=[
        {"name": "Predictions", "description": "Forecasting"},
        {"name": "Data", "description": "Historical price data"}
    ]
)

app = FastAPI(
    title="Gold Price Predictor",
    description="Predict future gold prices using ML",
    version="1.0.0"
)

app.include_router(routes.router)

# For local testing only
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
