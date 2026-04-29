class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for point in points:
            x, y = point
            heap.append((x ** 2 + y ** 2, x, y))

        heapq.heapify(heap)

        res = []

        while k > 0:
            d, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1

        return res


