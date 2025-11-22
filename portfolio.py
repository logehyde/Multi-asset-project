"""portfolio.py

Functions for portfolio construction and optimization:
- static allocations (60/40)
- risk parity
- dynamic allocations based on signals & regimes
"""
import pandas as pd
import numpy as np

def construct_static_60_40(df):
    return {'SPY': 0.6, 'AGG': 0.4}

def construct_dynamic_portfolio(df, signals_df, regimes_series):
    latest = signals_df.dropna().iloc[-1]
    w_spy = 0.6 + 0.2 * (1 if latest['spy_mom'] > 0 else -1)
    w_spy = max(0, min(1, w_spy))
    w_agg = 1 - w_spy
    return {'SPY': w_spy, 'AGG': w_agg}