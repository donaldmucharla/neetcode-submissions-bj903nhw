class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap = {}
        self.Left = Node(0, 0)
        self.Right = Node(0, 0)
        self.Left.next = self.Right
        self.Right.prev = self.Left

    def insert(self, node):
        prv, nxt = self.Right.prev,  self.Right
        prv.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prv
    
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
            self.insert(self.cacheMap[key])
            return self.cacheMap[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
        self.cacheMap[key] = Node(key, value)
        self.insert(self.cacheMap[key])

        if len(self.cacheMap) > self.capacity:
            lru = self.Left.next
            self.remove(lru)
            del self.cacheMap[lru.key]

        
