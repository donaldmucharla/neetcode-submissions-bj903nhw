class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        if not grid:
            return 0

        fruits = 0
        q = collections.deque()
        time = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fruits += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q and fruits > 0:
            qLen = len(q)
            
            for i in range(qLen):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if nr >= 0 and nr < ROW and nc >= 0 and nc < COL and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fruits -= 1
            time += 1
        return time if fruits == 0 else -1

