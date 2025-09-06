# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # preorder = [3,9,20,15,7]
    # inorder = [9,3,15,20,7]
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return
        root = TreeNode(preorder[0])
        inOrderRootIdx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1+inOrderRootIdx], inorder[:inOrderRootIdx])
        root.right = self.buildTree(preorder[1+inOrderRootIdx:], inorder[inOrderRootIdx+1:])
        return root