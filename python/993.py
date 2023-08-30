# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        res = [] # val, parent, depth

        q = deque()
        q.append([root, None, 0])

        while q:
            if len(res) == 2: break

            n, p, d = q.popleft()

            if ((n.val == x) or (n.val == y)):
                res.append((n.val, p, d))

            if n.left:
                q.append((n.left, n, 1+d))
            if n.right:
                q.append((n.right, n, 1+d))

        f1, f2 = res
        if f1[2] == f2[2]:
            if f1[1] == f2[1]:
                return False
            return True




            


                


