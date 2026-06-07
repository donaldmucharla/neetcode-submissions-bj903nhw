class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prevHeight):
            if r < 0 or r >= ROW or c < 0 or c >= COL or heights[r][c] < prevHeight or (r, c) in visited:
                return

            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
        

        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COL-1, atlantic, heights[r][COL-1])
        
        for c in range(COL):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROW-1,c, atlantic, heights[ROW-1][c] )
        
        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res