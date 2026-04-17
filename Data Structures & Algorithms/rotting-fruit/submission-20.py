class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        ROW, COL = len(grid), len(grid[0])
        fruits = 0
        time = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fruits += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q and fruits >0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if nr not in range(ROW) or nc not in range(COL) or grid[nr][nc] !=1:
                        continue
                    grid[nr][nc] = 2
                    fruits -= 1
                    q.append((nr, nc))
                
            time += 1
        return time if fruits== 0 else -1



        