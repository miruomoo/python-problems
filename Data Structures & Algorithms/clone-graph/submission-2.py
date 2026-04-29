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
        hmap = {}
        def dfs(node):
            if node in hmap:
                return hmap[node]
            new = hmap[node] = Node(node.val)
            for n in node.neighbors:
                new.neighbors.append(dfs(n))
            return new
        return dfs(node)
        