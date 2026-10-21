class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        count = 1
        maxCount = 1
        i = 1
        while i < len(nums):
            while i < len(nums) and nums[i] <= nums[i-1] + 1:
                if nums[i] == nums[i-1]+1:
                    count += 1
                i += 1
            maxCount = max(count, maxCount)
            count = 1
            i += 1
        return max(count, maxCount)