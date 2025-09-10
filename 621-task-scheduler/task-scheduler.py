class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = collections.Counter(tasks)
        maxHeap = [(-1 * v) for v in taskMap.values()]
        heapq.heapify(maxHeap)
        # ex: ["A","C","A","B","D","B"] -> [-2, -2, -1, -1]
        qcooldown = collections.deque() # [count, cooloff]
        iterations = 0

        while maxHeap or qcooldown:
            iterations += 1
            if maxHeap: # take largest occurrence and use it
                count = heapq.heappop(maxHeap) + 1 # really subtracting but since negs..
                if count != 0:
                    qcooldown.append([count, iterations + n])
            if qcooldown:
                lowestCooldown = qcooldown[0][1]
                # we're ready to be removed again
                if lowestCooldown <= iterations:
                    count, _ = qcooldown.popleft()
                    heapq.heappush(maxHeap, count)
        return iterations