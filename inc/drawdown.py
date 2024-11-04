import yfinance as yf
from datetime import datetime

def calculate_max_drawdown(portfolio):
    
  # Yahoo Finance codes for each asset (excluding "Bond" as it has no drawdown)
  bond = portfolio.pop('Bond',None)
  tickers = list(portfolio.keys())

  # Download historical data for ETFs
  now = datetime.now().strftime("%Y-%m-%d")
  data = yf.download(tickers, start='1980-01-01', end=now)['Adj Close']

  # We add the Bond component as a constant value for each date
  if bond is not None:
    data['Bond'] = bond

  # We calculate the daily value of each asset by multiplying the price by the invested amount
  for ticker, investment in portfolio.items():
    if ticker != 'Bond':  # We ignore the Bond because it is already fixed
      first_valid_index = data[ticker].first_valid_index()
      initial_value = data[ticker].loc[first_valid_index] if first_valid_index is not None else 1

      data[ticker] = data[ticker] * (float(investment) / initial_value)

  # We add the values ​​of all the components to obtain the total value of the portfolio.
  data['PortfolioValue'] = data[list(portfolio.keys())].sum(axis=1)

  # Calculate max drawdown
  data['CumulativeMax'] = data['PortfolioValue'].cummax()
  data['Drawdown'] = (data['PortfolioValue'] - data['CumulativeMax']) / data['CumulativeMax']
  max_drawdown = data['Drawdown'].min()

  # Result
  return {
    'drawdown': round((max_drawdown*-1)*100,2)
  }