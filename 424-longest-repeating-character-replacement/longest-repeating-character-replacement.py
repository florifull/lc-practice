class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ourChars = {}
        l = 0
        maxL = 0
        for r in range(len(s)):
            ourChars[s[r]] = ourChars.get(s[r], 0) + 1
            while (r - l + 1) - max(ourChars.values()) > k:
                ourChars[s[l]] -= 1
                l += 1
            maxL = max(maxL, r - l + 1)
        return maxL