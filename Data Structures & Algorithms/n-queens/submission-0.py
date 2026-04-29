class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pDiag = set() #r+c
        nDiag = set() #r-c
        res = []
        board = [["."]*n for i in range(n)]
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r+c) in pDiag or (r-c) in nDiag:
                    continue
                col.add(c)
                pDiag.add(r+c)
                nDiag.add(r-c)
                board[r][c] = "Q"
                dfs(r+1)
                col.remove(c)
                pDiag.remove(r+c)
                nDiag.remove(r-c)
                board[r][c] = "."
        dfs(0)
        return res

