class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_to_speed = {}
        # {start position : speed}
        for i in range(len(position)):
            position_to_speed[position[i]] = speed[i]
        fleets = 1
        position.sort(reverse = True) # decreasing (furthest start pos at 1st idx)
        # p much target - position gives us the distance to go, & distance / speed is time
        finishTime = (target - position[0]) / position_to_speed[position[0]]
        for i in range(1, len(position)):
            newFinishTime = (target - position[i]) / position_to_speed[position[i]]
            if newFinishTime > finishTime:
                finishTime = newFinishTime
                fleets += 1
        return fleets