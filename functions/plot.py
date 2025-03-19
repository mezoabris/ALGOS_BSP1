from functions.hash import hash_function
from functions.search_stock import search_stock
from functions.search_wkn import search_wkn
from classes.stockLine import stockLine
import matplotlib.pyplot as plt

def plotStock(stockSymbolList, StockNameList, stockList, search_input):
    stock_wkn = search_wkn(stockSymbolList, StockNameList, search_input)
    stock_index = search_stock(stock_wkn, stockList)
    linesOfStock = stockList[stock_index][1]
    stock_closeLast = []
    for line in linesOfStock:
        if isinstance(line, stockLine):
            line_price = float(line.closeLast.strip('$'))
            stock_closeLast.append(line_price)
            
    print(stock_closeLast)
    #print("drrrrrrrrrrrrrrrttfggfgggggggggghhhhjjuuuuuuuuuuuuujuiiiiiiiiiiiiiiiiiiiiiiiiiiikiktgztz")
    

    x_labels = list(range(1, len(stock_closeLast) + 1))

    # Plot the price trend
    plt.figure(figsize=(10, 5))
    plt.plot(x_labels, stock_closeLast, marker='o', linestyle='-', color='b', label='Price')
    
    # Formatting the chart
    plt.xlabel('Time (Days)')
    plt.ylabel('Price ($)')
    plt.title('Price Trend Chart')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.xticks(x_labels)  # Ensure all x-ticks are displayed
    plt.show()
