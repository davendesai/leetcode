# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def enumerate(bst_node, list):
            if not bst_node:
                return

            enumerate(bst_node.left, list)
            list.append(bst_node.val)
            enumerate(bst_node.right, list)

            return list

        complete = enumerate(root, [])
        ans = float('inf')
        for i in range(len(complete)-1):
            diff = abs(complete[i] - complete[i+1])
            ans = min(ans, diff)
        return ans

