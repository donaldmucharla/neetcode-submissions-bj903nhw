class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW  = len(grid)
        COL = len(grid[0])
        max_len = 0

        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            res = 1

            res += dfs(r+1, c)
            res += dfs(r-1, c)
            res += dfs(r, c+1)
            res += dfs(r, c-1)

            return res

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    max_len = max(max_len, dfs(r, c))
        
        return max_len