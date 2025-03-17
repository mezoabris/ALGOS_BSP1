import csv
from classes.stockLine import stockLine
from functions.add import add
from functions.search import search

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
        case 3:
            print("import")
        case 4:
            search(stockSymbolList, stockNameList)
            print("SEARCH")
        case 5:
            print("PLOT")
        case 6:
            print("SAVE")
        case 7:
            print("LOAD")
        case 8:
            print("QUIT")
            break
        case _:
            print("invalid")
            break
        


