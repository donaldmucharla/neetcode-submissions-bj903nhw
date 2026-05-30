class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()

        max_length = 0

        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] != 1 or (r, c) in visited:
                return 0
            visited.add((r, c))
            area = 1
            area += dfs(r+1, c)
            area += dfs(r, c+1)
            area += dfs(r-1, c)
            area += dfs(r, c-1)

            return area
        

        for r in range(ROW):
            for c in range(COL):
                if (r, c) not in visited and grid[r][c] == 1:
                    count = dfs(r, c)
                    max_length = max( max_length, count)
        
        return max_length