class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(nodeIndex, path):
            if nodeIndex == len(graph)-1:
                res.append(path[:])
                return
            for n in graph[nodeIndex]:
                path.append(n)
                dfs(n, path)
                path.pop()
            return
        dfs(0, [0]) 
        return res