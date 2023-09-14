"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0

        q = deque()
        q.append((root, ""))

        while q:
            node, binary_str = q.popleft()
            if not node.left and not node.right:
                val = 0
                for c in (binary_str + str(node.val)):
                    val = (val << 1) | int(c)
                ans += val

            if node.left:
                q.append((node.left, binary_str + str(node.val)))
            if node.right:
                q.append((node.right, binary_str + str(node.val)))
                
        return ans
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, val):
            if not node:
                return 0

            val = (val << 1) + node.val
            if not node.left and not node.right:
                return val

            # we want the sum of all possible leaf node values
            return dfs(node.left, val) + dfs(node.right, val)
    
        return dfs(root, 0)
