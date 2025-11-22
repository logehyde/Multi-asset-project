"""stress.py

Scenario analysis utilities:
- historical replay
- ad-hoc shocks to rates/equities/credit
"""
import pandas as pd

def historical_replay(price_df, start, end):
    return price_df.loc[start:end]

def apply_shock(price_df, shock_dict):
    shocked = price_df.copy()
    for asset, pct in shock_dict.items():
        if asset in shocked.columns:
            shocked.iloc[-1, shocked.columns.get_loc(asset)] = shocked.iloc[-1, shocked.columns.get_loc(asset)] * (1 + pct)
    return shocked