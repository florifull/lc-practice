class Solution:
    def search(self, nums: List[int], target: int) -> int:
        targetIdx = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: return m
            # determine sorted halfs
            if nums[m] <= nums[r]: # right side is sorted
                # strictly increasing rightside - nums[m] < target < nums[r]
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] >= nums[l]: # leftside is sorted
                # strictly increasing leftside - nums[l] < target < nums[m]
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1 