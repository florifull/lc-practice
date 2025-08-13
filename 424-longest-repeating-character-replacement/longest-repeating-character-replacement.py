class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        counts = {}
        l = 0
        maxF, maxL = 0, 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxF = max(maxF, counts[s[r]])
            while (r - l + 1) - maxF > k:
                counts[s[l]] -= 1
                l += 1
                maxF = max(maxF, max(counts.values()))
            maxL = max(maxL, r - l + 1)
        return maxL
    # T: O(n), S: O(n)
