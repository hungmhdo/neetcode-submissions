class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        i = 0
        while i <= n-3:
            target = 0 - nums[i]
            j = i+1
            k = n-1
            while j <= n-2 and k > i+1 and j < k:
                total = nums[j] + nums[k]
                if total == target:
                    # print(i,j,k)
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and j <= n-2 and nums[j+1] == nums[j]:
                        j += 1
                    while k > j and k > i+2 and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
                elif total > target:
                    k -= 1
                else:
                    j += 1
            while i < n-1 and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return ans