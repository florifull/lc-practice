class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        our_nums, seen = set(nums), set()
        longestSeq = 1
        for n in nums:
            # beginng of a sequence
            if n-1 not in our_nums and n not in seen:
                currLen = 1
                seen.add(n)
                while n + 1 in our_nums:
                    n += 1
                    currLen += 1
                    seen.add(n)
                longestSeq = max(longestSeq, currLen)
        return longestSeq