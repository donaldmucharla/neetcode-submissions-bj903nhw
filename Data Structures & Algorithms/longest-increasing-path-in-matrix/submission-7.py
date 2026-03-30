class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        ROW, COL = len(matrix), len(matrix[0])
        dp = {}
        def dfs(r, c, prevVal):
            if (r < 0 or r == ROW or c < 0 or c == COL or matrix[r][c] <= prevVal):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1

            res = max(res, 1+dfs(r+1, c, matrix[r][c]))
            res = max(res, 1+dfs(r, c+1, matrix[r][c]))
            res = max(res, 1+dfs(r-1, c, matrix[r][c]))
            res = max(res, 1+dfs(r, c-1, matrix[r][c]))

            dp[(r, c)] = res

            return res

        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, -1)

        return max(dp.values())
        