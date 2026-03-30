import heapq
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Fast path: no cooldown → just run them
        if n == 0:
            return len(tasks)

        # Count each task, push counts as negatives to make a max-heap
        freq = Counter(tasks)
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)

        time = 0
        # Process until all tasks are done
        while heap:
            # hold tasks we ran this round but still have remaining count
            wait = []
            # One "round" has up to n+1 slots
            slots = n + 1

            # Fill this round with the most frequent available tasks
            while slots > 0 and heap:
                cnt = -heapq.heappop(heap)   # make it positive
                cnt -= 1                     # we used one instance of this task
                time += 1                    # we spent one cycle
                if cnt > 0:
                    wait.append(cnt)         # still remaining, push back after round
                slots -= 1

            # Push back remaining tasks (still need to be scheduled later)
            for remaining in wait:
                heapq.heappush(heap, -remaining)

            # If heap not empty but round not fully filled → idle for leftover slots
            if heap and slots > 0:
                time += slots

        return time
