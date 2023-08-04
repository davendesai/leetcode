# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root, check):
            if not root and not check:
                return True
            if not root or not check:
                return False

            return root.val == check.val and dfs(root.left, check.left) and dfs(root.right, check.right)

        dq = deque()
        dq.appendleft(root)
        while len(dq) > 0:
            node = dq.pop()
            if node.val == subRoot.val and dfs(node, subRoot):
                return True
            if node.left:
                dq.appendleft(node.left)
            if node.right:
                dq.appendleft(node.right)
        
        return False

