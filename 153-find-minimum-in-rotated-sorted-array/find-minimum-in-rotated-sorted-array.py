class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2: return nums[0]
        if len(nums) == 2: return min(nums[0], nums[1])
        # find START of our increasing seq
            # when rightmost < leftmost AND middle > leftmost - means left:m is inc
            # SO, our right side window MUST hold start
        l, r = 0, len(nums) - 1
        minVal = float('inf')
        while l <= r:
            m = (l + r) // 2
            if nums[m] < minVal: minVal = nums[m]
            if nums[r] <= nums[l] and nums[m] >= nums[l]:
                l = m + 1
            else: r = m - 1
        return minVal