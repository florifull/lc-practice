class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        l = maxL = 0
        for r in range(1, len(s)):
            while s[r] in s[l:r] and l < r:
                l += 1
            currL = r - l + 1
            maxL = max(maxL, currL)
        return maxL