class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {1:3, 2:2, 3:1} (number:it's occurences)
        # bucket = [[x, x, x, x, x, [x,y], [x]]
        count = collections.Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        # fill our bucket
        for num, occ in count.items():
            bucket[occ].append(num)
        # return k most freq elements
        print(bucket)
        ans = []
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                ans.extend(bucket[i][:])
                freq = len(bucket[i])
                k -= freq
                if k <= 0: break
        return ans