import bisect
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # bisect.insort(sorted_arr, 25)
        def remove_from_sorted(arr, val):
            # Find the index of the element using binary search
            index = bisect.bisect_left(arr, val)
            
            # Check if the element actually exists at that index
            if index < len(arr) and arr[index] == val:
                arr.pop(index)  # or del arr[index]
                return True
            return False  # Value not found
            
        a = sorted(nums[0:k])
        ans = [a[-1]]
        for i in range(k, len(nums)):
            remove_from_sorted(a, nums[i-k])
            bisect.insort(a, nums[i])
            ans.append(a[-1])
        return ans