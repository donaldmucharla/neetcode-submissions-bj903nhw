class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        res = 0
        visited = set()
        minHeap = [(0, 0)]
        while len(visited) < N:
            dist, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            res += dist
            for neigdist, neig in adj[i]:
                if not neig in visited:
                    heapq.heappush(minHeap, (neigdist, neig))
        return res
        