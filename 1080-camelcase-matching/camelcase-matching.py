class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def helper(query):
            l = 0
            for c in query:
                if l < len(pattern) and c == pattern[l]:
                    l += 1
                elif c.isupper(): return False
            return l == len(pattern)
        res = []
        for query in queries:
            res.append(helper(query))
        return res