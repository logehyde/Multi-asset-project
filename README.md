# Dynamic Multi-Asset Allocation Project 

This project is a fully modular, Python-based framework for researching and backtesting multi-asset allocation strategies.
It combines macro regime classification, cross-asset factor & momentum signals, portfolio construction, and stress testing & scenario simulation.

This repository is structured exactly like a front-office research environment at a multi-asset fund.

**Repository structure**
```
Multi-Asset-Project/
│
├── data/                    # Sample datasets & macro inputs
├── notebooks/               # Exploratory analysis (Jupyter notebooks)
├── src/                     # Core Python modules (production-ready)
│   ├── data_pipeline.py     # Data ingestion, cleaning, alignment
│   ├── regimes.py           # Macro regimes (clustering / threshold models)
│   ├── signals.py           # Trend, carry, volatility filters
│   ├── portfolio.py         # Portfolio construction logic
│   ├── backtest.py          # Backtesting engine & performance statistics
│   ├── stress.py            # Historical scenarios, shocks
│   ├── attribution.py       # Return & risk attribution
│   ├── reporting.py         # Automated plots and summaries
│   └── utils.py             # Helper functions
│
├── reports/                 # Generated plots / summaries
├── run_project.py           # Full pipeline runner (end-to-end demo)
├── requirements.txt         # Python dependencies
├── LICENSE
└── README.md                # Project documentation


Uploaded resume (for context) at: `/mnt/data/Logan Hyde Resume.pdf`
