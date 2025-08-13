class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        counts = {}
        l = 0
        maxL = 0
        counts[s[l]] = 1
        for r in range(1, len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            bf = (r - l + 1) - max(counts.values())
            while bf > k and l < r:
                counts[s[l]] -= 1
                l += 1
                bf = (r - l + 1) - max(counts.values())
            maxL = max(maxL, r - l + 1)
        return maxL
