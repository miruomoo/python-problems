# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        q = deque([(root, root.val)]) #node, curMax

        while q:
            for _ in range(len(q)):
                node, curMax = q.popleft()
                if node.val >= curMax:
                    res += 1
                if node.left:
                    q.append((node.left, max(curMax, node.left.val)))
                if node.right:
                    q.append((node.right, max(curMax, node.right.val)))

        return res
                
