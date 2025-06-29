class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, val in enumerate(nums):
            # found a repeated leftmost value..
            if idx > 0 and val == nums[idx-1]: continue
            l, r = idx+1, len(nums) - 1
            while l < r:
                ourSum = val + nums[l] + nums[r]
                if ourSum == 0:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                elif ourSum < 0:
                    l += 1
                else:
                    r -= 1
        return res