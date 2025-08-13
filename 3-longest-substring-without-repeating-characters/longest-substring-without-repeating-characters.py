class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        l = 0
        visited = set(s[l])
        longestS = 1
        for r in range(1, len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            longestS = max(longestS, len(visited))
        return longestS
    # T: O(n), S: O(n)