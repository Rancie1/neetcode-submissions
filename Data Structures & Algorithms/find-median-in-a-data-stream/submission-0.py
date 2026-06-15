class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []


        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)
        big = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap,-big)

        if len(self.max_heap) < len(self.min_heap):
            small = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -small)
        
        

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            mid1 = self.min_heap[0]
            mid2 = self.max_heap[0]
            return float((mid1+(-mid2))/2)

        else:
            median = self.max_heap[0]
            return float(-median)
        
        