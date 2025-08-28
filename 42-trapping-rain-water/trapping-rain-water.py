class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeftVals = [0] * len(height)
        l = 0
        maxValLeft = 0
        for i in range(1, len(height)):
            if maxValLeft < height[i - 1]:
                maxValLeft = height[i-1]
            maxLeftVals[i] = maxValLeft
        maxRightVals = [0] * len(height)
        maxValRight = 0
        for i in range(len(height) - 2, -1, -1):
            if maxValRight < height[i + 1]:
                maxValRight = height[i + 1]
            maxRightVals[i] = maxValRight
        # have a proper tracker for max val of left and right from ea height idx
        runningSum = 0
        for i, val in enumerate(height):
            waterAmount = min(maxLeftVals[i], maxRightVals[i]) - val
            if waterAmount > 0: runningSum += waterAmount
        return runningSum