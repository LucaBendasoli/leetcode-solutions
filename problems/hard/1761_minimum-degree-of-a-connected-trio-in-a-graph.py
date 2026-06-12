from typing import List

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        adj = [set() for _ in range(n + 1)]
        degree = [0] * (n + 1)
        
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1
        
        min_degree = float('inf')
        
        for i in range(1, n + 1):
            for j in adj[i]:
                if j > i:
                    for k in adj[i]:
                        if k > j and k in adj[j]:
                            trio_degree = degree[i] + degree[j] + degree[k] - 6
                            min_degree = min(min_degree, trio_degree)
        
        return min_degree if min_degree != float('inf') else -1