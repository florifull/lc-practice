class Solution:
    def divisorGame(self, n: int) -> bool:
        if n < 2: return False
        if n % 2 != 0: return False
        return True