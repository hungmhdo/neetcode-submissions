class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - currMin)
            currMin = min(currMin, prices[i])
        return profit