from functions.search_wkn import search_wkn 
from functions.hash import hash_function 
from functions.compare import compare
def deleteStock(stockNameList, stockSymbolList, StockList):
    ####### WE TAKE THE STOCK NAME AND SYMBOL AND FIND ITS POSITION ######
    stockName = input("enter the name of the stock ")
    stockSymbol = input("enter the symbol of the stock: ")
    name_index = hash_function(stockName)
    name_index = compare(stockNameList, stockName, name_index)
    symbol_index = hash_function(stockSymbol)
    symbol_index = compare(stockSymbolList, stockSymbol, symbol_index)
    ####################################################################

           # if the return from compare() isnt -1 -> the stock exists#
           # we can overwirte the values using a tumbstone ############
    if name_index != -1 and symbol_index != -1 :
        stock_wkn = search_wkn(stockSymbolList, stockNameList, stockName)
        stockNameList[name_index] = 1
        stockSymbolList[symbol_index] = 1
        StockList[hash_function(stock_wkn)] = 1
        print(stockNameList)
        print(stockSymbolList)
        print(StockList)
        print("stock deleted")
    ######################################################################
    else:
    ######otherwise we dont delete anything###############################
        print("you cant delete a non-existing file")
    ######################################################################
    