class Solution:
    def maxDepth(self, s: str) -> int:
        openers = 0
        maxDepth = 0
        for c in s:
            if c == '(':
                openers += 1
                maxDepth = max(maxDepth, openers)
            elif c == ')': openers -= 1
        return maxDepth
    # T: O(n), S: O(1)