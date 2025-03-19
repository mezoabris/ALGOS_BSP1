from classes.stockLine import stocks, stockLine
import json

def load(stockList, stockLines, stockNameList, stockSymbolList):
    with open('hashtables/stock.json', 'r') as openfile:
        json_to_hashtable = json.load(openfile)
    
    countItemsInStockList = 0
    countItemsInstockLinesList = 0
    for stock in json_to_hashtable:
        if(stock != 0 and stock != 1):
            print(stock)
            for line in stock[1]:
            
                if(line != 0 and line != 1):
                    #stock_wkn = line[0]
                    
                    stockLineObject = stockLine(line["date"], line["closeLast"], line["volume"], line["open"], line["high"], line["low"])
                    #stockLines[countItemsInstockLinesList][0] = stock[0]
                    stockLines[countItemsInstockLinesList] = stockLineObject
                    
                    
                else:
                    stockLines[countItemsInstockLinesList] = line
                countItemsInstockLinesList+=1
            stockList[countItemsInStockList] =  [stock[0], stockLines]
        else:
            stockList[countItemsInStockList] = stock
        countItemsInStockList+=1

    
    print(stockList)

    with open('hashtables/name.json', 'r') as openfile:
        json_to_hashtable = json.load(openfile)
    
    countItemsInStockNameList = 0
    
    for stock_name_list_element in json_to_hashtable:
        if(stock_name_list_element != 0 and stock_name_list_element != 1):
            stock_name = stock_name_list_element[0]
            stock_wkn = stock_name_list_element[1]
            stockNameList[countItemsInStockNameList] = [stock_name, int(stock_wkn)]
        else:
            stockNameList[countItemsInStockNameList] = stock_name_list_element
        countItemsInStockNameList+=1
            

    print(stockNameList)

    with open('hashtables/symbol.json', 'r') as openfile:
        json_to_hashtable = json.load(openfile)
    countItemsInStockSymbolList = 0
    
    for stock_symbol_element in json_to_hashtable:
        if(stock_symbol_element != 0 and stock_symbol_element != 1):
            stock_symbol = stock_symbol_element[0]
            stock_wkn = stock_symbol_element[1]
            stockSymbolList[countItemsInStockSymbolList] = [stock_symbol, int(stock_wkn)]

        else:
            stockSymbolList[countItemsInStockSymbolList] = stock_symbol_element
        countItemsInStockSymbolList+=1
    

    print(stockSymbolList)