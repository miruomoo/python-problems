class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        graph = { i:[] for i in range(N) }

        # create adj list
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                d = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append([d, j])
                graph[j].append([d, i])

        res = 0
        visited = set()
        minHeap = [[0, 0]] # cost, point

        while len(visited) < N:
            cost, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            res += cost
            visited.add(point)
            for ncost, n in graph[point]:
                if n not in visited:
                    heapq.heappush(minHeap, [ncost, n])

        return res