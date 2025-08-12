class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(prefix)):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(len(prefix)-2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i+1]
        r_arr = [1] * len(nums)
        for i in range(len(r_arr)):
            r_arr[i] = prefix[i] * postfix[i]
        return r_arr