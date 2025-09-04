# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # write on notebook...
        def isSameTree(p, q):
            if not p and not q: return True
            if not p or not q or p.val != q.val: return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        # traverse all root nodes, checking whether it is same tree as subroot..
        def dfs(node):
            if not node: return False
            res = isSameTree(node, subRoot)
            if res: return True
            left, right = dfs(node.left), dfs(node.right)
            return left or right
        
        return dfs(root)
            