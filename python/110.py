# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return True, 0

            lb, lh = dfs(node.left)
            rb, rh = dfs(node.right)

            b = abs(lh - rh) < 2 and lb and rb
            return b, 1 + max(lh, rh)

        b, h = dfs(root)
        return b                

