class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr = []
        heapq.heapify(curr)
        ans = []
        for i in range(len(nums)):
            heapq.heappush(curr, (-1 * nums[i], i))
            if i >= k-1:
                while curr[0][1] <= i - k:
                    heapq.heappop(curr)
                
                ans.append(-1 * curr[0][0])
        
        return ans
