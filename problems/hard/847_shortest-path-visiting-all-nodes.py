from typing import List
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        full_mask = (1 << n) - 1

        visited = [[False] * n for _ in range(1 << n)]
        q = deque()

        for i in range(n):
            mask = 1 << i
            visited[mask][i] = True
            q.append((mask, i, 0))

        while q:
            mask, u, dist = q.popleft()

            if mask == full_mask:
                return dist

            for v in graph[u]:
                new_mask = mask | (1 << v)
                if not visited[new_mask][v]:
                    visited[new_mask][v] = True
                    q.append((new_mask, v, dist + 1))

        return -1