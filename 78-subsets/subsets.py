class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(ans, i):
            res.append(ans[:])
            for j in range(i, len(nums)):
                ans.append(nums[j])
                dfs(ans, j+1)
                ans.pop()
            return
        dfs([], 0)
        return res
    # T: O(2^n * n), S: O(2^n * n)