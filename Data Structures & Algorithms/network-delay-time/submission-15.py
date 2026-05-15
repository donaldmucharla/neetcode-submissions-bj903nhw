class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, t in times:
            edges[u].append((t, v))
        
        visited = set()
        t = 0
        minHeap = [(0, k)]

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            t = time
            for time2, node in edges[node]:
                if node not in visited:
                    heapq.heappush(minHeap, (time+time2, node))
        
        return t if len(visited) == n else -1