class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in closers:
                if not stack: return False
                prev = stack.pop()
                if prev != closers[c]: return False
                continue
            stack.append(c)
        return True if not stack else False