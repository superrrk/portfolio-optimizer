import yfinance as yf

def fetch_price_data(tickers):
    data = yf.download(tickers, period='1y', auto_adjust=True)['Close']
    return data
