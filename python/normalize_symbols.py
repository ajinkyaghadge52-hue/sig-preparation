symbols = [" aapl ", "MSFT", " googl", "AAPL "]


#["AAPL", "MSFT", "GOOGL", "AAPL"]


def normalize(symbols):
    norm=[]
    for symbol in symbols:
        norm.append(symbol.strip().upper())


    return norm


print(normalize(symbols))