class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Val, s2Val = [0] * 26, [0] * 26
        for c in s1:
            s1Val[ord(c) - ord('a')] += 1
        l = 0
        for r in range(len(s2)):
            while r - l + 1 > len(s1):
                s2Val[ord(s2[l]) - ord('a')] -= 1
                l += 1
            s2Val[ord(s2[r]) - ord('a')] += 1
            if tuple(s2Val) == tuple(s1Val): return True
        return False