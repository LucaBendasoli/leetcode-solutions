from heapq import heappop, heappush
from typing import List

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, cnt in edges:
            w = cnt + 1
            graph[u].append((v, w))
            graph[v].append((u, w))

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            d, u = heappop(pq)
            if d != dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(pq, (nd, v))

        ans = sum(d <= maxMoves for d in dist)

        for u, v, cnt in edges:
            ans += min(cnt, max(0, maxMoves - dist[u]) + max(0, maxMoves - dist[v]))

        return ans