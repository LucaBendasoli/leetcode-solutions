from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # Build adjacency list
        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        # Find initial leaves
        leaves = deque()
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
        
        # Remove leaves layer by layer
        remaining = n
        while remaining > 2:
            leaves_count = len(leaves)
            remaining -= leaves_count
            
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                # Remove this leaf from its neighbor
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                
                # If neighbor becomes a leaf, add to queue
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)
        
        # Remaining nodes are the centers
        return list(leaves)