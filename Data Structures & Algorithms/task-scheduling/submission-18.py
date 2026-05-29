class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        MaxHeap = [-c for c in count.values()]
        heapq.heapify(MaxHeap)
        q = collections.deque()
        time = 0

        while q or MaxHeap:
            time += 1
            if MaxHeap:
                cnt = 1+heapq.heappop(MaxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                cnt, time = q.popleft()
                heapq.heappush(MaxHeap, cnt)
        
        return time

            

        