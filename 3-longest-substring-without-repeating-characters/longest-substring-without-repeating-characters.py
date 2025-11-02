class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        longest = 1
        window = set({s[0]})
        l = 0
        for r in range(1, len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
    # T: O(n), S: O(1)