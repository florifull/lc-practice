class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap..
        maxHeap = []
        points_to_euclidean = collections.defaultdict(list)

        for x, y in points:
            euclidean = math.sqrt((x ** 2) + (y ** 2))
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, -1 * euclidean)
                points_to_euclidean[-1 * euclidean].append([x, y])
            else:
                # found a smaller element than our largest val of k CLOSEST points
                if euclidean < abs(maxHeap[0]):
                    heapq.heappushpop(maxHeap, -1 * euclidean)
                    points_to_euclidean[-1 * euclidean].append([x, y])
        res = []
        visited = set()
        for euc in maxHeap:
            if euc not in visited:
                points = points_to_euclidean[euc]
                # add all []'s into our res array
                res.extend(points)
                visited.add(euc)
        return res