class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        visited =set()
        time = 0
        fruits = 0
        q = collections.deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fruits += 1
        
        while q and fruits > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= ROW or nc < 0 or nc >= COL or (nr, nc) in visited or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] =  2
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    fruits -= 1
            time += 1
        
        return time if fruits == 0 else -1
            

        