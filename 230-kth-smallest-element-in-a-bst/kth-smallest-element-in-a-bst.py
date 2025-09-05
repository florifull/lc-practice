# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative
        node = root
        s = []
        curr = 0
        while s or node: # just for first run time
            while node:
                s.append(node)
                node = node.left
            # leftmost of said node..
            node = s.pop()
            curr += 1
            if curr == k: return node.val
            # check right side
            node = node.right

        # inorder traversal (L, C, R)
        # self.inorder = []
        # def dfs(node):
        #     if not node: return
        #     left = dfs(node.left)
        #     self.inorder.append(node.val)
        #     right = dfs(node.right)
        #     return
        # dfs(root)
        # return self.inorder[k-1]
    # T: O(n), S: O(n)