class Solution:
    def isValid(self, s: str) -> bool:
        # LIFO - solution
        closers = {'}':'{', ')':'(', ']':'['}
        stack = []
        for p in s:
            if p not in closers:
                stack.append(p)
            elif stack:
                if closers[p] != stack.pop(): return False
            else: return False  # case where more closers than openers
        return True if not stack else False