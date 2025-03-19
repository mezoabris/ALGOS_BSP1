import csv
from classes.stockLine import stockLine
from functions.add import add
from functions.search_wkn import search_wkn
from functions.importstock import importstock
from functions.search_stock import search_stock
from functions.save import save
from functions.delete import deleteStock
from functions.load import load

stockLines = [0] * 30
stockList = [0] * 101

stockSymbolList = [0] * 101
stockNameList = [0] * 101


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
            search_input = input("enter name or symbol: ")
            wkn = search_wkn(stockSymbolList, stockNameList, search_input)
            search_stock(wkn, stockList)
            print("SEARCH")
        case 5:
            print("PLOT")
        case 6:
            save(stockList,stockSymbolList, stockNameList)
            print("SAVE")
        case 7:
            print("LOAD")
            load(stockList, stockLines, stockNameList, stockSymbolList)
        case 8:
            print("QUIT")
            break
        case _:
            print("invalid")
            break
        


