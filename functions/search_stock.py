from functions.hash import hash_function, shiftIndex
from functions.search_wkn import compare
from classes.stockLine import stockLine

def search_stock(wkn, stockList):
    stock_index = hash_function(wkn)
    stock_index = compare(stockList, wkn, stock_index)
    return stock_index
    
                

    

        


