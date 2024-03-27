import hashlib

class Node:
    def __init__(self, key, value, next : Node) -> None:
        self.key = key
        self.value = value
        self.next = next

class ChainedHash :
    def __init__(self, capacity:int) :
        self.capacity = capacity
        self.table = [None] * self.capacity
    def hash_value(self, key) :
        if isinstance(key,int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(),16)%self.capacity)
    def search(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]
        
        while p is not None:
            if p.key == key:
                return False
            p = p.next
        
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
