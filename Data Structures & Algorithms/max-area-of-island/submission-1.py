class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c):
            if ((r,c) in visit or r not in range(rows)
            or c not in range(cols) or grid[r][c]==0):
                return 0
            size = 0
            visit.add((r,c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                size+=dfs(r+dr,c+dc)
            return size+1
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visit and grid[row][col]==1:
                    res = max(res, dfs(row, col))
        return res
