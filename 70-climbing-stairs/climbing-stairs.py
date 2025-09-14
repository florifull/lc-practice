class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2: return 2
        if n == 1: return 1
        if n == 0: return 0

        memo = [0] * (n+1)
        def dfs(i):
            if i == 0: return 0
            if i == 1: return 1
            if i == 2: return 2
            if memo[i]: return memo[i]
            memo[i] = dfs(i-1) + dfs(i-2)
            return memo[i]
        dfs(n)
        return memo[-1]