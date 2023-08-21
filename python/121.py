class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = [-1] * len(prices)
        for i in range(len(prices)-1, -1, -1):
            if i == len(prices) - 1:
                continue
            highest[i] = max(prices[i+1], highest[i+1])

        maxprofit = 0
        for i, p in enumerate(prices):
            profit = highest[i] - p
            maxprofit = max(maxprofit, profit)
        return maxprofit

        
