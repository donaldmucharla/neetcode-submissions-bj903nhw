class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROW, COL = len(grid), len(grid[0])
        maxArea = 0
        res = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            maxArea = 1

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr in range(ROW) and nc in range(COL) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        maxArea += 1
            return maxArea

    
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = bfs(r, c)
                
                res = max(maxArea, res)
        
        return res


        