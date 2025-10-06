class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [0] * (amount+1)
        # ex: [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3] -> 
        for i in range(1, amount+1):
            # traverse coins backwards
            coinAmount = float('inf')
            for j in range(len(coins)-1, -1, -1):
                if i >= coins[j]:
                    leftover = i - coins[j]
                    coinAmount = min(coinAmount, 1 + dp[leftover])
            dp[i] = coinAmount
        return dp[amount] if dp[amount] < (2**31) else -1