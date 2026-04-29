class MedianFinder:

    def __init__(self):
        # smaller half
        self.maxHeap = []
        # larger half
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, num * -1)

        if self.maxHeap and self.minHeap and self.maxHeap[0] * -1 > self.minHeap[0]:
            val = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, val)

        if len(self.maxHeap) - len(self.minHeap) >= 2:
            val = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, val)

        if len(self.minHeap) - len(self.maxHeap) >= 2:
            val = heapq.heappop(self.minHeap) * -1
            heapq.heappush(self.maxHeap, val)

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2

        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        