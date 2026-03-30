class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        minHeap = [ -cnt for cnt in count.values()]
        heapq.heapify(minHeap)

        time = 0
        q = deque()

        while q or minHeap:

            time += 1
            if minHeap:
                cnt = 1+ heapq.heappop(minHeap)
                if cnt:
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(minHeap, q.popleft()[0])

        return time

        