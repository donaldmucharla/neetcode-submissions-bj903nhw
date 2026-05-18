class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [[grid[0][0], 0, 0]]
        visited = set()
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        ROW, COL = len(grid), len(grid[0])

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == ROW-1 and c == COL-1:
                return t
            for dr, dc in directions:
                neiRow, neiCol = dr+r, dc+c
                if neiRow < 0 or neiCol < 0 or neiRow == ROW or neiCol == COL or (neiRow, neiCol) in visited:
                    continue
                visited.add((neiRow, neiCol))
                heapq.heappush(minHeap, [max(grid[neiRow][neiCol], t), neiRow, neiCol])
