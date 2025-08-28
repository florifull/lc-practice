class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ''
        tOccs = collections.Counter(t)
        sOccs = {}
        totalS, totalT = 0, len(t)  # keeps count of min required chars for valid window
        l = 0
        minL, twoPtrs = float('inf'), [-1, -1]

        for r, sChar in enumerate(s):
            if sChar in tOccs:
                sOccs[sChar] = sOccs.get(sChar, 0) + 1
                if sOccs[sChar] <= tOccs[sChar]:
                    totalS += 1
            while totalS == totalT:
                if r - l + 1 < minL:
                    minL = r - l + 1
                    twoPtrs = [l, r]
                if s[l] in tOccs:
                    if sOccs[s[l]] == tOccs[s[l]]:
                        totalS -= 1
                    sOccs[s[l]] -= 1
                l += 1
        return s[twoPtrs[0]:twoPtrs[1]+1] if minL != float('inf') else ''
    # T: O(n), S: O(m)