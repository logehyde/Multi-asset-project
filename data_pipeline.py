"""data_pipeline.py

Responsibilities:
- Download or load raw data from CSV / APIs
- Clean and align time series (resampling, forward/backfill)
- Persist processed data to disk for reproducibility
"""
import os
import pandas as pd

def load_and_prepare_data(data_dir):
    """Example loader. Replace with API pulls (FRED, Bloomberg) or CSV readers.

    Returns
    -------
    pd.DataFrame
        A wide-format DataFrame indexed by date containing asset prices and macro series.
    """
    sample_csv = os.path.join(data_dir, 'sample_prices.csv')
    if os.path.exists(sample_csv):
        df = pd.read_csv(sample_csv, parse_dates=['date']).set_index('date')
        return df
    dates = pd.date_range('2010-01-01', '2023-12-31', freq='B')
    assets = pd.DataFrame(index=dates)
    assets['SPY'] = 100 * (1 + 0.0002).cumprod()
    assets['AGG'] = 100 * (1 + 0.0001).cumprod()
    assets.index.name = 'date'
    return assets