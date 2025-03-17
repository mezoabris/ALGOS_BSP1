import csv
from classes.stockLine import stockLine
from functions.search import search
from functions.hash import hash_function, shiftIndex

def importstock(stockLines, stockList, stockSymbolList, stockNameList):
    stockName = input("Enter csv file name form stock directory ")
    stockName = "stocks/" + stockName 
    stockNameOrSymbol = input("Enter stock name or symbol ")

    ########Getting csv file and create a list of stockLine objects########
    countLines = 0
    with open(stockName, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            # Access each element in the row
            if(countLines < 30):
                stockObject = stockLine(row[0], row[1], row[2], row[3], row[4], row[5])
                stockLines[countLines] = stockObject
                countLines +=1
            else:
                print("Too many lines")
    ########1:Search for wkn 2: Create hash from WKN 3: save list in stockLines in stockList########
    wkn = search(stockSymbolList, stockNameList, stockNameOrSymbol)
    print(wkn)
    index_for_stockLines = hash_function(wkn)
    index_for_stockLines = shiftIndex(index_for_stockLines, stockList)
    if(index_for_stockLines != 102):
        stockList[index_for_stockLines] = stockLines

                
    
            



