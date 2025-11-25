class Solution:
    def rob(self, nums: List[int]) -> int:
        two_houses_back = one_house_back = 0
        for currH in nums:
            maxP = max(two_houses_back + currH, one_house_back)
            two_houses_back, one_house_back = one_house_back, maxP
        return one_house_back