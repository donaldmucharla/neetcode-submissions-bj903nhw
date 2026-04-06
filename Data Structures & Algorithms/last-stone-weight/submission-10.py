class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap)>1:
            second = heapq.heappop(maxHeap)
            first = heapq.heappop(maxHeap)
            if first > second:
                heapq.heappush(maxHeap, second-first)
        if len(maxHeap)>=1:
            return -maxHeap[0]
        return 0
        


        