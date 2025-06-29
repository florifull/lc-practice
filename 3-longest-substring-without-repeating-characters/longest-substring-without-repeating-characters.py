class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        l = maxL = 0
        window = set(s[l])
        for r in range(1, len(s)):
            while s[r] in window and l < r:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            maxL = max(maxL, len(window))
        return maxL
# T: O(n), S: O(min(n, m))