from functions.hash import hash_function
from functions.search_stock import search_stock
from functions.search_wkn import search_wkn
import matplotlib

def plotStock(stockSymbolList, StockNameList, stockList, search_input):
    stock_wkn = search_wkn(stockSymbolList, StockNameList, search_input)
    search_stock(stock_wkn, stockList)
    #print("drrrrrrrrrrrrrrrttfggfgggggggggghhhhjjuuuuuuuuuuuuujuiiiiiiiiiiiiiiiiiiiiiiiiiiikiktgztz")
    


