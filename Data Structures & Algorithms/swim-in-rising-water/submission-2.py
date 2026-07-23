class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        visit.add((0, 0))
        minHeap = [[grid[0][0], 0, 0]] # height, r, c

        while minHeap:
            h, r, c = heapq.heappop(minHeap)

            if r == N - 1 and c == N - 1:
                return h

            dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr == N or nc == N or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                heapq.heappush(minHeap, [max(grid[nr][nc], h), nr, nc])