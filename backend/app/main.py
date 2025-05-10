from fastapi import FastAPI, Query
from pydantic import BaseModel
import yfinance as yf
import pandas as pd

from app.indicators.combine import add_indicators 
from app.models.base import load_model
from app.models.controller import predict_signal 
from app.data_sources.collector import load_stock_data

app = FastAPI(title="Stock Analyzer Backend")

#load model at startup
model = load_model("random_forest.pkl")

@app.get("/")
def root():
    return {"message": "Stock Analyzer Backend is running."}

@app.get("/analyze")
def analyze(symbol: str = Query(..., description="Stock ticker symbol, e.g., AAPL")):
    try:
        #step 1: Get historical data
        # df = yf.download(symbol, period="6mo", interval="1d")
        df = load_stock_data(symbol)
        if df.empty:
            return {"error": "No data found for symbol."}
        
        #step 2: Add indicators
        df =  add_indicators(df)
        df.dropna(inplace=True) #Removing the rows with NAN indicators

        #step 3: Predict using the last row
        latest = df.iloc[-1:]
        prediction = predict_signal(model, latest)

        return {
            "symbol": symbol,
            "date": str(latest.index[0].date()),
            "prediction": prediction
        }
    except Exception as e:
        return {"error": str(e)}