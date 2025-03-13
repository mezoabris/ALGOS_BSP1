def hash_function(word):
    hash_value = 0
    for i, letter in enumerate(word):
        hash_value += ord(letter) * (i + 1)
    return hash_value

strings = ["apple", "tesla", "microsoft", "meta", "amazon", "google", "qualcomm", "cisco", "starbucs"]
hashtable = [0] * 101

for word in strings:
    hash_value = hash_function(word)  # Use the better_hash function
    position = hash_value % 101  # Get the position in the hashtable

    if hashtable[position] == 0:
        hashtable[position] = word
    else:
        print(word + " at position " + str(position) + " is already taken.")

print(hashtable)