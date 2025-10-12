class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prevSum = nums[0]
        globalSum = nums[0]
        for i in range(1, len(nums)):
            if prevSum < 0:
                prevSum = nums[i]
            else:
                prevSum += nums[i]
            globalSum = max(globalSum, prevSum)
        return globalSum
    # T: O(n), S: O(1) -> Kadane's algo