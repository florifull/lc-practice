class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i, num in enumerate(nums):
            if target - num in num_to_idx:
                return [num_to_idx[target-num], i]
            num_to_idx[num] = i
    # T: O(n), S: O(n)