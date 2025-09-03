class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        maxRadius = float('-inf')

        for house in houses:
            l, r = 0, len(heaters) - 1
            minRadius = float('inf')
            # binary search
            while l <= r:
                m = (l + r )// 2
                heaterVal = heaters[m]
                distance = abs(house - heaterVal)
                if distance < minRadius: minRadius = distance

                if heaterVal > house: r = m - 1
                elif heaterVal < house: l = m + 1
                else: break # found heater at exact position..
            if minRadius > maxRadius: maxRadius = minRadius
        return maxRadius