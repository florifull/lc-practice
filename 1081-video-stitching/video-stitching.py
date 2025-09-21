class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # clips = [[0,2],[1,9],[1,5],[4,6],[5,9],[8,10]] -> ex: prevStart=0
        clips.sort()
        prevStart = count = i = 0
        while i < len(clips) and prevStart < time:
            maxEnd = prevStart
            while i < len(clips) and clips[i][0] <= prevStart:
                maxEnd = max(maxEnd, clips[i][1])
                i += 1
            if prevStart == maxEnd: return -1
            prevStart = maxEnd
            count += 1
        return count if prevStart >= time else -1