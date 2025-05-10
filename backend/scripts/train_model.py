import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd

from app.indicators.combine import add_indicators
from app.models.controller import train_model

df = pd.read_csv("data/AAPL.csv", parse_dates=['Date'])
df.set_index('Date', inplace=True)
df = add_indicators(df)

model, acc = train_model("random_forest", df)
print(f"Model trained. Accuracy: {acc:.2f}")