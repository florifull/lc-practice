class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # take advantage of the fact sorted arr..
        l, r = 0, len(numbers) - 1
        while l < r:
            ourSum = numbers[l] + numbers[r]
            if ourSum == target: return [l+1, r+1]
            elif ourSum > target: r -= 1
            else: l += 1
        """
        T: O(n), S: O(n)
        nums = {}
        for i in range(len(numbers)):
            if target - numbers[i] in nums:
                return [1 + nums[target-numbers[i]], i + 1]
            nums[numbers[i]] = i
        """