class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * COL for r in range(ROW)]
        dp[0][0] = 1

        for r in range(ROW):
            for c in range(COL):
                if r == 0 and c == 0:
                    continue
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    top = dp[r-1][c] if r > 0 else 0
                    left = dp[r][c-1] if c > 0 else 0 

                    dp[r][c] = top + left
        
        return dp[ROW-1][COL-1]

