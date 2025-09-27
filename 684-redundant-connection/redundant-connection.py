class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # The number of nodes is the same as the number of edges since the problem
        # states the input graph has N nodes and N edges (a tree plus one extra edge).
        n = len(edges)
        
        # 1. Initialize the parent array for Union-Find.
        # Initially, every node is its own parent. We use 1-based indexing for nodes,
        # so we need an array of size n + 1.
        parent = list(range(n + 1)) 

        # --- Helper functions for Union-Find ---
        
        # FIND operation with Path Compression
        def find(i):
            # If the current node 'i' is not the root of its set,
            # recursively call find and set its parent directly to the root (path compression).
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        # UNION operation (returns True if the union was successful, False if a cycle was detected)
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            
            # If the roots are the same, adding this edge (i, j) creates a cycle.
            # This is the redundant connection.
            if root_i == root_j:
                return False  # Cycle detected
            
            # If they are different, merge the sets by setting one root's parent to the other.
            parent[root_i] = root_j
            return True  # Union successful
        
        # --- Main Logic ---

        # 2. Iterate through the edges in the given order.
        for u, v in edges:
            # Try to unite the sets of node u and node v.
            # If the union operation fails (returns False), it means u and v were
            # already connected, and this edge (u, v) is the redundant connection.
            if not union(u, v):
                return [u, v]
        
        # This line should theoretically not be reached if the input is valid as per the problem.
        return []