class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for u, v, t in times:
            adj[u].append([t, v])
        
        minHeap = []
        visited = set()

        heapq.heappush(minHeap, [0, k])
        total_time = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue
            total_time = w1
            
            visited.add(n1)
            for w2, n2 in adj[n1]:
                if not n2 in visited:
                    heapq.heappush(minHeap, [w1 + w2, n2])
            
        return total_time if len(visited) == n else -1
