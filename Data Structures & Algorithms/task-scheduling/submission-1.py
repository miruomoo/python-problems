class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-f for f in freq.values()]
        heapq.heapify(maxHeap)
        q = deque()
        res = 0

        while maxHeap or q:
            res += 1
            if maxHeap:
                count = heapq.heappop(maxHeap) * -1 - 1
                if count > 0:
                    q.append((-count, res + n)) 
            if q:
                time = q[0][1]
                if time == res:
                    newCount = q.popleft()[0]
                    heapq.heappush(maxHeap, newCount)
        return res

