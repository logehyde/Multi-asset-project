"""signals.py

Build cross-asset signals:
- trend (momentum)
- carry (placeholder)
- volatility filters
"""
import pandas as pd
import numpy as np

def momentum(series, window=252):
    return series.pct_change(window)

def build_signals(df):
    signals = {}
    signals['spy_mom'] = momentum(df['SPY'])
    signals['agg_mom'] = momentum(df['AGG'])
    signals_df = pd.DataFrame(signals)
    return signals_df