class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            number = nums[i]
            if len(res) >= index[i]+1:
                res.insert(index[i], number)
                continue
            res.append(number)
        return res