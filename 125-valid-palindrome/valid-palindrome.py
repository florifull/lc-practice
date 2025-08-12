class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alnum = []
        for c in s:
            if c.isalnum():
                alnum.append(c)
        return ''.join(alnum) == ''.join(alnum)[::-1]