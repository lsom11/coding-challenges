class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.deque = deque()
        self.cache = {}   
    def get(self, key):
        if key in self.cache:
            val = self.cache[key]
            self._remove(key)
            self.deque.append((key,val))
            return val
        return -1
    def put(self, key, value):
        if key in self.cache:
            self._remove(key)
        self.deque.append((key,value))
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            k, v = self.deque.popleft()
            del self.cache[k]
    def _remove(self, key):
        for k, v in self.deque:
                if k == key:
                    self.deque.remove((k, v))
                    break


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)