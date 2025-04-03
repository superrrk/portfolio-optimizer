import numpy as np
from scipy.optimize import minimize
import yfinance as yf
import pandas as pd

def compute_efficient_frontier(prices):
    log_returns = np.log(prices / prices.shift(1)).dropna()
    mean_returns = log_returns.mean()
    cov_matrix = log_returns.cov()
    
    num_assets = len(mean_returns)
    results = {
        'risks': [],
        'returns': [],
        'weights': []
    }

    for target_return in np.linspace(mean_returns.min(), mean_returns.max(), 50):
        def objective(weights):
            return weights.T @ cov_matrix @ weights

        constraints = (
            {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
            {'type': 'eq', 'fun': lambda x: x @ mean_returns - target_return}
        )
        bounds = tuple((0, 1) for _ in range(num_assets))
        init_guess = np.ones(num_assets) / num_assets

        result = minimize(objective, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        if result.success:
            results['risks'].append(np.sqrt(result.fun))
            results['returns'].append(target_return)
            results['weights'].append(result.x.tolist())

        print('Mean returns:', mean_returns)
        print('Cov matrix:', cov_matrix)
        print('Result:', result)


    return results

def fetch_price_data(tickers):
    data = yf.download(tickers, period='1y', auto_adjust=True)['Close']
    data = data.dropna(axis=0, how='all')  # Drop days with all NaNs
    data = data.dropna(axis=1, how='any')  # Drop tickers with missing data

    print("Cleaned data columns:", data.columns.tolist())
    return data
