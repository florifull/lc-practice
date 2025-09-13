class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, sumArray, localSum):
            if localSum == target:
                res.append(sumArray[:])
                return
            if i >= len(candidates) or localSum > target: return

            # left
            sumArray.append(candidates[i])
            dfs(i+1, sumArray, localSum + candidates[i])
            # right
            sumArray.pop()
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            dfs(i, sumArray, localSum)
            return
        dfs(0, [], 0)
        return res