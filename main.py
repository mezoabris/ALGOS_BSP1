import csv
from classes.stockLine import stockLine
from functions.add import add

testObj = stockLine("h", "s", "s", "t", "d", "sechs")
maxIndex = 101


print("1. ADD\n 2. DEL\n 3. IMPORT \n4. SEARCH \n5. PLOT \n 6. SAVE \n7. LOAD \n8. QUIT")
while(True):
    option = int(input("select an option:"))
    match option:
        case 1:
            print("add")
            print(testObj.high)
        case 2:
            print("del")
        case 3:
            print("import")
        case 4:
            print("SEARCH")
        case 5:
            print("PLOT")
        case 6:
            print("SAVE")
        case 7:
            print("LOAD")
        case 8:
            print("QUIT")
        case _:
            print("invalid")
            break
        


