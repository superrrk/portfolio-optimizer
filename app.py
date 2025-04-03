from flask import Flask, render_template, request, jsonify
from portfolio.optimizer import compute_efficient_frontier
from portfolio.data import fetch_price_data
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    try:
        data = request.get_json()
        if not data or 'tickers' not in data:
            return jsonify({"error": "No tickers provided"}), 400

        tickers = [t.strip().upper() for t in data['tickers']]
        
        if len(tickers) < 2:
            return jsonify({"error": "Please provide at least 2 tickers"}), 400

        prices = fetch_price_data(tickers)

        if prices.empty:
            return jsonify({"error": "No valid data found. Check your ticker symbols."}), 400

        results = compute_efficient_frontier(prices)
        return jsonify(results)

    except Exception as e:
        app.logger.error(f"Error in optimization: {str(e)}")
        return jsonify({"error": "An error occurred during optimization"}), 500

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"Server Error: {error}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



