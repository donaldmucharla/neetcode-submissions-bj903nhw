class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        dp = [[0] * COL for _ in range(ROW)]

        dp[0][0] = grid[0][0]

        for r in range(ROW):
            for c in range(COL):
                if r == 0 and c == 0:
                    continue
                
                top = dp[r-1][c] if r > 0 else float("inf")
                left = dp[r][c-1] if c > 0 else float("inf")

                dp[r][c] = grid[r][c]+ min(left, top)
        
        return dp[ROW-1][COL-1]
                
