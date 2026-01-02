from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main import predict_price

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict(data: dict):
    price = predict_price(
        data["grade"],
        data["sqft_above"],
        data["sqft_living"]
    )
    return {"price": price}

@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Prediction API"}