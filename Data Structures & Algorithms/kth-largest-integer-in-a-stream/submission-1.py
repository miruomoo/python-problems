class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(nums)

    def add(self, val: int) -> int:

        heapq.heappush(self.nums, val)
        target = len(self.nums) - self.k
        heapclone = self.nums.copy()

        while target > 0:
            heapq.heappop(heapclone)
            target -= 1

        return heapq.heappop(heapclone)
        
