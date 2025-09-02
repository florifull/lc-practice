class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]: return val
        return -1