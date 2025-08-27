class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we need to minimize bananas eaten
        l, r = 1, max(piles)
        minEatingSpeed = r # AKA banas eating per hour

        while l <= r:
            m = (l + r) // 2
            eatingSpeed = m
            hrs = 0
            for p in piles:
                hrs += ceil(p / eatingSpeed)
            if hrs <= h:
                minEatingSpeed = min(minEatingSpeed, eatingSpeed)
                r = m - 1
            else:
                # we need to eat bananas faster..
                l = m + 1
        return minEatingSpeed
    # T: O(plog(n)), S: O(p)