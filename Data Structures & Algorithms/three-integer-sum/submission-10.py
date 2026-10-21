class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            if sorted_nums[i] > 0:
                break

            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                current_sum = sorted_nums[left] + sorted_nums[right] + sorted_nums[i]

                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1

                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1

                    while right > left and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1

        return result
