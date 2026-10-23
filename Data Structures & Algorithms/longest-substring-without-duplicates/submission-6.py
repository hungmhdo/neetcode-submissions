class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charPos = {}
        # l = 0
        # maxLength = 0
        # for i in range(len(s)):
        #     c = s[i]
        #     if c not in charPos or charPos[c] < l:
        #         charPos[c] = i
        #     else:
        #         maxLength = max(maxLength, i-l)
        #         l = charPos[c]+1
        #         charPos[c] = i

        # return max(maxLength, len(s)-l)

        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

        # maxLength = 0
        # currStr = ""
        # for c in s:
        #     pos = currStr.find(c)
        #     if pos == -1:
        #         currStr += c
        #     else:
        #         maxLength = max(maxLength, len(currStr))
        #         currStr = currStr[pos + 1:] + c
        
        # return max(maxLength, len(currStr))

        # abba
        # l = 0
        # charPos = {a: 0, b:1}