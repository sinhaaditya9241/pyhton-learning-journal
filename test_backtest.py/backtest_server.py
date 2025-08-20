# backtest_server.py
# Required libraries: Flask, Flask-Cors, pandas, numpy, yfinance
# Install them with: pip install Flask Flask-Cors pandas numpy yfinance

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import datetime
import yfinance as yf

# --- Initialize Flask App ---
app = Flask(__name__)
CORS(app) # Allow requests from the frontend

# --- Data Fetching ---
def fetch_stock_data(ticker, start_date_str, end_date_str):
    """
    Fetches historical stock data from Yahoo Finance.
    """
    # Download data from yfinance using auto_adjust=True for adjusted close prices
    # and progress=False to clean up console output.
    data = yf.download(ticker, start=start_date_str, end=end_date_str, auto_adjust=True, progress=False)
    
    # Handle cases where the ticker is invalid or no data is returned
    if data.empty:
        raise ValueError(f"No data found for ticker '{ticker}'. It may be an invalid symbol or delisted.")
        
    # Reset the index to make 'Date' a column
    data.reset_index(inplace=True)
    
    # Ensure we only return the columns we need
    return data[['Date', 'Close']]

# --- Backtesting Logic ---
def run_backtest(data, strategy, initial_capital=10000.0):
    """
    Runs a backtest on the provided data using the specified strategy.
    """
    if strategy == 'buy_and_hold':
        return run_buy_and_hold(data, initial_capital)
    elif strategy == 'ma_crossover':
        # Using 20-day and 50-day moving averages for this simulation
        return run_ma_crossover(data, 20, 50, initial_capital)
    else:
        raise ValueError("Unknown strategy")

def run_buy_and_hold(data, initial_capital):
    """Calculates the performance of a simple buy-and-hold strategy."""
    initial_price = data['Close'].iloc[0]
    
    # Calculate portfolio value for each day for the chart
    returns = data['Close'] / initial_price
    portfolio_values = initial_capital * returns
    
    final_value = portfolio_values.iloc[-1]
    total_return_pct = ((final_value - initial_capital) / initial_capital) * 100
    
    return {
        'metrics': {'final_value': final_value, 'total_return_pct': total_return_pct},
        'portfolio_values': portfolio_values.tolist()
    }

def run_ma_crossover(data, short_window, long_window, initial_capital):
    """
    Calculates performance of a moving average crossover strategy using a vectorized approach.
    """
    signals = pd.DataFrame(index=data.index)
    signals['price'] = data['Close']
    signals['short_ma'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_ma'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    
    # Generate buy/sell signals (1 for buy, 0 for hold/sell)
    signals['signal'] = 0.0
    # Use .loc for safe assignment to avoid ChainedAssignmentError
    signals.loc[signals.index[short_window:], 'signal'] = np.where(
        signals['short_ma'][short_window:] > signals['long_ma'][short_window:], 1.0, 0.0
    )
    
    # The position is the signal from the previous day
    signals['positions'] = signals['signal'].shift(1).fillna(0)

    # --- Vectorized Portfolio Calculation ---
    # Calculate daily returns of the stock
    daily_returns = signals['price'].pct_change().fillna(0)
    
    # Calculate strategy returns (we only make money when in a position)
    strategy_returns = signals['positions'] * daily_returns
    
    # Calculate the cumulative returns and the portfolio value over time
    cumulative_returns = (1.0 + strategy_returns).cumprod()
    portfolio_values = initial_capital * cumulative_returns
    
    final_value = portfolio_values.iloc[-1]
    total_return_pct = ((final_value - initial_capital) / initial_capital) * 100
    
    return {
        'metrics': {'final_value': final_value, 'total_return_pct': total_return_pct},
        'portfolio_values': portfolio_values.tolist()
    }

# --- API Endpoint ---
@app.route('/backtest', methods=['POST'])
def backtest_endpoint():
    """
    API endpoint to receive backtest parameters, run the simulation,
    and return the results.
    """
    try:
        params = request.get_json()
        ticker = params.get('ticker')
        start_date = params.get('start_date')
        end_date = params.get('end_date')
        strategy = params.get('strategy')

        if not all([ticker, start_date, end_date, strategy]):
            return jsonify({'error': 'Missing parameters'}), 400

        # 1. Fetch real stock data
        stock_data = fetch_stock_data(ticker, start_date, end_date)
        
        # 2. Run the selected strategy
        strategy_results = run_backtest(stock_data, strategy)
        
        # 3. Always run "Buy and Hold" for comparison
        buy_and_hold_results = run_backtest(stock_data, 'buy_and_hold')

        # 4. Format data for the response
        response_data = {
            'metrics': strategy_results['metrics'],
            'chart_data': {
                'dates': [d.strftime('%Y-%m-%d') for d in stock_data['Date']],
                'strategy_values': strategy_results['portfolio_values'],
                'buy_and_hold_values': buy_and_hold_results['portfolio_values']
            }
        }
        
        return jsonify(response_data)

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

# --- Run the Server ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)
