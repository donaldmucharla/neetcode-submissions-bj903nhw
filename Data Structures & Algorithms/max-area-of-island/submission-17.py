class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r,c))
            maxArea = 1
            directions = [(1,0), (0,1), (-1,0), (0,-1)]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr >= 0 and nc >=0 and nr < ROW and nc < COL and (nr, nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        maxArea += 1
            return maxArea
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, bfs(r, c))
        
        return res
 


        
