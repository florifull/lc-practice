class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.sol = []

        def dfs(i, arr):
            if i > len(nums) - 1:
                self.sol.append(arr[:])
                return
            arr.append(nums[i])
            left = dfs(i+1, arr)
            arr.pop()
            right = dfs(i+1, arr)
            return
            
        dfs(0, [])
        return self.sol