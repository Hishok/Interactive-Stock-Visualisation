import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Define the ticker symbols and indices you're interested in
tickers = ['SPY', 'ACWI', 'AAPL', 'MSFT', 'GOOGL']  # SPY for S&P 500, ACWI for FTSE All-World, plus some example companies

# Define the start and end dates for the data fetch
start_date = '2000-01-01'
end_date = pd.to_datetime('today').strftime('%Y-%m-%d')  # Fetches up to the current day

# Initialize a subplot
fig = make_subplots(rows=1, cols=1, shared_xaxes=True, vertical_spacing=0.02)

# Fetch data for each ticker and plot
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    fig.add_trace(go.Scatter(x=data.index, y=data['Adj Close'], mode='lines', name=ticker,
                             customdata=data[['Open', 'Close', 'Adj Close']],
                             hovertemplate="Ticker: " + ticker +
                                           "<br>Date: %{x}" +
                                           "<br>Open: $%{customdata[0]}" +
                                           "<br>Close: $%{customdata[1]}" +
                                           "<br>Adj Close: $%{customdata[2]}<extra></extra>"),
                  row=1, col=1)

# Update layout
fig.update_layout(title='Stock Prices Over Time',
                  xaxis_title='Date',
                  yaxis_title='Price',
                  hovermode='closest')

# Show the figure
fig.show()
