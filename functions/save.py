import json
from json import JSONEncoder
from classes.stockLine import EncodeList
def save(listToSave):

    print(EncodeList().encode(listToSave))
    filename = input("Enter json filename:")
    filename = "hashtables/" + filename
    with open(filename, "w") as file:
        json.dump(listToSave, file, cls=EncodeList, indent=4)  
