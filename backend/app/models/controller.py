from app.models import random_forest
from app.models.base import load_model, save_model

MODEL_MAP = {
    "random_forest": random_forest.train,
    #add more models here
}

def train_model(model_name, df):
    if model_name not in MODEL_MAP:
        raise ValueError("Unsupported model")

    model, accuracy = MODEL_MAP[model_name](df)
    save_model(model, f"{model_name}.pkl")
    return model, accuracy

def predict_signal(model, latest_row_df):
    X = latest_row_df[['SMA', 'EMA', 'RSI', 'MACD', 'BB_UPPER', 'BB_LOWER', 'STOCH']]
    y_pred = model.predict(X)[0]
    return "BUY" if y_pred == 1 else "SELL"