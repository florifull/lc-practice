class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}
        for i in range(len(numbers)):
            if target - numbers[i] in nums:
                return [1 + nums[target-numbers[i]], i + 1]
            nums[numbers[i]] = i