import numpy as np
import pandas as pd
import torch

class BacktestTradingSystem:
    def __init__(self, initial_balance=10000, trading_fee=0.001):
        self.initial_balance = initial_balance
        self.trading_fee = trading_fee
        self.reset()

    def reset(self):
        self.balance = self.initial_balance
        self.position = 0  # Positive for long, negative for short
        self.trade_history = []

    def execute_trade(self, action, price):
        if action == "buy" and self.balance > 0:
            # Buy as much as possible with current balance
            quantity = self.balance / price
            self.balance -= quantity * price * (1 + self.trading_fee)
            self.position += quantity
            self.trade_history.append(("buy", price, quantity))
        elif action == "sell" and self.position > 0:
            # Sell all current holdings
            self.balance += self.position * price * (1 - self.trading_fee)
            self.trade_history.append(("sell", price, self.position))
            self.position = 0

    def calculate_pnl(self, current_price):
        # Calculate profit and loss
        return self.balance + self.position * current_price - self.initial_balance

    def backtest(self, data, strategy):
        """
        Backtest a given strategy on the provided candle data.
        :param data: A DataFrame with columns ['open', 'high', 'low', 'close'].
        :param strategy: A function that takes a row of data and returns 'buy', 'sell', or 'hold'.
        """
        self.reset()
        for index, row in data.iterrows():
            action = strategy(row)
            if action in ["buy", "sell"]:
                self.execute_trade(action, row['close'])
        # Calculate final PnL
        final_pnl = self.calculate_pnl(data.iloc[-1]['close'])
        return final_pnl, self.trade_history

def simple_moving_average_strategy(window=5):
    """
    A simple moving average crossover strategy.
    Buy when the close price is above the moving average, sell when it's below.
    """
    def strategy(row):
        if row['close'] > row['sma']:
            return "buy"
        elif row['close'] < row['sma']:
            return "sell"
        else:
            return "hold"
    return strategy

if __name__ == '__main__':
    # Generate dummy candle data
    np.random.seed(42)
    num_candles = 100
    prices = np.cumsum(np.random.randn(num_candles)) + 100  # Simulated price data
    data = pd.DataFrame({
        'open': prices + np.random.uniform(-1, 1, num_candles),
        'high': prices + np.random.uniform(0, 2, num_candles),
        'low': prices - np.random.uniform(0, 2, num_candles),
        'close': prices
    })

    # Calculate a simple moving average (SMA)
    window = 5
    data['sma'] = data['close'].rolling(window=window).mean()

    # Initialize backtesting system
    backtester = BacktestTradingSystem(initial_balance=10000, trading_fee=0.001)

    # Define strategy
    strategy = simple_moving_average_strategy(window=window)

    # Run backtest
    final_pnl, trade_history = backtester.backtest(data, strategy)

    # Print results
    print(f"Final PnL: {final_pnl}")
    print("Trade History:")
    for trade in trade_history:
        print(trade)