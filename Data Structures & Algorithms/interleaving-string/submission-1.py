class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If total length doesn't match, it's impossible
        if len(s1) + len(s2) != len(s3):
            return False

        # Cache to store (index_s1, index_s2) -> result
        dp = {}

        def dfs(i, j):
            # Base Case: Reached the end of both strings
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            # Choice 1: Use character from s1
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            
            # Choice 2: Use character from s2
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True

            dp[(i, j)] = False
            return False

        return dfs(0, 0)