class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def addroom(r, c):
            if r<0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == -1 or (r, c) in visited:
                return
            
            visited.add((r,c))
            q.append((r, c))


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))

        dist = 0
        while q:
            
            for n in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addroom(r+1, c)
                addroom(r-1, c)
                addroom(r, c+1)
                addroom(r, c-1)
            dist += 1



            




                    

        