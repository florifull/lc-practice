class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        our_sum = sum(nums)
        if our_sum % 2 != 0: return False
        target = our_sum // 2
        
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            our_dp = dp.copy()
            for d in our_dp:
                dp.add(d + nums[i])
                
        return False if target not in dp else True