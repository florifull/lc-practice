class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        l, r = 0, len(needle)-1
        while r < len(haystack):
            word = haystack[l:r+1]
            if word == needle: return l
            l, r = l + 1, r + 1
        return -1