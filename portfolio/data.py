import pandas_datareader.data as web
from datetime import datetime, timedelta
import pandas as pd

def fetch_price_data(tickers):
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        
        # Fetch data for each ticker and combine
        dfs = []
        for ticker in tickers:
            try:
                df = web.DataReader(ticker, 'stooq', start_date, end_date)
                df = df['Close'].rename(ticker)
                dfs.append(df)
            except Exception as e:
                print(f"Error fetching data for {ticker}: {str(e)}")
                continue
        
        if not dfs:
            return pd.DataFrame()
        
        # Combine all dataframes
        combined_df = pd.concat(dfs, axis=1)
        # Forward fill missing values and drop any remaining NaN
        combined_df = combined_df.fillna(method='ffill').dropna()
        
        return combined_df
    except Exception as e:
        print(f"Error in fetch_price_data: {str(e)}")
        return pd.DataFrame()
