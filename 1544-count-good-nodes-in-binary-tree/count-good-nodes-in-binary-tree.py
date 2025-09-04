# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0
        def dfs(node, maxPathVal):
            if not node: return
            if node and node.val >= maxPathVal:
                self.counter += 1
                maxPathVal = node.val
            dfs(node.left, maxPathVal)
            dfs(node.right, maxPathVal)
        dfs(root, root.val)
        return self.counter
    
        # counter = 0
        # q = collections.deque() # hold node : maxPathVal
        # q.append((root, root.val))
        # while q:
        #     node, maxPathVal = q.popleft()
        #     if node.val >= maxPathVal: counter += 1
        #     if node.left:
        #         q.append((node.left, max(maxPathVal, node.val)))
        #     if node.right:
        #         q.append((node.right, max(maxPathVal, node.val)))
        # return counter
    # T: O(n), S: O(w) - where w is the max width at a level within the tree