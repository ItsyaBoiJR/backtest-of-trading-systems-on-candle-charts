# Backtest of Trading Systems on Candle Charts

This repository contains an implementation of the concepts presented in the research paper **"Backtest of Trading Systems on Candle Charts"** by Stanislaus Maier-Paape and Andreas Platen. The paper introduces a methodology to backtest trading strategies using only candle chart data, addressing ambiguities in scenarios where trading signals cannot be uniquely determined. The provided implementation leverages Python and PyTorch to demonstrate the backtesting process for financial trading systems.

## Core Concept

The paper focuses on backtesting trading systems when only OHLC (Open-High-Low-Close) candle chart data is available, a common dataset format in financial markets. Backtesting is the process of evaluating a trading strategy's performance by simulating trades on historical data. However, ambiguities arise when dealing with certain situations in candle charts, such as:

1. **Order of Events**: Determining whether the high or low occurred first within a candle.
2. **Execution of Conditional Orders**: Handling cases where multiple conditions are met within the same candle.
3. **Partial Fills**: Addressing scenarios where an order is partially executed due to price fluctuations.

The authors propose strategies to resolve these ambiguities and provide a framework for implementing robust backtesting systems based on candle data.

## Repository Overview

This repository provides a Python/PyTorch-based implementation of the backtesting framework described in the paper. The code is designed to simulate and evaluate trading strategies using historical OHLC data. The implementation includes methods to handle ambiguous scenarios and supports flexible strategy definitions.

### Features

- **OHLC Data Parsing**: Load and preprocess historical candle chart data into a suitable format for backtesting.
- **Backtesting Engine**: Simulate trading strategies by processing OHLC data and applying user-defined trading rules.
- **Ambiguity Handling**: Implement strategies to resolve non-unique scenarios in candle chart data.
- **Performance Metrics**: Evaluate strategy performance using metrics such as profit/loss, win rate, and drawdown.

## Getting Started

### Prerequisites

To run this implementation, ensure you have Python installed along with the following dependencies:

- PyTorch
- Pandas
- NumPy
- Matplotlib (optional, for visualizations)

You can install the required packages using pip:

```bash
pip install torch pandas numpy matplotlib
```

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/candle-chart-backtesting.git
cd candle-chart-backtesting
```

### Usage

1. **Prepare Your Data**: Provide your historical OHLC data as a CSV file. Ensure the file contains the following columns:
   - `Open`
   - `High`
   - `Low`
   - `Close`
   - `Volume` (optional)

2. **Define Your Strategy**: Modify the `strategy.py` file to define your trading logic. Use the provided template to implement entry and exit conditions.

3. **Run the Backtest**: Execute the main script to perform the backtest:
   ```bash
   python backtest.py --data_path path_to_your_data.csv
   ```

4. **Analyze Results**: View the results, including performance metrics and optional visualizations of trades on the candle chart.

### Example

An example dataset and a sample moving average crossover strategy are included in the repository. To run the example:

```bash
python backtest.py --data_path example_data.csv
```

## Code Structure

- `data_loader.py`: Handles loading and preprocessing of OHLC data.
- `strategy.py`: Contains the template and examples for defining trading strategies.
- `backtest.py`: The main script for running the backtesting engine.
- `utils.py`: Includes utility functions for calculations and performance evaluation.
- `example_data.csv`: Sample OHLC data for demonstration purposes.

## Results

The backtesting engine outputs key performance metrics, including:

- Total profit/loss
- Win rate
- Maximum drawdown
- Return on investment (ROI)

Optional visualizations can be generated to display trades on the candle chart.

## References

- **Paper**: [Backtest of Trading Systems on Candle Charts](https://arxiv.org/pdf/1412.5558v1) by Stanislaus Maier-Paape and Andreas Platen.

## Contributing

Contributions to this repository are welcome. If you identify a bug, have a feature request, or want to contribute improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.