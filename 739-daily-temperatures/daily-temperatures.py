class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stack_i, stack_t = stack.pop()
                output[stack_i] = i - stack_i
            stack.append((i, t))
        return output
    # T: O(n), S: O(n)
    # stack holds smaller vals towards the top..
    # - ex stack in middle of running will hold [75, 71, 69]