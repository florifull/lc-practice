# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal (L, C, R)
        self.inorder = []
        def dfs(node):
            if not node: return
            left = dfs(node.left)
            self.inorder.append(node.val)
            right = dfs(node.right)
            return
        dfs(root)
        return self.inorder[k-1]
    # O()