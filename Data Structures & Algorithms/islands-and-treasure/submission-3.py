class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            if (r not in range(rows) or c not in range(cols) or
            (r,c) in visit or grid[r][c]==-1):
                return
            visit.add((r, c))
            q.append([r, c])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==0:
                    q.append([row,col])
                    visit.add((row,col))
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                directions = [[0, 1],[0, -1],[1, 0],[-1, 0]]
                for dr, dc in directions:
                    addRoom(r+dr, c+dc)
            distance+=1