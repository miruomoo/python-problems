"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashMap = {}
        def dfs(cur):
            if cur in hashMap:
                return hashMap[cur]
            hashMap[cur] = Node(cur.val)
            for n in cur.neighbors:
                hashMap[cur].neighbors.append(dfs(n))
            return hashMap[cur]
        return dfs(node)
            