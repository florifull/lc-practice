# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # no upperbound on right, no lowerbound on left
        def dfs(root, minVal, maxVal):
            if not root: return True
            if root.val >= maxVal or root.val <= minVal: return False
            # update max required when we go left, update min required when go right
            left = dfs(root.left, minVal, min(root.val, maxVal))
            right = dfs(root.right, max(root.val, minVal), maxVal)
            return left and right
        return dfs(root, float('-inf'), float('inf'))