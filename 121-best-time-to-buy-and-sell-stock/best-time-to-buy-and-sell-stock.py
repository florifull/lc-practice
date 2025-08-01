class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
                continue
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        return maxP
    # T: O(n), S: O(1)