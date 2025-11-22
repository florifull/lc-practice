class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxD = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                if stack:
                    stack.pop()
            maxD = max(maxD, len(stack))
        return maxD