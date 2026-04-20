class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, t in times:
            edges[u].append((t, v))

        visited = set()
        minHeap = [(0, k)]
        t = 0

        while minHeap:
            time1, destination = heapq.heappop(minHeap)
            if destination in visited:
                continue
            visited.add(destination)
            t = time1
            for time2, neighbor in edges[destination]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (time1+time2, neighbor))
        return t if n == len(visited) else -1
                

        