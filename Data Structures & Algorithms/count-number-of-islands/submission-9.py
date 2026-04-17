class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if nr in range(ROW) and nc in range(COL) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and  (r, c) not in visited:
                    bfs(r, c)
                    islands+= 1
        
        return islands



        