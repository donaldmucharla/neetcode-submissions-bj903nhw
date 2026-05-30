class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = set()

        count = 0
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visited or grid[r][c] != "1":
                return 
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c) 
            dfs(r, c+1) 
            dfs(r, c-1) 

        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        
        return count
                

