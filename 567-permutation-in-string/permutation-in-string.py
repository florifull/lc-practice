class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        uniCode = [0] * 26
        for c in s1:
            uniCode[ord(c) - ord('a')] += 1
        tupleUnicode = tuple(uniCode)
        
        l = 0
        uniCode = [0] * 26
        for r in range(len(s2)):
            while r - l + 1 > len(s1):
                uniCode[ord(s2[l]) - ord('a')] -= 1
                l += 1
            uniCode[ord(s2[r]) - ord('a')] += 1
            if tuple(uniCode) == tupleUnicode:
                return True
        return False

