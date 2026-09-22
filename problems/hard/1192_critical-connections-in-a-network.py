from __future__ import annotations
import sys
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        sys.setrecursionlimit(10**6)
        
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Discovery times and low-link values
        disc = [-1] * n
        low = [0] * n
        time = 0
        ans = []
        
        def dfs(u: int, parent: int) -> None:
            nonlocal time
            disc[u] = low[u] = time
            time += 1
            
            for v in graph[u]:
                if v == parent:
                    continue
                if disc[v] == -1:         # tree edge
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        ans.append([u, v])
                else:                     # back edge
                    low[u] = min(low[u], disc[v])
        
        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)
        
        return ans