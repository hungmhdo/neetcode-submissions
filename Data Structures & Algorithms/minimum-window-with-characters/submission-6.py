class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = dict(Counter(t))

        l = 0
        have = 0
        need = len(tCount)
        curr = s + s
        sCount = {}
        for r in range(len(s)):
            if s[r] in t:
                sCount[s[r]] = sCount.get(s[r], 0) + 1
                if sCount[s[r]] == tCount[s[r]]:
                    have += 1
            
            while have == need:
                st = s[l:r + 1]
                if len(st) < len(curr):
                    curr = st
                
                if s[l] in t:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < tCount[s[l]]:
                        have -= 1
                
                l += 1
        
        if len(curr) > len(s):
            return ""
        else:
            return curr
                    

