class MyHashSet:

    def __init__(self):
        self.Hashset = set()

    def add(self, key: int) -> None:
        self.Hashset.add(key)
        
    def remove(self, key: int) -> None:
        if key in self.Hashset:
            self.Hashset.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.Hashset:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)