class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        p2 = p3 = p5 = 0
        while len(res) < n:
            prod = min(res[p2]*2, res[p3]*3, res[p5]*5)
            res.append(prod)
            if prod == res[p2] * 2: p2 += 1
            if prod == res[p3] * 3: p3 += 1
            if prod == res[p5] * 5: p5 += 1
        return res[-1]
    # T: O(n), S: O(1)