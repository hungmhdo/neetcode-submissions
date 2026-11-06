class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = [0] * len(temperatures)
        # heap = []
        # heapq.heapify(heap)

        # for i in range(len(temperatures)):
        #     if not heap:
        #         heapq.heappush(heap, (temperatures[i], i))
        #     else:
        #         while heap and temperatures[i] > heap[0][0]:
        #             ans[heap[0][1]] = i - heap[0][1]
        #             heapq.heappop(heap)
        #         heapq.heappush(heap, (temperatures[i], i))
        # return ans

        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            t = temperatures[i]

            while stack and t > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return ans

