class Solution:
    def calculate(self, s: str) -> int:
        res = prevDigit = currDigit = 0
        i = 0
        operator = '+'
        while i < len(s):
            # parse entire digit
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    currDigit = currDigit * 10 + int(s[i])
                    i += 1
                i -= 1
                # execute operation
                if operator == '+':
                    res += currDigit
                    prevDigit = currDigit
                elif operator == '-':
                    currDigit *= -1
                    res += currDigit
                    prevDigit = currDigit
                elif operator == '*':
                    res -= prevDigit
                    res += prevDigit * currDigit
                    # "3+2*2*2" -> prev digit needs to multiply up / dynamic..
                    prevDigit *= currDigit
                else:
                    res -= prevDigit
                    # "3+2/2/2" -> prev digit needs to multiply up / dynamic..
                    res += int(prevDigit / currDigit)
                    prevDigit = int(prevDigit / currDigit)
                currDigit = 0
            # operator detected
            elif s[i] != ' ':
                operator = s[i]
            i += 1
        return res