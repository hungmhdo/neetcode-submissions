class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        heapq.heapify(self.heap)
        self.curr = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curr += 1
        heapq.heappush(self.heap, (val, self.curr))

    def pop(self) -> None:
        self.stack.pop()
        self.curr -= 1
        while self.heap and self.heap[0][1] > self.curr:
            heapq.heappop(self.heap)
        

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        # while self.heap[0][1] > self.curr:
        #     heapq.heappop(self.heap)
        return self.heap[0][0]

