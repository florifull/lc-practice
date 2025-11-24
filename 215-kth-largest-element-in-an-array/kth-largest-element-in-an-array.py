class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for n in nums:
            heapq.heappush(minHeap, -1 * n)
        i = 1
        while i < k:
            heapq.heappop(minHeap)
            i += 1
        return -1 * minHeap[0]
        # [6, 5, 5, 4, 3, 3, 2, 2, 1]