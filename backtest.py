"""backtest.py

Simple backtesting utilities:
- calculate portfolio returns given weights (static or time-varying)
- performance metrics (ann return, volatility, sharpe, max drawdown)
"""
import pandas as pd
import numpy as np

def portfolio_returns_from_weights(price_df, weights):
    rets = price_df.pct_change().dropna()
    port_ret = rets[list(weights.keys())].dot(pd.Series(weights))
    return port_ret

def performance_stats(returns, annualize=252):
    ann_ret = (1 + returns.mean())**annualize - 1
    ann_vol = returns.std() * (annualize**0.5)
    sharpe = ann_ret / ann_vol if ann_vol != 0 else np.nan
    cum = (1 + returns).cumprod()
    peak = cum.cummax()
    dd = (cum - peak) / peak
    max_dd = dd.min()
    return {'ann_return': ann_ret, 'ann_vol': ann_vol, 'sharpe': sharpe, 'max_drawdown': max_dd}

def run_demo_backtest(price_df, weights):
    port_ret = portfolio_returns_from_weights(price_df, weights)
    stats = performance_stats(port_ret)
    return stats