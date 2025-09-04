# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True
        def dfs(p, q):
            if not p and not q: return
            elif not p or not q: 
                self.isSame = False
                return
            elif p.val != q.val:
                self.isSame = False
                return
            if not p and not q: return
            dfs(p.left, q.left)
            dfs(p.right, q.right)
        dfs(p, q)
        return self.isSame