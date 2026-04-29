# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def sameTree(self, r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val!=r2.val:
                return False
            return self.sameTree(r1.left, r2.left) and self.sameTree(r1.right, r2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.sameTree(root, subRoot):
            return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right