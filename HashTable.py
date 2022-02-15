
class HashTable:

    # initialize a HashTable object with a size and table attribute
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    # hash function for hashing a given key
    def generate_hash(self, key):
        hash = 1
        for char in key:
            hash *= ord(char)
        return hash

    # given a key, sort it using counting sort (different implementation than the book, explained in PDF)
    def counting_sort(self, key):
        anagram_encoding = [0]*26
        for char in key:
            anagram_encoding[ord(char)-97] += 1
        sorted = []
        for letter in range(26):
            sorted.append(chr(97 + letter) * anagram_encoding[letter])
        return ''.join(sorted)

    # adding key-value pairs to the HashTable
    def add(self, key, value):
    # hash the key
        hashed_key = self.generate_hash(key) % self.size
        # start a new chain
        if self.table[hashed_key] is None:
            # the value is held in an array
            self.table[hashed_key] = [[key, [value]]]
            return
        else:
            # if a branch exists at the index
            for key_value in self.table[hashed_key]:
                # check to see if the sorted key is present
                if key_value[0] == key:
                    # if present, append the value to the value array
                    key_value[1].append(value)
                    return
            # if a branch exists but the key isn't there, chain a key-value pair to the already existing one(s)
            self.table[hashed_key].append([key, [value]])
            return

    # getting values from HashTable
    def values(self):
        values = []
        for i in range(0, len(self.table)):
            # if a linked list exists
            if self.table[i]:
                # get all the anagrams on this branch
                for j in self.table[i]:
                    values.append(j[1])
        return values
