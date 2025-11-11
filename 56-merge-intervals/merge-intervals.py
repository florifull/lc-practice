class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals
        # starts: [1, 2, 8, 15]
        # ends:   [3, 6, 10, 18]

        # [[1, 10], [2, 3], [4, 5]]
        stack = []
        intervals.sort(key=lambda x:x[0])
        for i in range(len(intervals)):
            if i == 0:
                stack.append([intervals[i][0], intervals[i][1]])
                continue
            prevStart, prevEnd = stack.pop()
            currStart, currEnd = intervals[i][0], intervals[i][1]
            if currStart <= prevEnd:
                maxEnd = max(prevEnd, currEnd)
                stack.append([prevStart, maxEnd])
            else:
                stack.append([prevStart, prevEnd])
                stack.append([currStart, currEnd])
        return stack