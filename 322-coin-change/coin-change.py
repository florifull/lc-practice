class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                subtract = i - c
                if subtract < 0: subtract = i
                dp[i] = min(dp[i], 1 + dp[subtract])
        return dp[-1] if dp[-1] != float('inf') else -1
        # [1, 4, 5] -> amount = 12 -> 