class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.capacity = capacity
        self.lt = []

    def get(self, key: int) -> int:
        result = -1
        if key in self.lru:
            result = self.lru[key]
            self.lt.append(self.lt.pop(self.lt.index(key)))
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key] = value
            self.lt.append(self.lt.pop(self.lt.index(key)))
        elif len(self.lru) < self.capacity:
            self.lru[key] = value
            self.lt.append(key)
        else:
            p = self.lt.pop(0)
            del self.lru[p]
            self.lru[key] = value
            self.lt.append(key)
        # print(self.lru)

# lRUCache  = LRUCache(2)
# lRUCache.put(1,1)
# lRUCache.put(2,2)
# lRUCache.get(1)
# lRUCache.put(3, 3)
# lRUCache.get(2)
# lRUCache.put(4, 4)
# lRUCache.get(1)
# lRUCache.get(3)
# lRUCache.get(4)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)