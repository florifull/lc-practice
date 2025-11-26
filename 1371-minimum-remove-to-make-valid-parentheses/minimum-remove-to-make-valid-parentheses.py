class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] # hold opening parentheses
        closerRemoval = set() # hold closing parentheses that we NEED to remove..

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                # there's no matching parentheses.. so mark it for REMOVAL
                if not stack:
                    closerRemoval.add(i)
                else:
                    # we do have openers to match this closer
                    stack.pop()
        res = []
        for i, c in enumerate(s):
            if i in stack or i in closerRemoval:
                continue
            res.append(c)
        return ''.join(res)