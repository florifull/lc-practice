class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest = 0
        l = 0
        for _, c in enumerate(s):
            while c in window:
                window.remove(s[l])
                l += 1
            window.add(c)
            if len(window) > longest: longest = len(window)
        return longest
    # T: O(n), S: O(1)