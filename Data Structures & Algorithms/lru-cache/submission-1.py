class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.count = 0
        self.time = []
        self.real = {}
        self.current = 0
        self.value = {}

        

    def get(self, key: int) -> int:
        self.current += 1
        if key in self.value:
            self.real[key] = self.current
            heapq.heappush(self.time, (self.current, key))
            return self.value[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        self.current += 1
        if key not in self.value:
            self.count += 1
        if key not in self.value and self.count > self.cap:
            while True:
                t, k = heapq.heappop(self.time)
                if k not in self.value or self.real[k] != t:
                    continue
                else:
                    del self.real[k]
                    del self.value[k]
                    break
        self.value[key] = value
        self.real[key] = self.current
        heapq.heappush(self.time, (self.current, key))
