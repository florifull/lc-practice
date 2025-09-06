class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap..
        maxHeap = [(-1 * s) for s in stones]
        # heapify so max val at top (neg)
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)
            if y == x: continue
            y = -1 * (abs(y) - abs(x))
            heapq.heappush(maxHeap, y)
        return 0 if not maxHeap else abs(maxHeap[0])