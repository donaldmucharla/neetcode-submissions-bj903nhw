class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fruit = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fruit += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q and fruit > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fruit -= 1
            time += 1

        return time if fruit == 0 else -1

        