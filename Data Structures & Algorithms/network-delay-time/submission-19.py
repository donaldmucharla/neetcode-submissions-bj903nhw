class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))
        
        minHeap = []
        heapq.heappush(minHeap, (0, k))
        visited = set()
        t = 0

        while minHeap:
            time, dest = heapq.heappop(minHeap)
            if dest in visited:
                continue
            visited.add(dest)
            t = time
            for time1, nei in adj[dest]:
                if not nei in visited:
                    heapq.heappush(minHeap, (time+time1, nei))
        
        return t if len(visited) == n else -1
