class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        

        heap = []

        for i in count.keys():
            heapq.heappush(heap, (count[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for j in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        
        return res

        


        