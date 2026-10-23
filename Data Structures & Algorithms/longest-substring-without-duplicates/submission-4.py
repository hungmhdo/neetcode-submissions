class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charPos = {}
        # l = 0
        # maxLength = 0
        # for i in range(len(s)):
        #     c = s[i]
        #     if c not in charPos:
        #         charPos[c] = i
        #     else:
        #         maxLength = max(maxLength, i-l)
        #         l = charPos[c]+1
        #         charPos[c] = i

        # return max(maxLength, len(s)-l)

        maxLength = 0
        currStr = ""
        for c in s:
            pos = currStr.find(c)
            if pos == -1:
                currStr += c
            else:
                maxLength = max(maxLength, len(currStr))
                currStr = currStr[pos + 1:] + c
        
        return max(maxLength, len(currStr))

        # abba
        # l = 0
        # charPos = {a: 0, b:1}