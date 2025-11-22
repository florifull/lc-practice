class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, ans):
            res.append(ans[:])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                ans.append(nums[j])
                dfs(j+1, ans)
                ans.pop()
            return
        dfs(0, [])
        return res
     # T: O(n * 2^n), S: O(n * 2^n)