class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROW = len(heights)
        COL = len(heights[0])

        minHeap = []
        heapq.heappush(minHeap, (0, 0, 0))
        visited = set()
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]

        while minHeap:
            effort , r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            
            if r == ROW-1 and c == COL-1:
                return effort
            
            visited.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= ROW or nc < 0 or nc >= COL or (nr, nc) in visited:
                    continue
                diff = abs(heights[r][c] - heights[nr][nc])
                newEffor = max(diff, effort)
                heapq.heappush(minHeap, (newEffor, nr, nc))
        return 0