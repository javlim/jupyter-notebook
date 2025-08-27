import yfinance as yf

def get_stock_data(ticker: str, start_date: str, end_date: str):
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    return df