class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set()
        res =  0

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            maxArea = 1

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    if (row+dr) in range(rows) and (col + dc) in range(cols) and grid[row+dr][col+dc] == 1 and (row +dr, col+dc) not in visited:
                        q.append((row+dr, col+dc))
                        visited.add((row+dr, col+dc))
                        maxArea += 1
            return maxArea



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                   maxArea =  bfs(r, c)
                res = max(res, maxArea)
        
        return res