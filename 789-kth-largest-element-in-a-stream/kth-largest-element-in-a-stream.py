class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k = nums, k
        heapq.heapify(self.nums)
        while len(nums) > k:
            heapq.heappop(nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val >= self.nums[0]:
            # replace smallest val with new val (can also use heapq.heappushpop..)
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)
        return self.nums[0]
    # T: O(nlogk), S: O(k)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)