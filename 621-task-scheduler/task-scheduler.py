class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = collections.deque()
        counts = collections.Counter(tasks)
        maxHeap = [(-1 * v) for v in counts.values()]
        heapq.heapify(maxHeap)
        
        cycles = 0
        while cooldown or maxHeap:
            cycles += 1
            # if we have anything ready to pop, take 'largest'
            if maxHeap:
                # pop the 'largest' occurrence and subtract (add)
                occ = heapq.heappop(maxHeap) + 1
                if abs(occ) > 0:
                    # cycles rep round we're on, n is default cooldown time
                    # stored in q as... remaining occurrence count : cooldown period
                    cooldown.append([occ, cycles + n])
            if cooldown:
                # if something is almost ready to be used again
                if cycles >= cooldown[0][1]:
                    count, _ = cooldown.popleft()
                    heapq.heappush(maxHeap, count)
        return cycles