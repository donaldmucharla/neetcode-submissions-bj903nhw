class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N  = len(grid)
        visited= set()
        minHeap = [[grid[0][0], 0, 0]]
        visited.add((0, 0))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N-1 and c == N-1:
                return t
            for dr, dc in directions:
                neigR, neigC = r+dr, c+dc
                if neigR < 0 or neigR >= N or neigC < 0 or neigC >= N or (neigR, neigC) in visited:
                    continue
                visited.add((neigR, neigC))
                heapq.heappush(minHeap, [max(t, grid[neigR][neigC]), neigR, neigC])
        return t

            
        