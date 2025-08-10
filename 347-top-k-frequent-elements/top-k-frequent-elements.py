class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        ans = [[] for i in range(len(nums) + 1)]
        
        for num, occ in counts.items():
            ans[occ].append(num)
        ret = []
        for i in range(len(ans)-1, -1, -1):
            if ans[i]:
                ret.extend(ans[i][:])
                if len(ret) == k:
                    return ret
