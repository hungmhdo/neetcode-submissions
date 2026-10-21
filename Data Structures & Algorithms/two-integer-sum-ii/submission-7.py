import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)-1):
        #     index = bisect.bisect_right(numbers, target - numbers[i])
        #     if index <= len(numbers) and numbers[i] + numbers[index-1] == target:
        #         return [i+1, index]
        i = 0 
        j = len(numbers) - 1
        while  i >= 0 and j < len(numbers) and i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return[i + 1, j + 1]
            elif total < target:
                i += 1
            else: 
                j -= 1
        
        return[]