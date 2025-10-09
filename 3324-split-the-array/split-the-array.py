class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        occs = collections.Counter(nums)
        for v in occs.values():
            if v > 2: return False
        return True