class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newS = []
        for i in range(len(s)):
            if s[i].isalnum(): newS.append(s[i])
        s = ''.join(newS)
        return s == s[::-1]