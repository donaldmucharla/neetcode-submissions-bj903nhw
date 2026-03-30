class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dimensions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        island = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                r,c = q.popleft()
                for dr, dc in dimensions:
                    nr = dr+r
                    nc = dc+c
                    if nc < 0 or nr < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0":
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    island += 1
        
        return island

        