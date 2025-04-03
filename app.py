from flask import Flask, render_template, request, jsonify
from portfolio.optimizer import compute_efficient_frontier
from portfolio.data import fetch_price_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    tickers = [t.strip().upper() for t in request.json['tickers']]
    prices = fetch_price_data(tickers)

    if prices.empty:
        return jsonify({"error": "No valid data found. Check your ticker symbols."}), 400

    results = compute_efficient_frontier(prices)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)



