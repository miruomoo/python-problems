class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        visit.add((0, 0))
        minHeap = [[grid[0][0], 0, 0]] #(max-height, r, c)

        while minHeap:
            h, r, c = heapq.heappop(minHeap)

            if r == N - 1 and c == N - 1:
                return h

            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nc < 0 or nr < 0 or nc == N or nr == N or (nr, nc) in visit):
                    continue
                visit.add((nr, nc))
                heapq.heappush(minHeap, [max(h, grid[nr][nc]), nr, nc])

#T: O(N * M)
#S: O(N * M)