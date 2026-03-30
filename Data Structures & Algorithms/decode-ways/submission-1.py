class Solution:
    def numDecodings(self, s: str) -> int:
        # Array to store the number of ways to decode up to each index
        dp = { len(s) : 1 }

        def dfs(i):
            # If already calculated or at the end of the string
            if i in dp:
                return dp[i]
            # Leading zero cannot be decoded
            if s[i] == "0":
                return 0

            # Single digit decoding
            res = dfs(i + 1)
            
            # Double digit decoding (must be between 10 and 26)
            if (i + 1 < len(s) and (s[i] == "1" or 
                (s[i] == "2" and s[i + 1] in "0123456"))):
                res += dfs(i + 2)
            
            dp[i] = res
            return res

        return dfs(0)