class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}
        def dfs(i, buying):
            if i>=len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooling = dfs(i+1, buying)

            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(cooling, buy)
            else:
                sell = dfs(i+2, not buying)+prices[i]
                dp[(i, buying)] = max(cooling, sell)
            
            return dp[(i, buying)]
        
        return dfs(0, True)
        