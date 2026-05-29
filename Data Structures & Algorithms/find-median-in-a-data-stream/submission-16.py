class MedianFinder:

    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -num)
        if self.leftHeap and self.rightHeap and -self.leftHeap[0] > self.rightHeap[0]:
            val = -heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, val)
        if len(self.leftHeap) > len(self.rightHeap)+1:
            val = -heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, val)
        if len(self.rightHeap) > len(self.leftHeap)+1:
            val = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, -val)
        
    def findMedian(self) -> float:
        if len(self.leftHeap) > len(self.rightHeap):
            return float(-self.leftHeap[0])
        elif len(self.rightHeap) > len(self.leftHeap):
            return float(self.rightHeap[0])
        else:
            return (-self.leftHeap[0]+self.rightHeap[0])/2
    
        
        
        