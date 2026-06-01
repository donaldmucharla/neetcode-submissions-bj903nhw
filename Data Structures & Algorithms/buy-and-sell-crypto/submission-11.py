class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0

        for price in prices:
            if price < lowest:
                lowest = min(lowest, price)
            else:
                profit = price - lowest
                max_profit = max(profit, max_profit)
        
        return max_profit
