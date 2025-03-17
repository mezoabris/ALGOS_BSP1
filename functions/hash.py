def hash_function(word):
    print("the program enters the hashfunction")
    hash_index = 0
    for i in word:
        hash_index = hash_index + ord(i)
    hash_index = hash_index % 101
    return hash_index


def shiftIndex(hash_index, list):
    if(list[hash_index] != 0):
        print("Index is occupied value is shifted")
        for j in range(len(list)):
            hash_index = (hash_index + j*j)%101
            if(list[hash_index] == 0 or list[hash_index] == 1 ):
                print("value is inserted...")
                return hash_index
            if(j == len(list)):
                print("no more free space")
                return 102
    else:
        return hash_index
        #Shift value with quadratic probing