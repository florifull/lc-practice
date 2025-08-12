class Solution:
    def maxArea(self, height: List[int]) -> int:
        # area = min(height[l], height[r]) * r-l
        l, r = 0, len(height) - 1
        maxA = 0
        while l < r:
            localA = min(height[l], height[r]) * (r - l)
            maxA = max(maxA, localA)
            if height[r] < height[l]:
                r -= 1
                continue
            l += 1
        return maxA
        # T: O(n), S: O(1)