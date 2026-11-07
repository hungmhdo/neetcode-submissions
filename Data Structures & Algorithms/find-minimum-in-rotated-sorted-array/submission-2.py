class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        num = nums[0]

        while l <= r:
            m = (l + r) // 2

            if nums[m] >= nums[l]:
                num = min(num, nums[l])
                l = m + 1
            else:
                num = min(num, nums[m])
                r = m - 1

        return num