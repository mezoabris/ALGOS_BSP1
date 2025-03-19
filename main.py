import csv
from classes.stockLine import stockLine
from functions.add import add
from functions.search_wkn import search_wkn
from functions.importstock import importstock
from functions.search_stock import search_stock
from functions.save import save
from functions.delete import deleteStock
from functions.load import load
from functions.plot import plotStock

stockLines = [0] * 30
stockList = [0] * 1009

stockSymbolList = [0] * 1009
stockNameList = [0] * 1009


testObj = stockLine("h", "s", "s", "t", "d", "sechs")



print("1. ADD\n 2. DEL\n 3. IMPORT \n4. SEARCH \n5. PLOT \n 6. SAVE \n7. LOAD \n8. QUIT")
while(True):
    option = int(input("select an option:"))
    match option:
        case 1:
            print("add")
            add(stockSymbolList, stockNameList)
        case 2:
            print("del")
            deleteStock(stockNameList, stockSymbolList, stockList)

        case 3:
            print("import")
            importstock(stockLines, stockList, stockSymbolList, stockNameList)
        case 4:
            print("SEARCH")
            search_input = input("enter name or symbol: ")
            wkn = search_wkn(stockSymbolList, stockNameList, search_input)
            stock_index = search_stock(wkn, stockList)
            linesOfStock = stockList[stock_index][1]
            line = linesOfStock[0]
            if isinstance(line, stockLine):
                print(line.date + line.closeLast+line.volume+line.open + line.high + line.low)
        case 5:
            print("PLOT")
            search_input = input("enter name or symbol: ")
            plotStock(stockSymbolList, stockNameList, stockList, search_input)
        case 6:
            save(stockList,stockSymbolList, stockNameList)
            print("SAVE")
        case 7:
            print("LOAD")
            search_input = input("enter name or symbol: ")
            load(stockList, stockLines, stockNameList, stockSymbolList)
        case 8:
            print("QUIT")
            break
        case _:
            print("invalid")
            break
        


