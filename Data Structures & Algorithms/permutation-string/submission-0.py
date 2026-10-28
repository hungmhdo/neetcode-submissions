class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = dict(Counter(s1))

        d2 = dict(Counter(s2[:len(s1)]))

        if d1 == d2:
            return True
        
        for i in range(len(s1), len(s2), 1):
            if s2[i] not in d2:
                d2[s2[i]] = 1
            else:
                d2[s2[i]] += 1
            d2[s2[i - len(s1)]] -= 1
            if d2[s2[i - len(s1)]] == 0:
                del d2[s2[i - len(s1)]]
            if d1 == d2:
                return True
        
        return False