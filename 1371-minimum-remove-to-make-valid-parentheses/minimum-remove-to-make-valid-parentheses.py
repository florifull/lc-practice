class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove = set()
        stack = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if not stack:
                    to_remove.add(i)
                    continue
                stack.pop()
        # note all open parentheses that we need to remove..
        for i in stack:
            to_remove.add(i)
        
        return ''.join(c for i, c in enumerate(s) if i not in to_remove)