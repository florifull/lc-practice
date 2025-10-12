class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums = [3,2,1,1,0]
        max_idx = 0
        for i, val in enumerate(nums):
            if max_idx == i and nums[i] == 0 and i < len(nums)-1: return False
            curr_max_jump = i + nums[i]
            max_idx = max(max_idx, curr_max_jump)
        return max_idx >= len(nums)-1
