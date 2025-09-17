class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # Store the furthest end point reachable from each starting position
        furthest_reach = [0] * time
      
        # Build the furthest reach array from all clips
        for start, end in clips:
            # Only consider clips that start before the target time
            if start < time:
                furthest_reach[start] = max(furthest_reach[start], end)
      
        # Initialize variables for the greedy algorithm
        num_clips = 0  # Number of clips used
        max_reach = 0   # Maximum position we can reach so far
        prev_end = 0    # End position of the last selected clip
      
        # Iterate through each position in the time interval
        for current_pos, furthest_from_here in enumerate(furthest_reach):
            # Update the maximum reachable position
            max_reach = max(max_reach, furthest_from_here)
          
            # If we can't reach beyond current position, there's a gap
            if max_reach <= current_pos:
                return -1
          
            # If we've reached the end of the previous clip's coverage
            if prev_end == current_pos:
                # Select a new clip that extends furthest
                num_clips += 1
                prev_end = max_reach
      
        return num_clips