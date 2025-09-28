class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nums = [10,9,2,5,3,7,101,18] -> [1, 1, 1, 2, 2, 3, 4, 4]
        res = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], 1 + res[j])
        return max(res)