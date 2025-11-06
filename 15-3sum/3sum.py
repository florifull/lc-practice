class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = 0
        res = []
        while l < len(nums):
            if l > 0 and nums[l] == nums[l-1]:
                l += 1
                continue
            m, r = l + 1, len(nums) - 1
            while m < r:
                if m - 1 != l and nums[m] == nums[m-1]:
                    m += 1
                    continue
                ourSum = nums[l] + nums[m] + nums[r]
                if ourSum > 0:
                    r -= 1
                    continue
                elif ourSum == 0:
                    res.append([nums[l], nums[m], nums[r]])
                m += 1
            l += 1
        return res
        # nums = [-1,0,1,2,-1,-4] -> [-4, -4, -4, -1, 0, 1, 2]
