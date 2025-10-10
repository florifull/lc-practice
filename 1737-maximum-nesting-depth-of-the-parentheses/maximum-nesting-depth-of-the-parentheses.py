class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxDepth = 0
        for c in s:
            if c == '(':
                stack.append('(')
                maxDepth = max(maxDepth, len(stack))
            elif c == ')':
                if stack: stack.pop()
        return maxDepth