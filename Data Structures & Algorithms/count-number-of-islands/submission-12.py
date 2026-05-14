class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        islands = 0
        

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc+col
                    if nr >= 0 and nc >= 0 and nr < ROW and nc < COL and (nr, nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        visited.add((nr, nc))
            
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands
                        