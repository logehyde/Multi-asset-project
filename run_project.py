# Orchestration script to run a simple end-to-end pipeline demo using the starter modules.
import os
from src import data_pipeline, regimes, signals, portfolio, backtest, reporting

def main():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)

    print("Step 1: Load and prepare data")
    df = data_pipeline.load_and_prepare_data(data_dir)

    print("Step 2: Fit regimes")
    regimes_df = regimes.fit_regimes(df)

    print("Step 3: Build signals")
    sigs = signals.build_signals(df)

    print("Step 4: Construct portfolio")
    port = portfolio.construct_dynamic_portfolio(df, sigs, regimes_df)

    print("Step 5: Backtest")
    perf = backtest.run_demo_backtest(df, port)

    print("Step 6: Reporting")
    reporting.generate_report(df, perf, output_dir='reports')

    print('Done. Check the reports/ folder.')

if __name__ == '__main__':
    main()