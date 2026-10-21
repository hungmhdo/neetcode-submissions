class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = dict(Counter(nums))
        sortedCount = dict(sorted(countNums.items(), key=lambda item: item[1], reverse = True))

        count = 0
        freqEle = []
        for key in sortedCount:
            freqEle.append(key)
            count += 1
            if count == k:
                return freqEle
        
        return freqEle
