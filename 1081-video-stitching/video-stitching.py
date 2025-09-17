class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        
        count = 0
        end = 0  # Represents the current furthest reach
        i = 0
        
        while end < time:
            new_end = end
            
            # Find the best clip to make the next jump
            while i < len(clips) and clips[i][0] <= end:
                new_end = max(new_end, clips[i][1])
                i += 1
            
            # If no progress was made, it's impossible to stitch
            if new_end == end:
                return -1
            
            # Make the jump and increment the count
            end = new_end
            count += 1
            
        return count

# [[0,2], [1,5], [1,9],[4,6],[5,9],[8,10]]