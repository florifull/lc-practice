class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prevprev, prev = cost[0], cost[1]
        currCost = float('inf')
        for i in range(2, len(cost)):
            currCost = min(cost[i]+prev, cost[i]+prevprev)
            prevprev, prev = prev, currCost
        return min(prevprev, prev)
    # T: O(n), S: O(n)