# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minV, maxV):
            if not node: return True
            if node.val <= minV or node.val >= maxV: return False
            left = dfs(node.left, minV, node.val)
            right = dfs(node.right, node.val, maxV)
            return left and right
        return dfs(root, float('-inf'), float('inf'))
    # T: O(n), S: O(n)