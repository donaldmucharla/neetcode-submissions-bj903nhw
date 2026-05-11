class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        res = 0

        heapq.heapify(maxHeap)
        while k > 0:
            res = heapq.heappop(maxHeap)
            k -= 1
        return -res
        