class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def dfs(path, node):
            # found target (n - 1 node aka len(graph)-1)
            if node == len(graph)-1:
                paths.append(path[:])
                return
            nei = graph[node]
            for n in nei:
                path.append(n)
                dfs(path, n)
                path.pop()
            return
        path = [0]
        dfs(path, 0)
        return paths
    # T: O(2^n * n), S: O(n)