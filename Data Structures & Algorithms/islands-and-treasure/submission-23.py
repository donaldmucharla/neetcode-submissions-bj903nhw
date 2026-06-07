class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        q = collections.deque()
        visited = set()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def addCell(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == -1 or (r, c) in visited:
                return
            visited.add((r, c))
            q.append((r, c))
            
        
        dist = 0

        while q:
            for i in range(len(q)):
                r, c  = q.popleft()
                grid[r][c] = dist
                addCell(r+1, c)
                addCell(r, c+1)
                addCell(r-1, c)
                addCell(r, c-1)

            dist += 1




