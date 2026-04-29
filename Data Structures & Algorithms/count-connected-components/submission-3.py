class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def findParent(node):
            res = node

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res

        def union(n1, n2):
            p1, p2 = findParent(n1), findParent(n2)

            if p1 == p2:
                return 0

            if rank[p1] < rank[p2]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            return 1

        total = n
        for n1, n2 in edges:
            total -= union(n1, n2)
        
        return total

