class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(localSol, choices):
            if len(localSol) == len(nums):
                res.append(localSol[:])
                return
            # decisions
            for i in range(len(choices)):
                localSol.append(choices[i])
                dfs(localSol, choices[:i] + choices[i+1:])
                localSol.pop()
        dfs([], nums)
        return res
    # T: O(n * n!), S: O(n^2)