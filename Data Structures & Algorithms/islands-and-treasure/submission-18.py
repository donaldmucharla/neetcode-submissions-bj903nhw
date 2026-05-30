class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        dist = 0
        visited = set()
        q = collections.deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL  or (r, c) in visited or grid[r][c] == -1:
                return
            
            visited.add((r, c))
            q.append((r, c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
            
            dist += 1


