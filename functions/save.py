import json
from json import JSONEncoder
from classes.stockLine import EncodeList
def save(stockList, stockSymbolList, stockNameList):

    filenameStocks = input("Enter json filename for stocks:")
    filenameSymbol = input("Enter json filename for symbols:")
    filenameName = input("Enter json filename for names:")
   

    filenameStocks = "hashtables/" + filenameStocks
    filenameSymbol = "hashtables/" + filenameSymbol
    filenameName = "hashtables/" + filenameName

    with open(filenameStocks, "w") as file:
        json.dump(stockList, file, cls=EncodeList, indent=4)  
    with open(filenameSymbol, "w") as file:
        json.dump(stockSymbolList, file, cls=EncodeList, indent=4)  
    with open(filenameName, "w") as file:
        json.dump(stockNameList, file, cls=EncodeList, indent=4)  
