import numpy as np
from scipy.optimize import minimize
import yfinance as yf
import pandas as pd

def compute_efficient_frontier(prices):
    try:
        # Calculate log returns and clean up any missing data
        log_returns = np.log(prices / prices.shift(1)).dropna()
        mean_returns = log_returns.mean()
        cov_matrix = log_returns.cov()
        
        num_assets = len(mean_returns)
        results = {
            'risks': [],
            'returns': [],
            'weights': []
        }

        # Generate points along the efficient frontier
        return_range = np.linspace(mean_returns.min(), mean_returns.max(), 50)
        for target_return in return_range:
            def objective(weights):
                return np.sqrt(weights.T @ cov_matrix @ weights)  # Standard deviation

            constraints = [
                {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},  # Weights sum to 1
                {'type': 'eq', 'fun': lambda x: x @ mean_returns - target_return}  # Target return
            ]
            bounds = tuple((0, 1) for _ in range(num_assets))  # Weights between 0 and 1
            init_guess = np.ones(num_assets) / num_assets  # Equal weight initial guess

            try:
                result = minimize(
                    objective, 
                    init_guess, 
                    method='SLSQP',
                    bounds=bounds,
                    constraints=constraints
                )
                
                if result.success:
                    results['risks'].append(float(result.fun))  # Convert to float for JSON serialization
                    results['returns'].append(float(target_return))
                    results['weights'].append([float(w) for w in result.x])  # Convert to list of floats
            except:
                continue  # Skip failed optimizations

        # Sort results by risk
        if results['risks']:
            sorted_indices = np.argsort(results['risks'])
            results['risks'] = [results['risks'][i] for i in sorted_indices]
            results['returns'] = [results['returns'][i] for i in sorted_indices]
            results['weights'] = [results['weights'][i] for i in sorted_indices]
            
        return results
    except Exception as e:
        raise Exception(f"Error in portfolio optimization: {str(e)}")

def fetch_price_data(tickers):
    data = yf.download(tickers, period='1y', auto_adjust=True)['Close']
    data = data.dropna(axis=0, how='all')  # Drop days with all NaNs
    data = data.dropna(axis=1, how='any')  # Drop tickers with missing data

    print("Cleaned data columns:", data.columns.tolist())
    return data
