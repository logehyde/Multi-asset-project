"""regimes.py

Implement regime classification logic:
- threshold-based regimes (growth/inflation)
- clustering (KMeans)
- Markov switching (statsmodels)
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def fit_regimes(df, n_clusters=4):
    """Fit a simple KMeans clustering on macro inputs (example).

    Returns a pd.Series of regime labels."""
    df2 = df[['SPY','AGG']].pct_change().dropna().fillna(0)
    X = df2.values
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
    regimes = pd.Series(kmeans.labels_, index=df2.index, name='regime')
    return regimes