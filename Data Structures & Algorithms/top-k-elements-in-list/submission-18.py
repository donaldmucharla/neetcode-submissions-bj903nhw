class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        count = collections.Counter(nums)

        for n, f in count.items():
            heapq.heappush(maxHeap, (-f, n))
        
        res = []
        
        while k > 0:
            f, n = heapq.heappop(maxHeap)
            res.append(n)
            k -= 1
        return res