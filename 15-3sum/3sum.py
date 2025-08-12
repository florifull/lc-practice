class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l, r = 0, len(nums) - 1
        while l < r:
            r = len(nums) - 1
            m = l + 1
            while m < r:
                ourSum = nums[l] + nums[m] + nums[r]
                if ourSum == 0:
                    res.append([nums[l], nums[m], nums[r]])
                elif ourSum > 0:
                    r -= 1
                    continue
                m += 1
                while m < r and nums[m] == nums[m-1]:
                    m += 1
            l += 1
            while l < r and nums[l] == nums[l - 1]:
                l += 1
        return res