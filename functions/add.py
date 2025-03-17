from functions.hash import hash_function, shiftIndex
def add(stockSymbols, stockNames):
    stockName = input("Enter name ")
    stockSymbol = input("Enter symbol ")
    stockWKN= input("Enter wkn ")
    #1; Hash function(symbol(for hashing name)) -> creates index for Name in stockNames
    #2; Name is saved in stockNames
    name_index = hash_function(stockName, stockNames)
    name_index = shiftIndex(name_index, list)
    if(name_index != 102):
        stockNames[name_index] = stockName

    #1; Hash function(name(for hashing symbol)) -> create index for symbol in stockSymbols
    #2; Symbol with WKO is saved in StockSymbols
    hash_function


    return 1
