class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        class_to_pre = collections.defaultdict(list)
        visited = set()
        setres = set()
        for c, p in prerequisites:
            class_to_pre[c].append(p)
        # {1: [0], 2: [0], 3: [1, 2]}
        def dfs(i):
            if i in setres: return True
            if i not in class_to_pre:
                res.append(i)
                setres.add(i)
                return True
            if i in visited: return False # cycle detected
            visited.add(i)
            for c in class_to_pre[i]:
                if not dfs(c): return False
            visited.remove(i)
            res.append(i)
            setres.add(i)
            class_to_pre[i] = [] # able to be visited
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        return res
