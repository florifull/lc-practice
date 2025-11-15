class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack = [(char, count), ...]
        # "deeedbbcccbdaa" -> [(d,1), (e,2)] ex: k = 3-1=2
        stack = [[s[0], 1]]
        for i in range(1, len(s)):
            # if top of stack is equal to THIS char
            if stack and stack[-1][0] == s[i]:
                if stack[-1][1] >= k-1:
                    stack.pop()
                    continue
                # not at removal threshold
                stack[-1][1] += 1
            else:
                stack.append([s[i], 1])
        return ''.join(char * count for char, count in stack)
            