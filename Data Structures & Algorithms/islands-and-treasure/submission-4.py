class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==0:
                    q.append([row,col])
                    visit.add((row,col))

        def checkCell(r, c):
            if (r not in range(rows) or c not in range(cols)
            or grid[r][c]==-1 or (r,c) in visit):
                return
            visit.add((r,c))
            q.append([r,c])
            
        directions = [[0, 1],[0, -1],[1, 0],[-1, 0]]
        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=distance
                for dr, dc in directions:
                    checkCell(r+dr, c+dc)
            distance+=1



