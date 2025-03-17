from functions.hash import hash_function, shiftIndex
def add(stockSymbolList, stockNameList):
    stockName = input("Enter name ")
    stockSymbol = input("Enter symbol ")
    stockWKN= input("Enter wkn ")
    stockWknSymbol = stockSymbol , stockWKN
    stockWknName = stockName , stockWKN
    #1; Hash function(symbol(for hashing name)) -> creates index for Name in stockNameList
    #2; Name is saved in stockNameList
    name_index = hash_function(stockName)
    name_index = shiftIndex(name_index, stockNameList)
    if(name_index != 102):
        stockNameList[name_index] = stockWknName
        print(stockNameList)

    #1; Hash function(name(for hashing symbol)) -> create index for symbol in stockSymbolList
    #2; Symbol with WKO is saved in stockSymbolList
    symbol_index = hash_function(stockSymbol)
    symbol_index = shiftIndex(symbol_index, stockSymbolList)
    if(symbol_index != 102):
        stockSymbolList[symbol_index] = stockWknSymbol
        print(stockSymbolList)


    return 1
