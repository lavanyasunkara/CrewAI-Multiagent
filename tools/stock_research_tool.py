import yfinance as yf
from crewai.tools import tool
@tool("Live stock information tool")
def get_stock_price(stock_symbol:str)->str:
    """
    Retrieves latest stock price and other relevant info for a given stock symbol using yahoo finance

    parameters:
    stock_symbol(str):The ticker symbol of the stock(e.g. TSLA,MSFT,AAPL)

    returns:
    str: A summary of the stock's current price, daily change and other key dates
    """

    stock = yf.Ticker(stock_symbol)
    info = stock.info
    #print(info)
    current_price = info.get("regularMarketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency = info.get("currency","USD")

    if current_price is None:
        return f"could not fetch price for {stock_symbol}. Please check the symbol"

    return (f"stock: {stock_symbol.upper()}\n"
            f"price: {current_price} {currency}\n"
            f"change: {round(change_percent,2)}%")


#print(get_stock_price("AAPL"))