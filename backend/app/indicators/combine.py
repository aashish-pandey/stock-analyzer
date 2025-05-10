from .sma import calculate_sma
from .ema import calculate_ema
from .rsi import calculate_rsi
from .macd import calculate_macd
from .bollinger import calculate_bollinger
from .stochastic import calculate_stochastic
from .obv import calculate_obv


def add_indicators(df):
    df['SMA'] = calculate_sma(df)
    df['EMA'] = calculate_ema(df)
    df['RSI'] = calculate_rsi(df)
    df['MACD'] = calculate_macd(df)
    df['BB_UPPER'], df['BB_LOWER'] = calculate_bollinger(df)
    df['STOCH'] = calculate_stochastic(df)
    # df['OBV'] = calculate_obv(df)
    return df

