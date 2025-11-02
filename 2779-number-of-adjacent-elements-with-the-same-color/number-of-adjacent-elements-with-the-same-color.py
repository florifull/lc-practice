class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        counts = [0] * n # counts of colors related to their position..
        for i in range(len(queries)):
            modified_idx, newVal = queries[i][0], queries[i][1]
            oldVal = counts[modified_idx]
            counts[modified_idx] = newVal
            # adjust the pairs count based on the modified area..
            pairs = 0
            if oldVal == newVal:
                res[i] = res[i-1]
            # new val isn't equal to old val
            else:
                # if neighbors are 0's - ignore
                if modified_idx - 1 in range(len(counts)):
                    leftNei = counts[modified_idx-1]
                    if leftNei == 0:
                        pass
                    else:
                        if leftNei == oldVal: pairs -= 1
                        elif leftNei == newVal: pairs += 1
                if modified_idx + 1 in range(len(counts)):
                    rightNei = counts[modified_idx+1]
                    if rightNei == 0:
                        pass
                    else:
                        if rightNei == oldVal: pairs -= 1
                        elif rightNei == newVal: pairs += 1
                res[i] = res[i-1] + pairs
        return res
    # T: O(q * n), S: O(q)