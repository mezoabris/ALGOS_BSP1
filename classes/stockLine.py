class stockLine:
     def __init__(self, date, closeLast,volume, open, high, low):
        self.date = date
        self.closeLast = closeLast
        self.volume = volume
        self.open = open
        self.high = high
        self.low = low

class stocks:
      def __init__(self, symbol, stockName):
        self.symbol = symbol
        self.stocks = stockName
