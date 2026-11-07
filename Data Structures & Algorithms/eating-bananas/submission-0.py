class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min k = 1
        # max k = max(piles)

        l = 1
        r = max(piles)
        ans = 0

        while l <= r:
            print(l, r)
            m = (l + r) // 2
            total = 0

            for c in piles:
                if c < m:
                    total += 1
                else:
                    total += math.ceil(c / m)
            

            if total <= h:
                r = m - 1
                ans = m
            else:
                l = m + 1
        
        return ans