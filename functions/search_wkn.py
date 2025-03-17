from functions.hash import hash_function, shiftIndex
from functions.compare import compare
def search_wkn(stockSymbolList, stockNameList, search_input):
    search_index = hash_function(search_input)

    if len(search_input) <= 4:
        print("symbol recognized")
        search_index = compare(stockSymbolList, search_input, search_index)
        wkn = str(stockSymbolList[search_index][1])
    else:
        print("name recognized")
        search_index = compare(stockNameList, search_input, search_index)
        wkn = str(stockNameList[search_index][1])
    return wkn


