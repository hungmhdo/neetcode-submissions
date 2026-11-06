import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums,target)
        if index > -1 and index < len(nums) and nums[index] == target:
            return index
        
        return -1