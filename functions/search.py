from functions.hash import hash_function, shiftIndex

def search(stockSymbolList, stockNameList):
    charCounter = 0
    search_input = input("enter name or symbol: ")
    search_index = hash_function(search_input)
    print(search_index)



    if len(search_input) <= 4:
        print("its a symbol")
        compare(stockSymbolList, search_input, search_index)
            

    else:
        print("its a name")
        compare(stockNameList, search_input, search_index)

def compare(list, search_input, search_index):
    j = 1

    while True:
        if(list[search_index] != 0 and list[search_index] != 1):
            if search_input == list[search_index][0]:
                print(list[search_index][0])
                return True
            else:
                search_index = search_index + j*j
        elif(list[search_index] == 1):
            search_index = search_index + j*j
        else:
            print("stock not found")
            break
        j+=1
    return False