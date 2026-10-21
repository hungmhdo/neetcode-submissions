import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            index = bisect.bisect_right(numbers, target - numbers[i])
            # print(numbers[i], numbers[index-1], index)
            if index <= len(numbers) and numbers[i] + numbers[index-1] == target:
                return [i+1, index]
        
        return[]