class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            # duplicate on left ptr
            if i > 0 and n == nums[i-1]:
                continue
            m, r = i + 1, len(nums) - 1
            while m < r:
                ourSum = n + nums[m] + nums[r]
                if ourSum == 0:
                    res.append([n, nums[m], nums[r]])
                elif ourSum > 0:
                    r -= 1
                    continue
                m += 1
                while m < r and nums[m] == nums[m-1]:
                    m += 1
        return res    