from functions.hash import hash_function
def add(stockSymbols, stockNames):
    stockName = input("Enter name ")
    stockSymbol = input("Enter symbol ")
    stockWKN= input("Enter wkn ")
    hash_function(stockName)
    #1; Hash function(symbol(for hashing name)) -> creates index for Name in stockNames
    #2; Name is saved in stockNames

    #1; Hash function(name(for hashing symbol)) -> create index for symbol in stockSymbols
    #2; Symbol with WKO is saved in StockSymbols


    return 1
