class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l, r = l + 1, r - 1
            return True

        def dfs(i, localSol):
            if i >= len(s):
                res.append(localSol[:])
                return
            # decisions
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    localSol.append(s[i:j+1])
                    dfs(j+1, localSol)
                    localSol.pop()
        dfs(0, [])
        return res