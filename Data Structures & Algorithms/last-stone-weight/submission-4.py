class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            one = heapq.heappop(maxHeap) * -1
            two = heapq.heappop(maxHeap) * -1

            if one == two:
                continue
            else:
                heapq.heappush(maxHeap, abs(one - two) * -1)

        return maxHeap[0] * -1 if maxHeap else 0