class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        prevprev, prev = 1, 2
        ways = 0
        for i in range(3, n+1):
            ways = prev + prevprev
            prev, prevprev = ways, prev
        return ways