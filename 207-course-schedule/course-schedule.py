class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = collections.defaultdict(list)
        for c, pre in prerequisites:
            prereq[c].append(pre)
        # [[1,0],[0,1]] => {1->[0], 0->[1]}
        # [[1, 0], [0, 3]] => {1-> [0], 0->[3]}, 3 has no prereqs so not in map...
        visited = set()
        def dfs(c):
            if c not in prereq: return True
            if c in visited: return False
            visited.add(c)
            for pre in prereq[c]:
                if not dfs(pre): return False
            visited.remove(c)
            prereq[c] = []
            return True
        for i in range(numCourses):
            if i in prereq:
                if not dfs(i): return False
        return True
    # T: O(V + E), S: O(V + E)