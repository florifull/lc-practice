class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i, val in enumerate(index):
            res.insert(index[i], nums[i])
        return res
    # T: O(n^2), S: O(1)