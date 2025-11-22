class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(ans, arr):
            res.append(ans[:])
            for i in range(len(arr)):
                ans.append(arr[i])
                dfs(ans, arr[i+1:])
                ans.pop()
            return
        dfs([], nums)
        return res