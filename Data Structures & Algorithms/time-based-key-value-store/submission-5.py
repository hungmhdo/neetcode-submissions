import bisect
class TimeMap:

    def __init__(self):
        self.di = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        curr = self.di.get(key, [])
        bisect.insort(curr, (timestamp, value))
        self.di[key] = curr

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.di:
            return ""
        tmp = bisect.bisect_left(self.di[key], (timestamp, ''))
        # print(tmp, self.di[key])

        if tmp == len(self.di[key]) or self.di[key][tmp][0] > timestamp:
            tmp = tmp - 1
        
        
        if tmp < 0:
            return ""
        
        return self.di[key][tmp][1]
