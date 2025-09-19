class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [73,74,75,71,69,72,76,73]
        # [[75, 2], 71, [69, 4]] -> [temp, idx]
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, idx = stack.pop()
                res[idx] = i - idx
            stack.append([t, i])
        return res