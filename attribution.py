"""attribution.py

Simplified return and risk attribution functions.
"""
import pandas as pd

def contribution_to_return(returns, weights):
    rets = returns.mean()
    contrib = rets * pd.Series(weights)
    return contrib / contrib.sum()