class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = {}
        maxCount = 0

        for e in nums:
            num[e] = 1

        num = dict(sorted(num.items()))
        for key in num:
            if key-1 in num:
                num[key] = num[key-1]+1
            if num[key] > maxCount:
                maxCount = num[key]
        
        return maxCount