class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        return all(x == 0 for x in count)
        # hashS, hashT = {}, {}
        # for i in range(len(s)):
        #     hashS[s[i]] = hashS.get(s[i], 0) + 1
        #     hashT[t[i]] = hashT.get(t[i], 0) + 1
        # return hashS == hashT