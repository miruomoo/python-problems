"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = { None: None }
        cur = head
        while cur:
            copy = Node(cur.val)
            hmap[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = hmap[cur]
            copy.next = hmap[cur.next]
            copy.random = hmap[cur.random]
            cur = cur.next
        return hmap[head]