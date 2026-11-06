class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win = []
        maxs = []
        heapq.heapify(win)
        for i in range(len(nums)):
            heapq.heappush(win, (-1 * nums[i], i))
            # print("add", nums[i])
            if i >= k-1:
                # print("over", k-1)
                while win[0][1] <= i - k:
                    v = heapq.heappop(win)
                    # print("trash", v)
                # print("in win",win[0][0] * -1)
                maxs.append(win[0][0] * -1)
        return maxs