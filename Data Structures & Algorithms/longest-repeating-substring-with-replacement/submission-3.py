class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # subStr = ""
        # maxLength = 0
        # for i in range(0, len(s)):
        #     charDict = {s[i]: 1}
        #     currChar = s[i]
        #     currMax = 1
        #     j = i+1
        #     while j < len(s):
        #         if s[j] not in charDict:
        #             charDict[s[j]] = 1
        #         else:
        #             charDict[s[j]] += 1
                
        #         if charDict[s[j]] > currMax:
        #             currMax = charDict[s[j]]
        #             currChar = s[j]
                
        #         totalDiff = 0
        #         for key in charDict:
        #             if key != currChar:
        #                 totalDiff += charDict[key]
        #         if totalDiff > k:
        #             maxLength = max(maxLength, j-i)
        #             break
        #         j += 1
        #     if j == len(s):
        #         return max(maxLength, j-i)
        
        # return maxLength

        # observation: at most k+1 distinct character
        # convert into 1 character -> sliding window
        # diff = set(s)
        # maxLength = 0
        # for c in diff:
        #     l = 0
        #     tmp = k
        #     for r in range(len(s)):
        #         if s[r] != c and tmp < 1:
        #             l += 1
        #             while l < r and s[l] != c:
        #                 l += 1
        #         elif s[r] != c:
        #             tmp -= 1
        #         maxLength = max(maxLength, r-l+1)
        #         # print(l, r, s[l], s[r], tmp, maxLength)

        # return maxLength

        # ABAABAAA - 1
        # ABAABBBA - 2
        # ABAABCCC - 2

        # heap
        # length substring - # most appear letter = what left

        charHeap = []
        l = 0
        maxLength = 0
        currMax = 0
        charDict = defaultdict(int)
        for r in range(len(s)):
            currLength = r-l+1
            charDict[s[r]] += 1

            if charDict[s[r]] > currMax:
                currMax = charDict[s[r]]
            
            if currLength - currMax > k:
                maxLength = max(maxLength, currLength - 1)
                charDict[s[l]] -= 1
                l += 1
        
        return max(maxLength, len(s)-l)
         
