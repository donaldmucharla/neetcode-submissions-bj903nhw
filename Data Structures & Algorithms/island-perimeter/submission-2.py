class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        perimeter = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    perimeter += 4
                
                    if r < ROW-1 and grid[r+1][c] == 1:
                        perimeter -= 1
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 1
                    if c < COL-1 and grid[r][c+1]:
                        perimeter -= 1
                    if c > 0 and grid[r][c-1]:
                        perimeter -= 1
        
        return perimeter
