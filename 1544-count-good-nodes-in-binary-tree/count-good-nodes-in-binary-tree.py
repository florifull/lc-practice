# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        q = collections.deque() # hold node : maxPathVal
        q.append((root, root.val))
        while q:
            node, maxPathVal = q.popleft()
            if node.val >= maxPathVal: counter += 1
            if node.left:
                q.append((node.left, max(maxPathVal, node.val)))
            if node.right:
                q.append((node.right, max(maxPathVal, node.val)))
        return counter