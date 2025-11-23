class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                # Explicitly skip invalid coins
                if i - c < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != float('inf') else -1
    # T: O(a * n), S: (a)