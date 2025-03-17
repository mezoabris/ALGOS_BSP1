from functions.hash import hash_function, shiftIndex

def search(stockSymbolList, stockNameList, search_input):
    search_index = hash_function(search_input)

    if len(search_input) <= 4:
        print("symbol recognized")
        wkn = compare(stockSymbolList, search_input, search_index)
    else:
        print("name recognized")
        wkn = compare(stockNameList, search_input, search_index)
    return wkn


def compare(list, search_input, search_index):
    j = 1
    wkn = 0
    while True:
        if(list[search_index] != 0 and list[search_index] != 1):
            if search_input == list[search_index][0]:
                print("stock found")
                wkn = str(list[search_index][1])
                print(wkn)
                return wkn
            else:
                search_index = search_index + j*j
        elif(list[search_index] == 1):
            search_index = search_index + j*j
        else:
            print("stock not found")
            break
        j+=1
    print("stock not found")