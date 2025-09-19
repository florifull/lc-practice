# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # base cases
        if root1 and not root2: return False
        if root2 and not root1: return False
        if not root1 and not root2: return True
        if root1.val != root2.val: return False

        left = self.flipEquiv(root1.left, root2.left)
        leftFlip = self.flipEquiv(root1.left, root2.right)
        right = self.flipEquiv(root1.right, root2.right)
        rightFlip = self.flipEquiv(root1.right, root2.left)
        return (left and right) or (leftFlip and rightFlip)