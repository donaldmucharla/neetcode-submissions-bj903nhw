class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        # Initialize a 2D table with 0s
        # Rows: coins (0 to n), Columns: amounts (0 to amount)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        # Base Case: There is 1 way to make amount 0 (by choosing no coins)
        for i in range(n + 1):
            dp[i][0] = 1
            
        for i in range(1, n + 1):
            for a in range(1, amount + 1):
                # Option 1: Don't use the current coin (take value from row above)
                dp[i][a] = dp[i-1][a]
                
                # Option 2: Use the current coin (stay in the same row)
                current_coin = coins[i-1]
                if a >= current_coin:
                    dp[i][a] += dp[i][a - current_coin]
                    
        return dp[n][amount]