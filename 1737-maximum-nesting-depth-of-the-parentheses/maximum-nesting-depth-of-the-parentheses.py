class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        maxD = 0
        for i in range(len(s)):
            if s[i] == '(':
                current_depth += 1
            elif s[i] == ')':
                current_depth -= 1
            maxD = max(maxD, current_depth)
        return maxD
    # T: O(n), S: O(1)