import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
import os

FEATURES = ['SMA', 'EMA', 'RSI', 'MACD', 'BB_UPPER', 'BB_LOWER', 'STOCH']
TARGET_COLUMN = 'Target'

def generate_target(df):
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    return df

def get_feature_target(df):
    df = df.dropna()
    X = df[FEATURES]
    y = df[TARGET_COLUMN]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def save_model(model, name="model.pkl"):
    joblib.dump(model, f"model/{name}")

def load_model(name="model.pkl"):
    return joblib.load(f"model/{name}")