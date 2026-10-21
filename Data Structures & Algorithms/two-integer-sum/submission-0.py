class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # for i in range(0, n-1):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # return []
        numsLookUp = dict()
        for i in range(0, n):
            remain = target - nums[i]
            if remain in numsLookUp:
                return [numsLookUp[remain], i]
            if nums[i] not in numsLookUp:
                numsLookUp[nums[i]] = i
        
        return [0, 0]
