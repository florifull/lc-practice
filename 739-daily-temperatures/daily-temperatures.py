class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []  # monotonic decreasing (only push vals less than top)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_temp, stack_i = stack.pop()
                answer[stack_i] = i - stack_i
            stack.append([t, i])
        return answer
    # T: O(n), S: O(n)