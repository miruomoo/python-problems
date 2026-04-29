# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            rightNode = None
            for i in range(len(q)):
                rightNode = q.popleft()
                if rightNode.left:
                    q.append(rightNode.left)
                if rightNode.right:
                    q.append(rightNode.right)
            res.append(rightNode.val)
        return res