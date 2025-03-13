def hash_function(word, list):
    hash_index = 0
    for i in word:
        hash_index = hash_index + ord(i)
    hash_index = hash_index % 101
    print(hash_index)
    if(list[hash_index] == 0):
        print("value is inserted...")
    else:
        print("Index is occupied value is shifted")
        #Shift value with quadratic probing


