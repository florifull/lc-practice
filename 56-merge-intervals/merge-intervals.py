class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return [intervals[0]]

        intervals.sort()
        res = [[intervals[0][0], intervals[0][1]]] # initially holds first interval
        i = 1
        prevStart = prevEnd = 0
        while i < len(intervals):
            prevStart, prevEnd = res[-1][0], res[-1][1]
            currStart, currEnd = intervals[i][0], intervals[i][1]
            if currStart <= prevEnd: # found an overlap / time conflict..
                # create a new interval..
                res.pop()
                newStart, newEnd = prevStart, max(prevEnd, currEnd)
                res.append([newStart, newEnd])
            else:
                res.append([currStart, currEnd])
            i += 1
        return res
