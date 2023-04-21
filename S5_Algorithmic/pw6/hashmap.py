from tp6.hachage import hachage
from tp6.item import Item


class HashMap:

    def __init__(self, max_size: int = 256):
        self.sentinelle = -1
        self.arr = [self.sentinelle] * max_size
        self.size = 0
        self.max_size = max_size

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def get(self, k: str):
        i = 0
        l = len(self.arr)
        index = int(hachage(k, l) + 0.5 * i + 0.5 * (i ** 2)) % l
        first_item = self.arr[index]
        while self.arr[index].key != k and self.arr[index] is not self.sentinelle:
            if self.arr[index] is first_item and i != 0:       #If it looped, the process stops
                break
            i += 1
            index = int(hachage(k, l) + 0.5 * i + 0.5 * (i ** 2)) % l
        if self.arr[index] is self.sentinelle or (self.arr[index] is first_item and i != 0):
            raise IndexError('Key not in HashMap')
        else:
            return self.arr[index].value

    def put(self, k: str, v: int):
        i = 0
        l = len(self.arr)
        index = int(hachage(k, l) + 0.5 * i + 0.5 * (i ** 2)) % l
        first_item = self.arr[index]
        while self.arr[index] is not self.sentinelle and self.arr[index] is not None:
            if self.arr[index] is first_item and i != 0:        #If it looped, the process stops
                break
            if self.arr[index].key == k:   #If the user tries to add a key that already exists, it overwrites the value
                self.arr[index].value = v
                break
            i += 1
            index = int(hachage(k, l) + 0.5 * i + 0.5 * (i ** 2)) % l
        if self.arr[index] is first_item and i != 0:
            self.rehash()       #If it looped, it means there's no more place so it rehashes
            self.put(k, v)      #And it adds the value in the new hashmap
        else:
            self.arr[index] = Item(k, v)
            self.size += 1
        if self.size >= self.max_size * 2 / 3:      #If the hashmap is quite filled, it automatically creates a new one
            self.rehash()                           #To keep the process efficient
        return self

    def delete(self, k: str):
        i = 0
        l = len(self.arr)
        index = int(hachage(k, l) + 0.5 * i + 0.5 * (i ** 2)) % l
        first_item = self.arr[index]
        while self.arr[index] is not self.sentinelle and self.arr[index].key != k:
            if self.arr[index] is first_item and i != 0: #If it looped, the process stops
                break
            i += 1
            index = int(hachage(k, l) + 0.5 * i + 0.5 * (i ** 2)) % l
        if self.arr[index] is self.sentinelle or (self.arr[index] is first_item and i != 0):
            raise IndexError('Key not in HashMap')
        else:
            self.arr[index] = None
            self.size -= 1
        return self

    def rehash(self):
        new_hashmap = HashMap(self.max_size * 2)  #Makes a twice as big hashmap
        for i in self.items():
            new_hashmap.put(i.key, i.value)
        self.max_size = new_hashmap.max_size
        self.arr = new_hashmap.arr
        return self

    def keys(self):
        for i in range(len(self.arr)):
            if self.arr[i] is not self.sentinelle and self.arr[i] is not None:
                yield self.arr[i].key

    def values(self):
        for k in self.keys():
            yield self.get(k)

    def items(self):
        for i in range(len(self.arr)):
            if self.arr[i] is not self.sentinelle and self.arr[i] is not None:
                yield self.arr[i]

    def __str__(self):
        if len(self) == 0:
            return '{}'
        s = '{'
        for i in range(len(self.arr)):
            if self.arr[i] is not self.sentinelle and self.arr[i] is not None:
                s += self.arr[i].key + ' : ' + str(self.arr[i].value) + ', '
        s = s[:-2] + '}'
        return s


if __name__ == '__main__':
    hashmap = HashMap()
    hashmap.put('abc', 12)
    hashmap.put('moi', 1)
    print(hashmap)
    hashmap.put('flo', 2)
    print(hashmap)
    hashmap.put('cro', 45)
    print(hashmap)
    hashmap.put('flo',18)
    print(hashmap)
