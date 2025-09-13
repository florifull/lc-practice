class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currSumArray):
            currSum = sum(currSumArray)
            if currSum == target:
                res.append(currSumArray[:])
                return
            if i >= len(candidates) or currSum > target: return

            currSumArray.append(candidates[i])
            # left
            dfs(i, currSumArray)
            # right
            currSumArray.pop()
            dfs(i+1, currSumArray)
            return
        
        dfs(0, [])
        return res