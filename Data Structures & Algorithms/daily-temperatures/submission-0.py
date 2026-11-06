class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        heap = []
        heapq.heapify(heap)

        for i in range(len(temperatures)):
            if not heap:
                heapq.heappush(heap, (temperatures[i], i))
            else:
                while heap and temperatures[i] > heap[0][0]:
                    ans[heap[0][1]] = i - heap[0][1]
                    heapq.heappop(heap)
                heapq.heappush(heap, (temperatures[i], i))
        return ans