class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        count = 1
        maxCount = 1
        # print(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] + 1:
                if count > maxCount:
                    maxCount = count
                count = 1
            elif nums[i] == nums[i-1] + 1:
                count += 1
        return max(count, maxCount)