class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = [-num for num in nums]
        heapq.heapify(self.maxHeap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, -val)
        copyHeap = self.maxHeap.copy()
        target = self.k
        
        while target > 1:
            heapq.heappop(copyHeap)
            target -= 1
        
        return -heapq.heappop(copyHeap)
        
