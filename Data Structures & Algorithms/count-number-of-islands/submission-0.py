class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = 0

        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols)
            or grid[r][c] == "0" or (r,c) in visit):
                return
            visit.add((r,c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visit:
                    res+=1
                    dfs(row, col)
        return res