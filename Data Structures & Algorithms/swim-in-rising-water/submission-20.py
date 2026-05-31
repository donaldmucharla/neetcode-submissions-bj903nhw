class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == ROW-1 and c == COL-1:
                return t
            
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nr >= ROW or nc < 0 or nc >= COL or (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))
                next_height = max(grid[nr][nc], t)
                heapq.heappush(minHeap, (next_height, nr, nc))
            
        return 0