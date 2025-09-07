class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []    # by default, min..
        for n in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, n)
            else:
                if minHeap[0] < n:
                    heapq.heappushpop(minHeap, n)
        return minHeap[0]