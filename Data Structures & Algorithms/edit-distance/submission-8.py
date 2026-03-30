class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # dp[i][j] = min operations to convert word1[i:] to word2[j:]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: word1 empty → insert all remaining word2 chars
        for j in range(n + 1):
            dp[m][j] = n - j

        # Base case: word2 empty → delete all remaining word1 chars
        for i in range(m + 1):
            dp[i][n] = m - i

        # Fill table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],     # delete
                        dp[i][j + 1],     # insert
                        dp[i + 1][j + 1]  # replace
                    )

        return dp[0][0]
