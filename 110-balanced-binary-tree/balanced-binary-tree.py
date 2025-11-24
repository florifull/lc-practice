class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        A height-balanced binary tree is a binary tree
        in which the depth of the two subtrees of every node never differs by more than one.
        """
        self.balanced = True
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left-right) > 1: self.balanced = False
            return 1 + max(left, right)
        dfs(root)
        return self.balanced