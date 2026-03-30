class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        time = 0
        freq = collections.Counter(tasks)
        heap = [-t for t in freq.values()]
        heapq.heapify(heap)

        while heap:

            wait = []
            slots = n+1

            while heap and slots:
                cnt = -heapq.heappop(heap)
                cnt -= 1
                time += 1
                if cnt:
                    wait.append(cnt)
                slots -= 1

            if wait:
                for w in wait:
                    heapq.heappush(heap, -w)

            if heap and slots > 0:
                time += slots
        return time
            


        