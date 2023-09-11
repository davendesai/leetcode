# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # every node has 0 or 2 children
            if not node.left and not node.right:
                return node.val

            l, r = dfs(node.left), dfs(node.right)

            if node.val == 2:
                # or
                return l or r
            else:
                return l and r
        
        return dfs(root)

