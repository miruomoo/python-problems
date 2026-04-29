class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            stone1 = heapq.heappop(stones) * -1
            stone2 = heapq.heappop(stones) * -1

            if stone1 == stone2:
                continue
            elif stone1 < stone2:
                heapq.heappush(stones, (stone2 - stone1) * -1)
            else:
                heapq.heappush(stones, (stone1 - stone2) * -1)

        return stones[0] * -1 if stones else 0