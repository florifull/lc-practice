class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 5, 5, 4, 3
        # A, B, A, B -> A:9, B: 8
        maxHeap = []
        for p in piles:
            heapq.heappush(maxHeap, -1 * p)
        a = b = 0
        turn = 2
        while maxHeap:
            absVal = abs(heapq.heappop(maxHeap))
            if turn % 2 == 0:
                a += absVal
            else:
                b += absVal
            turn += 1
        return a > b