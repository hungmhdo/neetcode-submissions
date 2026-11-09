class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            # print(nums[l], nums[r], nums[m])

            if nums[m] == target:
                return m

            # l -> mid increasing:
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    # if target < nums[mmid] and target >= nums[l]:
                    r = m - 1
            # 5 6 1 2 3 4 - mid could be middle of and increasing sequence
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1