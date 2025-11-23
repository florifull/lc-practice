class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # permutations -> n! - where n is the length of nums
        res = []
        def dfs(ans, arr):
            if len(ans) == len(nums):
                res.append(ans[:])
                return
            for i in range(len(arr)):
                ans.append(arr[i])
                dfs(ans, arr[:i]+arr[i+1:])
                ans.pop()
            return
        dfs([], nums)
        return res
    # T: O(n * n!), S: O(n * n!)