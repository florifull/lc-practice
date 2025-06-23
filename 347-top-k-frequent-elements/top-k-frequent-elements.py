class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return [nums[0]]
        kMap = collections.Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        # fill bucket with index = occurence, val = val
        for num, count in kMap.items():
            bucket[count].append(num)
        ans = []
        for i in range(len(bucket)-1, 0, -1):
            ans.extend(bucket[i])
            if len(ans) >= k: break
        return ans