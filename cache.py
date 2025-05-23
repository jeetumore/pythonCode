from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity:int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key:int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key:int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)





cache = LRUCache(2)  # Cache capacity is 2
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)      # Evicts key 2
print(cache.get(2))  # Output: -1 (not found)
cache.put(4, 4)      # Evicts key 1
print(cache.get(1))  # Output: -1 (not found)
print(cache.get(3))  # Output: 3
print(cache.get(4))  # Output: 4