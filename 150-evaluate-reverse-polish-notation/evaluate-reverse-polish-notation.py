class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        stack = []
        for s in tokens:
            if s in operators:
                R = stack.pop()
                L = stack.pop()
                if s == '+': stack.append(L + R)
                elif s == '-': stack.append(L - R)
                elif s == '*': stack.append(L * R)
                else: stack.append(int(L / R))
            else:
                stack.append(int(s))
        return stack[-1]
    # T: O(n), S: O(n)