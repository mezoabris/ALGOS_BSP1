def compare(list, search_input, search_index):
    j = 1
    wkn = 0
    while True:
        if(list[search_index] != 0 and list[search_index] != 1):
            if search_input == list[search_index][0]:
                print("stock found")
                return search_index
            else:
                search_index = search_index + j*j
        elif(list[search_index] == 1):
            search_index = search_index + j*j
        else:
            break
        j+=1
    print("stock not found")
    return -1