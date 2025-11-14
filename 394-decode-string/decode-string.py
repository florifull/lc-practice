class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                # grab string val:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()
                intVal = ''
                while stack and stack[-1].isdigit():
                    intVal = stack.pop() + intVal
                stack.append(int(intVal) * substr)
        return ''.join(stack)
    '''
    Example 1:
    Input: s = "3[a]2[bc]" -> 3 a-> [aaa]
    Output: "aaabcbc"

    Example 2:
    Input: s = "3[a2[c]]" -> 3a2c -> -> 3acc-> 3 * [acc] => [accaccacc]
    Output: "accaccacc"
    '''