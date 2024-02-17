# Interactive Stock Price Dashboard

This project creates an interactive dashboard to visualize how stock prices have changed over time from 01/01/2000 to the present day. It includes features to view the open, close, and adjusted close prices when hovering over each ticker symbol's line in the chart. The dashboard supports multiple ticker symbols, including indices like the S&P 500 and FTSE All-World.

## Requirements

- Python
- Pandas
- yfinance
- Plotly

## Installation

Ensure you have Python installed on your system. Then, install the required Python libraries using pip:

```bash
pip install yfinance pandas plotly
```

## Usage
1. The script fetches stock data for specified ticker symbols and indices, then plots them in an interactive chart using Plotly. To use the script:

2. Define the ticker symbols you're interested in within the tickers list in the script. The example includes SPY for the S&P 500 and ACWI for the FTSE All-World, along with other company symbols like AAPL, MSFT, and GOOGL.
3. Run the script to fetch data and generate the dashboard.

## Author
Hisho Rajanathan