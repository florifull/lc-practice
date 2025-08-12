class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        occ = set(nums)
        maxL = 0
        for n in occ:
            # start of a sequence
            if n-1 not in occ:
                seqL = 1
                while n + 1 in occ:
                    n += 1
                    seqL += 1
                maxL = max(maxL, seqL)
        return maxL
