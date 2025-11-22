class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        # [a,3]
        for c in s:
            if stack:
                topC, topCount = stack[-1]
                if topCount == k: stack.pop()
                if stack and stack[-1][0] == c:
                    stack[-1][1] += 1
                    continue
            stack.append([c, 1])
        # last char check
        if stack[-1][1] >= k: stack.pop()
        return ''.join(v * c for c, v in stack) # 