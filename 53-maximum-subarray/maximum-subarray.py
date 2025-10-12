class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prevSum = nums[0]
        globalSum = float('-inf')
        for i in range(1, len(nums)):
            globalSum = max(globalSum, prevSum)
            if prevSum < 0 and nums[i] > prevSum:
                prevSum = nums[i]
            else:
                prevSum += nums[i]
            globalSum = max(globalSum, prevSum)
        return globalSum if len(nums) > 1 else nums[0]