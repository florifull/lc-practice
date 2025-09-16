class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses_to_radius = {} # house : radius (abs(house - heater))
        heaters.sort() # O(nlogn)

        for house in houses:
            l, r = 0, len(heaters) - 1
            while l <= r:
                m = (l + r) // 2
                heater = heaters[m]
                distance = abs(house - heater)
                if house in houses_to_radius:
                    currMinDistance = houses_to_radius[house]
                    if distance < currMinDistance:
                        houses_to_radius[house] = distance
                else:
                    houses_to_radius[house] = distance
                if house == heater:
                    # exit while condition / binary search
                    break
                elif house < heater:
                    r = m - 1
                else:
                    l = m + 1
        minReqDistance = 0 # max of min required distances
        for r in houses_to_radius.values():
            if r > minReqDistance: minReqDistance = r
        return minReqDistance
    # T: O(hlogn) where h is houses, or O(nlogn) - S: O(h)