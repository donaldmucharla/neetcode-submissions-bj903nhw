class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count  = collections.Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = collections.deque()

        while q or maxHeap:
            time += 1
            if maxHeap:
                cnt = 1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] <= time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

        