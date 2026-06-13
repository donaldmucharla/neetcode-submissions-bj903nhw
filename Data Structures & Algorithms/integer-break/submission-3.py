class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1

        for num in range(2, n+1):
            for split in range(1, num):
                dp[num] = max(dp[num], split * (num-split), split * dp[num-split])
        
        return dp[n]
        