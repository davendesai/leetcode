# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, sum):
            if not node:
                return False

            if node.left or node.right:
                fLeft = dfs(node.left, sum - node.val)
                fRight = dfs(node.right, sum - node.val)
                return fLeft or fRight

            if node.val == sum:
                return True

        return dfs(root, targetSum)

