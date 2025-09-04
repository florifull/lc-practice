# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node: return 0

            maxLeftHeight = dfs(node.left)
            maxRightHeight = dfs(node.right)
            localDiameter = maxLeftHeight + maxRightHeight
            if localDiameter > self.diameter: self.diameter = localDiameter
            return 1 + max(maxLeftHeight, maxRightHeight)
        dfs(root)
        return self.diameter