class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            # our left window is sorted..
            if nums[m] >= nums[l]:
                if target in range(nums[l], nums[m]):
                    r = m - 1
                else:
                    l = m + 1
            # right window is sorted..
            elif nums[m] < nums[r]:
                # target may be in right window
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1 