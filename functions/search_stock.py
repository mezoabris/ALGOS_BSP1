from functions.hash import hash_function, shiftIndex
from functions.search_wkn import compare
from classes.stockLine import stockLine

def search_stock(wkn, stockList):
    stock_index = hash_function(wkn)
    stock_index = compare(stockList, wkn, stock_index)
    linesOfStock = stockList[stock_index][1]
    line = linesOfStock[0]
    if isinstance(line, stockLine):
        print(line.date + line.closeLast+line.volume+line.open + line.high + line.low)
                

    

        


