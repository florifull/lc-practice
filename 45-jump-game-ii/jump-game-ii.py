class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        jumps = 0
        while r < len(nums)-1:
            furthest = 0
            for i in range(l, r+1):
                if i + nums[i] > furthest:
                    furthest = i + nums[i]
            l, r = r+1, furthest
            jumps += 1
        return jumps
    # T: O(n), S: O(1)