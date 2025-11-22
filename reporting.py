"""reporting.py

Generate plots and save simple reports. Use Plotly or Matplotlib for charts.
"""
import os
import matplotlib.pyplot as plt

def generate_report(price_df, perf_stats, output_dir='reports'):
    os.makedirs(output_dir, exist_ok=True)
    fig, ax = plt.subplots()
    try:
        price_df[['SPY','AGG']].pct_change().cumsum().plot(ax=ax)
    except Exception:
        ax.text(0.5, 0.5, 'No data to plot', ha='center')
    ax.set_title('Cumulative Returns (sample)')
    fig_path = os.path.join(output_dir, 'cumulative_returns.png')
    fig.savefig(fig_path)
    plt.close(fig)
    summary_path = os.path.join(output_dir, 'summary.txt')
    with open(summary_path, 'w') as f:
        f.write(str(perf_stats))
    return {'fig': fig_path, 'summary': summary_path}