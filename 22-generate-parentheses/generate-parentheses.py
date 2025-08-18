class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []

        def bt(openers, closers):
            # if we have open and close parantheses and maxed out..
            if openers == closers == n:
                res.append(''.join(stack))
                return
            if openers < n:
                stack.append('(')
                bt(openers + 1, closers)
                stack.pop()
            if closers < n and closers < openers:
                stack.append(')')
                bt(openers, closers + 1)
                stack.pop()
        bt(0, 0)
        return res