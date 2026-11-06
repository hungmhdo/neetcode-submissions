class Solution:
    def isValid(self, s: str) -> bool:
        di = {')': '(', ']': '[', '}': '{'}
        st = []
        for c in s:
            if c not in di:
                st.append(c)
            else:
                if len(st) == 0 or st[-1] != di[c]:
                    return False
                else:
                    st.pop()
        
        return len(st) == 0
                