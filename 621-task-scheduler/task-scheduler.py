class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasksInfo = collections.Counter(tasks)
        storage = [[-1*occ, letter, 0] for letter, occ in tasksInfo.items()]
        heapq.heapify(storage)
        cooldown = collections.deque()

        i = 0 # intervals
        while storage or cooldown:
            i += 1
            if cooldown:
                # check if anything is cooled down..[char, occ, exp]
                while cooldown and cooldown[0][2] <= i:
                    occ, char, coolExp = cooldown.popleft()
                    heapq.heappush(storage, [occ, char, 0])
            # now use a task from our storage of ready-to-use tasks..
            if storage:
                occ, char, coolExp = heapq.heappop(storage)
                occ += 1
                if occ == 0: continue
                coolExp = i + n + 1
                cooldown.append([occ, char, coolExp])
        return i
    # O(m * n), S: O(1)