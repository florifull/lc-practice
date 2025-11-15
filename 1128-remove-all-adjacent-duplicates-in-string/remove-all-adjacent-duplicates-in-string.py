class Solution:
    def removeDuplicates(self, s: str) -> str:
        # s = "azxxzy" -> [a, y]
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
                continue
            stack.append(s[i])
        return ''.join(stack)
    # T: O(n), S: O(n)