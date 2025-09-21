class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]
        minRadius = float('-inf')
        # houses = [1, 2, 3, 4]
        # heaters = [1, 2, 3]
        r = 1
        for _, house in enumerate(houses):
            while house > heaters[r]:
                r += 1
            minRadius = max(minRadius, min(heaters[r] - house, house - heaters[r-1]))
        return minRadius