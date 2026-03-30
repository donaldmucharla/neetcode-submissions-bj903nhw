import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # Build adjacency list
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim’s algorithm
        res = 0
        visited = set()
        minHeap = [[0, 0]]  # (cost, node)

        while len(visited) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            res += cost
            visited.add(i)

            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])

        return res
