# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # left = 2n, right = 2n+1 - width is right-left + 1 | ex:2: 14 - 8
        # ex1: 7(right) - 4(left) + 1 = 4 (total width)
        ans = 1
        q = collections.deque()
        q.append((root,1))

        while q:
            ans = max(ans, q[-1][1] - q[0][1] + 1)
            # check level
            for _ in range(len(q)):
                node, level = q.popleft()
                if node.left: q.append((node.left, 2 * level))
                if node.right: q.append((node.right, 2 * level + 1))
        return ans
    # T: O(n), S: O(n)