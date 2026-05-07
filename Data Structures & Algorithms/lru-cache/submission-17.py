class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Cache = {}
        self.left = Node(0, 0) 
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        self.right.prev = node
        node.next = self.right

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.Cache:
            self.remove(self.Cache[key])
            self.insert(self.Cache[key])
            return self.Cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.Cache:
            self.remove(self.Cache[key])
        self.Cache[key] = Node(key, value)
        self.insert(self.Cache[key])


        if len(self.Cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.Cache[lru.key]


        
