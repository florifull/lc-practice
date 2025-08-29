class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find START of our increasing seq
            # when rightmost < leftmost AND middle > leftmost - means left:m is inc
            # SO, our right side window MUST hold start
        l, r = 0, len(nums) - 1
        minVal = float('inf')
        while l <= r:
            m = (l + r) // 2
            if nums[m] < minVal: minVal = nums[m]
            if nums[r] < nums[l] and nums[m] >= nums[l]:
                l = m + 1
            else: r = m - 1
        return minVal