class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for i in range(self.size)]

    def add(self, key: int) -> None:
        index = key % self.size
        if key not in self.bucket[index]:
            self.bucket[index].append(key)        

    def remove(self, key: int) -> None:
        index = key % self.size
        if key in self.bucket[index]:
            self.bucket[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.size
        return key in self.bucket[index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)