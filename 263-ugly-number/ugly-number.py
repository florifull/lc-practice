class Solution:
    def isUgly(self, n: int) -> bool:
        ugly = set({2, 3, 5})

        def dfs(n):
            if n <= 0: return False
            if n == 1: return True
            for num in ugly:
                if n % num == 0:
                    n //= num
                    return dfs(n)
            return False
        return dfs(n)