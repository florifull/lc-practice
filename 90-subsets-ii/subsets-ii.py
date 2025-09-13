class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, localSol):
            if i >= len(nums):
                res.append(localSol[:])
                return
            
            # left
            localSol.append(nums[i])
            dfs(i+1, localSol)
            # right
            localSol.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            dfs(i, localSol)
            return
        dfs(0, [])
        return res