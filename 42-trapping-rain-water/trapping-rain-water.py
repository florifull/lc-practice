class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        totalWater = 0
        while l <= r:
            leftVal, rightVal = height[l], height[r]
            if leftVal > leftMax: leftMax = leftVal
            if rightVal > rightMax: rightMax = rightVal

            if leftMax <= rightMax:
                potentialWater = leftMax - height[l]
                if potentialWater > 0: totalWater += potentialWater
                l += 1
            elif rightMax <= leftMax:
                potentialWater = rightMax - height[r]
                if potentialWater > 0: totalWater += potentialWater
                r -= 1
        return totalWater