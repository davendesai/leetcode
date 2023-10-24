# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            # return (sum_values, total_tilt)
            if not node:
                return 0, 0

            l_sum, l_tilt = dfs(node.left)
            r_sum, r_tilt = dfs(node.right)

            tilt = abs(l_sum - r_sum)
            return node.val + l_sum + r_sum, l_tilt + r_tilt + tilt

        _, tilt = dfs(root)
        return tilt

