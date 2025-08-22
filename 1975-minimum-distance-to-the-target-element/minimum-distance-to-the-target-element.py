class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minVal = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                minVal = min(minVal, abs(i - start))
        return minVal
        # T: O(n), S: O(1)