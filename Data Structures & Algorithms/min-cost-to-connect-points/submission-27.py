class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1, p2 = points[i]
                t1, t2 = points[j]
                dist = abs(p1-t1)+abs(p2-t2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        res = 0
        visited = set()
        minHeap = []
        heapq.heappush(minHeap, (0, 0))

        while len(visited) < len(points):
            dist, v = heapq.heappop(minHeap)
            if v in visited:
                continue
            visited.add(v)
            res += dist
            for dist2, nei in adj[v]:
                if not nei in visited:
                    heapq.heappush(minHeap, (dist2, nei))
        
        return res
        

