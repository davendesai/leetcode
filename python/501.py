# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nodes = {}

        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            nodes[node.val] = nodes.get(node.val, 0) + 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        freq = max(nodes.values())
        return [k for k, v in nodes.items() if v == freq]

