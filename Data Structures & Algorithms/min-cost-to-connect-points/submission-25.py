class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i, len(points)):
                x, y = points[i]
                p, q = points[j]

                dist = abs(x-p) + abs(y-q)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        minHeap = []
        res = 0
        visited = set()

        heapq.heappush(minHeap, (0, 0))

        while len(visited) < len(points):
            dist, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            
            res += dist
            visited.add(point)
            for neigDist, neiP in adj[point]:
                if not neiP in visited:
                    heapq.heappush(minHeap, (neigDist, neiP))
        
        return res
            
            
        
                