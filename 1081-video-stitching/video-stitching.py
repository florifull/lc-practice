class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        hops = 0
        prevStart = newStart = 0
        # [[0,2],[0, 1],[1,5],[1, 9],[4,6],[5,9],[8,10]]

        # [[0,0],[0,6],[1,8],[2,3],[4,5],[5,7],[5,10],[7,10]]
        i = 0
        while i < len(clips) and prevStart < time:
            while i < len(clips) and clips[i][0] <= prevStart:
                # tells us how far we can hop to for said start..
                newStart = max(newStart, clips[i][1])
                i += 1
            if prevStart == newStart: return -1
            prevStart = newStart
            hops += 1
        return hops if prevStart >= time else -1
    # T: O(nlogn), S: O(1)