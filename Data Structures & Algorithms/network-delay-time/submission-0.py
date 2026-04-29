class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for time in times:
            start, end, cost = time
            graph[start].append([cost, end])

        minHeap = [[0, k]]
        total = 0
        visited = set()

        while minHeap:
            node = heapq.heappop(minHeap)
            cost, end = node
            if end in visited:
                continue
            visited.add(end)
            total = cost

            for neighbor in graph[end]:
                newCost, newEnd = neighbor
                if newEnd not in visited:
                    heapq.heappush(minHeap, [newCost + cost, newEnd])

        return total if len(visited) == n else -1

        