import collections

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        # We define a nested function to handle the recursion using absolute indices l and r
        def findLongest(l, r):
            if r - l + 1 < k: return 0
            
            currString = s[l:r+1]
            counts = collections.Counter(currString)
            
            # 3. Find the Divider and Divide
            for i, char in enumerate(currString):
                
                if counts[char] < k:                    
                    # Calculate the absolute index (in the original string s) of the divider
                    abs_divider_index = l + i
                    
                    # Find the first index j of a character that is NOT an invalid divider
                    j = i
                    while j < len(currString) and counts[currString[j]] < k:
                        j += 1
                    
                    # Calculate the absolute index where the right segment starts
                    abs_right_start = l + j
                                        
                    # Left Segment: s[l : abs_divider_index]
                    left_result = findLongest(l, abs_divider_index - 1) 
                    
                    # Right Segment: s[abs_right_start : r + 1]
                    right_result = findLongest(abs_right_start, r)
                    
                    # We return the max of the two resulting subproblems for this step
                    return max(left_result, right_result)

            # If the loop finishes without returning, the entire current segment is valid.
            return r - l + 1
        return findLongest(0, len(s) - 1)