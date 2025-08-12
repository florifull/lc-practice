class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l] != s[r]: return False
                l, r = l + 1, r - 1
            elif s[l].isalnum():
                r -= 1
            elif s[r].isalnum():
                l += 1
            else:
                l, r = l + 1, r - 1
        return True
