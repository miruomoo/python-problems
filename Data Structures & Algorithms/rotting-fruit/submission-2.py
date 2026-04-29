class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh=[0]
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    fresh[0]+=1
                if grid[row][col]==2:
                    q.append([row, col])
        
        def checkOrange(r, c):
            if (r not in range(rows) or c not in range(cols)
            or grid[r][c]!=1):
                return
            grid[r][c] = 2
            q.append([r,c])
            fresh[0]-=1
        
        directions = [[0, 1],[0, -1],[1, 0],[-1, 0]]
        while q and fresh[0]>0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    checkOrange(r+dr, c+dc)
            time+=1
        return time if fresh[0]==0 else -1
        
