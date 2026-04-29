class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if ((r,c) in visit or r not in range(rows)
            or c not in range(cols) or grid[r][c]=="0"):
                return
            visit.add((r,c))
            directions = [[0,1],[0,-1],[-1,0],[1,0]]
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1" and (row,col) not in visit:
                    res+=1
                    dfs(row,col)
        return res