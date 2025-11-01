class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def dfs(num):
            # check for base case (loop OR ends in value 1)
            if num == 1: return True
            if num in visited: return False
            visited.add(num)
            sumSquares = 0
            for n in str(num):
                sumSquares += int(n) ** 2
            return dfs(sumSquares)
        return dfs(n)